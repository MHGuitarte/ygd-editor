#!/bin/bash
# Runs install.sh against a local server: a good release, a tampered checksum, an app signed by
# someone else, and a release with no build for this Mac. The good case uses the real zip of the
# latest release, downloaded once into $YGD_TEST_CACHE. macOS only. Usage: tools/test-install.sh
set -euo pipefail
cd "$(dirname "$0")/.."
[ "$(uname -s)" = Darwin ] || { echo 'macOS only'; exit 1; }

case "$(uname -m)" in
  arm64) ARCH=arm64 ;;
  *) if [ "$(sysctl -n sysctl.proc_translated 2>/dev/null || echo 0)" = 1 ]; then ARCH=arm64; else ARCH=x64; fi ;;
esac
OTHER=$([ "$ARCH" = arm64 ] && echo x64 || echo arm64)
CACHE="${YGD_TEST_CACHE:-${TMPDIR:-/tmp}/ygd-install-test}"
WORK="$(mktemp -d)"
SERVER_PID=
cleanup() {
  if [ -n "$SERVER_PID" ]; then kill "$SERVER_PID" 2>/dev/null; wait "$SERVER_PID" 2>/dev/null || true; fi
  rm -rf "$WORK"
}
trap cleanup EXIT

# The real zip of the latest release, once.
mkdir -p "$CACHE"
curl -fsSL https://github.com/MHGuitarte/ygd-editor/releases/latest/download/SHA256SUMS.txt -o "$CACHE/SHA256SUMS.txt"
LINE=$(grep -E "  ygd-editor-[0-9][^ ]*-mac-$ARCH\.zip$" "$CACHE/SHA256SUMS.txt")
ZIP=${LINE#*  }
SUM=${LINE%%  *}
if [ ! -f "$CACHE/$ZIP" ] || [ "$(shasum -a 256 "$CACHE/$ZIP" | awk '{print $1}')" != "$SUM" ]; then
  echo "downloading $ZIP once into $CACHE"
  curl -fL --progress-bar "https://github.com/MHGuitarte/ygd-editor/releases/latest/download/$ZIP" -o "$CACHE/$ZIP"
fi

# The same app re-signed ad-hoc: valid signature, wrong certificate.
mkdir "$WORK/adhoc"
ditto -x -k "$CACHE/$ZIP" "$WORK/adhoc"
codesign --force --deep -s - "$WORK/adhoc/ygd-editor.app" 2>/dev/null
ditto -c -k --keepParent "$WORK/adhoc/ygd-editor.app" "$WORK/adhoc.zip"
rm -rf "$WORK/adhoc"

PORT=$(python3 -c 'import socket; s = socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1])')
mkdir "$WORK/srv"
python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$WORK/srv" >/dev/null 2>&1 &
SERVER_PID=$!
for _ in $(seq 50); do curl -fs "http://127.0.0.1:$PORT/" >/dev/null && break; sleep 0.1; done

FAILED=0
# release <zip file to serve> <SHA256SUMS.txt line> : lays out one release in the server's directory.
release() {
  rm -rf "$WORK/srv"/*
  cp "$1" "$WORK/srv/$ZIP"
  printf '%s\n' "$2" > "$WORK/srv/SHA256SUMS.txt"
}
# run <name> [cat] : runs install.sh into a fresh directory; `cat` pipes it into bash as curl would.
run() {
  rm -rf "$WORK/apps" && mkdir "$WORK/apps"
  local env=(YGD_RELEASES_URL="http://127.0.0.1:$PORT" YGD_INSTALL_DIR="$WORK/apps" YGD_NO_OPEN=1)
  set +e
  if [ "${2:-}" = cat ]; then OUT=$(cat install.sh | env "${env[@]}" bash 2>&1); else OUT=$(env "${env[@]}" bash install.sh 2>&1); fi
  CODE=$?
  set -e
}
check() { # check <name> <condition…>
  local name=$1; shift
  if "$@"; then echo "ok   $name"; else echo "FAIL $name"; echo "$OUT" | sed 's/^/     /'; FAILED=1; fi
}
installed() { [ -d "$WORK/apps/ygd-editor.app" ]; }
not_installed() { [ ! -e "$WORK/apps/ygd-editor.app" ]; }
says() { echo "$OUT" | grep -q "$1"; }

# 1. A good release, piped into bash as curl would, over an existing copy.
release "$CACHE/$ZIP" "$SUM  $ZIP"
rm -rf "$WORK/apps" && mkdir -p "$WORK/apps/ygd-editor.app" && touch "$WORK/apps/ygd-editor.app/old-copy"
set +e; OUT=$(cat install.sh | env YGD_RELEASES_URL="http://127.0.0.1:$PORT" YGD_INSTALL_DIR="$WORK/apps" YGD_NO_OPEN=1 bash 2>&1); CODE=$?; set -e
check 'good release installs' [ "$CODE" = 0 ]
check 'good release replaces the old copy' [ ! -e "$WORK/apps/ygd-editor.app/old-copy" ]
check 'installed app verifies' codesign --verify --deep --strict "$WORK/apps/ygd-editor.app"
check 'installed app has no quarantine' bash -c "! xattr -p com.apple.quarantine '$WORK/apps/ygd-editor.app' >/dev/null 2>&1"

# 2. A checksum that does not match the zip.
release "$CACHE/$ZIP" "$(printf '0%.0s' $(seq 64))  $ZIP"
run tampered
check 'wrong checksum is refused' [ "$CODE" != 0 ]
check 'wrong checksum says so' says 'checksum'
check 'wrong checksum installs nothing' not_installed

# 3. An app with a valid signature from another certificate.
release "$WORK/adhoc.zip" "$(shasum -a 256 "$WORK/adhoc.zip" | awk '{print $1}')  $ZIP"
run adhoc
check 'ad-hoc signed app is refused' [ "$CODE" != 0 ]
check 'ad-hoc signed app says so' says 'certificate'
check 'ad-hoc signed app installs nothing' not_installed

# 4. A release with a build for the other architecture only.
release "$CACHE/$ZIP" "$SUM  ${ZIP/-mac-$ARCH.zip/-mac-$OTHER.zip}"
run noarch
check 'no build for this Mac is refused' [ "$CODE" != 0 ]
check 'no build for this Mac says so' says 'no build for this Mac'

exit $FAILED
