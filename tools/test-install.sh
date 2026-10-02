#!/bin/bash
# Runs install.sh against a local server: a good release, checksums whose signature is missing, does
# not match or was made by another key, a zip that does not match its checksum, an app signed by
# someone else, and a release with no build for this Mac. The good case uses the real zip, checksums
# and signature of the latest release, downloaded once into $YGD_TEST_CACHE. The cases past the
# signature check sign their own checksums with a throwaway key and hand install.sh its certificate
# (YGD_TEST_SIGNING_CERT); the code-signature pin stays the project's. macOS only.
# Usage: tools/test-install.sh
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

# The real zip of the latest release, once, with its checksums and their signature.
mkdir -p "$CACHE"
curl -fsSL https://github.com/MHGuitarte/ygd-editor/releases/latest/download/SHA256SUMS.txt -o "$CACHE/SHA256SUMS.txt"
curl -fsSL https://github.com/MHGuitarte/ygd-editor/releases/latest/download/SHA256SUMS.txt.sig -o "$CACHE/SHA256SUMS.txt.sig"
LINE=$(grep -E "  ygd-editor-[0-9][^ ]*-mac-$ARCH\.zip$" "$CACHE/SHA256SUMS.txt")
ZIP=${LINE#*  }
SUM=${LINE%%  *}
if [ ! -f "$CACHE/$ZIP" ] || [ "$(shasum -a 256 "$CACHE/$ZIP" | awk '{print $1}')" != "$SUM" ]; then
  echo "downloading $ZIP once into $CACHE"
  curl -fL --progress-bar "https://github.com/MHGuitarte/ygd-editor/releases/latest/download/$ZIP" -o "$CACHE/$ZIP"
fi

# A key that is not the project's, to sign checksums install.sh must refuse, or, handed its
# certificate, accept so that the later checks are reached.
openssl req -x509 -newkey rsa:2048 -sha256 -days 1 -nodes -subj '/CN=not the project' \
  -keyout "$WORK/other.key" -out "$WORK/other.pem" 2>/dev/null
sign() { openssl dgst -sha256 -sign "$WORK/other.key" -out "$WORK/srv/SHA256SUMS.txt.sig" "$WORK/srv/SHA256SUMS.txt"; }

# The real zip with one byte more: a download that does not match its checksum.
cp "$CACHE/$ZIP" "$WORK/corrupt.zip" && printf 'x' >> "$WORK/corrupt.zip"

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
# release <zip file to serve> <SHA256SUMS.txt line> : lays out one release in the server's directory,
# without a signature; `real` and `sign` add one.
release() {
  rm -rf "$WORK/srv"/*
  cp "$1" "$WORK/srv/$ZIP"
  printf '%s\n' "$2" > "$WORK/srv/SHA256SUMS.txt"
}
real() { cp "$CACHE/SHA256SUMS.txt" "$CACHE/SHA256SUMS.txt.sig" "$WORK/srv/"; }
# run <name> [cat|other] : runs install.sh into a fresh directory; `cat` pipes it into bash as curl
# would, `other` makes it check the signature against the throwaway certificate.
run() {
  rm -rf "$WORK/apps" && mkdir "$WORK/apps"
  local env=(YGD_RELEASES_URL="http://127.0.0.1:$PORT" YGD_INSTALL_DIR="$WORK/apps" YGD_NO_OPEN=1)
  if [ "${2:-}" = other ]; then env+=(YGD_TEST_SIGNING_CERT="$WORK/other.pem"); fi
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
release "$CACHE/$ZIP" "$SUM  $ZIP" && real
rm -rf "$WORK/apps" && mkdir -p "$WORK/apps/ygd-editor.app" && touch "$WORK/apps/ygd-editor.app/old-copy"
set +e; OUT=$(cat install.sh | env YGD_RELEASES_URL="http://127.0.0.1:$PORT" YGD_INSTALL_DIR="$WORK/apps" YGD_NO_OPEN=1 bash 2>&1); CODE=$?; set -e
check 'good release installs' [ "$CODE" = 0 ]
check 'good release replaces the old copy' [ ! -e "$WORK/apps/ygd-editor.app/old-copy" ]
check 'installed app verifies' codesign --verify --deep --strict "$WORK/apps/ygd-editor.app"
check 'installed app has no quarantine' bash -c "! xattr -p com.apple.quarantine '$WORK/apps/ygd-editor.app' >/dev/null 2>&1"

# 2. Checksums with no signature.
release "$CACHE/$ZIP" "$SUM  $ZIP"
run unsigned
check 'unsigned checksums are refused' [ "$CODE" != 0 ]
check 'unsigned checksums say so' says 'SHA256SUMS.txt.sig'
check 'unsigned checksums install nothing' not_installed

# 3. Checksums changed after they were signed: the project's signature, another file.
release "$CACHE/$ZIP" "$SUM  $ZIP" && real && printf '%s\n' "$(printf '0%.0s' $(seq 64))  extra.zip" >> "$WORK/srv/SHA256SUMS.txt"
run altered
check 'altered checksums are refused' [ "$CODE" != 0 ]
check 'altered checksums say so' says 'signature'
check 'altered checksums install nothing' not_installed

# 4. Checksums that match the zip, signed with a key that is not the project's.
release "$CACHE/$ZIP" "$SUM  $ZIP" && sign
run foreign
check 'checksums signed by another key are refused' [ "$CODE" != 0 ]
check 'checksums signed by another key say so' says 'signature'
check 'checksums signed by another key install nothing' not_installed

# 5. A zip that does not match its (genuinely signed) checksum.
release "$WORK/corrupt.zip" "$SUM  $ZIP" && real
run corrupt
check 'wrong checksum is refused' [ "$CODE" != 0 ]
check 'wrong checksum says so' says 'checksum mismatch'
check 'wrong checksum installs nothing' not_installed

# 6. An app with a valid signature from another certificate, past the checksum checks.
release "$WORK/adhoc.zip" "$(shasum -a 256 "$WORK/adhoc.zip" | awk '{print $1}')  $ZIP" && sign
run adhoc other
check 'ad-hoc signed app is refused' [ "$CODE" != 0 ]
check 'ad-hoc signed app says so' says 'certificate'
check 'ad-hoc signed app installs nothing' not_installed

# 7. A release with a build for the other architecture only.
release "$CACHE/$ZIP" "$SUM  ${ZIP/-mac-$ARCH.zip/-mac-$OTHER.zip}" && sign
run noarch other
check 'no build for this Mac is refused' [ "$CODE" != 0 ]
check 'no build for this Mac says so' says 'no build for this Mac'

exit $FAILED
