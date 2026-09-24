#!/bin/bash
# ygd-editor for macOS, installed from Terminal:
#
#   curl -fsSL https://mhguitarte.github.io/ygd-editor/install.sh | bash
#
# The app is signed with the project's own certificate, not an Apple Developer ID, so a copy
# downloaded through a browser makes macOS ask for "Open Anyway" in System Settings. A file curl
# writes carries no quarantine attribute and macOS does not ask. What Gatekeeper would have checked,
# this checks instead: the zip against the release's SHA256SUMS.txt, and the app's signature against
# the project certificate pinned below (https://mhguitarte.github.io/ygd-editor/#genuine). Run it
# again at any time to reinstall the latest version. Nothing here uses sudo.
#
# Everything runs from the call on the last line, so a download cut off halfway runs nothing.
set -euo pipefail

# SHA-1 of the project certificate (release-signing.pem); tools/build.py fails when they differ.
YGD_PIN_SHA1='79A40643BDFE500AB6730154B03B336C1809C57C'
YGD_PAGE='https://mhguitarte.github.io/ygd-editor/'
YGD_TMP=

ygd_fail() {
  printf 'ygd-editor: %s\n' "$*" >&2
  exit 1
}

ygd_install() {
  # Test-only overrides: where the release is read from, where the app goes, and not opening it.
  local releases="${YGD_RELEASES_URL:-https://github.com/MHGuitarte/ygd-editor/releases/latest/download}"
  local dest="${YGD_INSTALL_DIR:-}"

  [ "$(uname -s)" = Darwin ] || ygd_fail "this installer is for macOS; download ygd-editor for your system from $YGD_PAGE"

  # Apple Silicon also when this shell runs under Rosetta.
  local arch
  case "$(uname -m)" in
    arm64) arch=arm64 ;;
    x86_64) if [ "$(sysctl -n sysctl.proc_translated 2>/dev/null || echo 0)" = 1 ]; then arch=arm64; else arch=x64; fi ;;
    *) ygd_fail "unsupported Mac architecture: $(uname -m)" ;;
  esac

  YGD_TMP="$(mktemp -d)"
  trap 'rm -rf "$YGD_TMP"' EXIT

  # One request gives the file name, the version and the hash, with no API rate limit.
  printf 'Looking for the latest ygd-editor for macOS (%s)…\n' "$arch"
  curl -fsSL "$releases/SHA256SUMS.txt" -o "$YGD_TMP/SHA256SUMS.txt" || ygd_fail "could not read $releases/SHA256SUMS.txt"
  local line sum file version
  line="$(awk -v a="$arch" '{ f = $2; sub(/^\*/, "", f) } f ~ ("^ygd-editor-[0-9][^ ]*-mac-" a "\\.zip$") { print $1, f; exit }' "$YGD_TMP/SHA256SUMS.txt")"
  [ -n "$line" ] || ygd_fail "the latest release has no build for this Mac ($arch); see $YGD_PAGE"
  sum="${line%% *}"
  file="${line#* }"
  version="${file#ygd-editor-}"
  version="${version%-mac-$arch.zip}"
  printf '%s' "$sum" | grep -Eq '^[0-9a-f]{64}$' || ygd_fail "SHA256SUMS.txt has no valid checksum for $file"

  printf 'Downloading ygd-editor %s…\n' "$version"
  curl -fL --progress-bar "$releases/$file" -o "$YGD_TMP/$file" || ygd_fail "could not download $releases/$file"
  local got
  got="$(shasum -a 256 "$YGD_TMP/$file" | awk '{ print $1 }')"
  [ "$got" = "$sum" ] || ygd_fail "checksum mismatch for $file (expected $sum, got $got); nothing was installed"

  mkdir "$YGD_TMP/unpacked"
  ditto -x -k "$YGD_TMP/$file" "$YGD_TMP/unpacked" || ygd_fail "could not unpack $file"
  local app="$YGD_TMP/unpacked/ygd-editor.app"
  [ -d "$app" ] || ygd_fail "$file does not contain ygd-editor.app; nothing was installed"
  codesign --verify --deep --strict "$app" 2>/dev/null || ygd_fail "the app's signature does not verify; nothing was installed"
  codesign -d --extract-certificates="$YGD_TMP/cert-" "$app" 2>/dev/null || true
  [ -f "$YGD_TMP/cert-0" ] || ygd_fail "the app is not signed with a certificate (ad-hoc or unsigned); nothing was installed"
  local leaf
  leaf="$(shasum -a 1 "$YGD_TMP/cert-0" | awk '{ print toupper($1) }')"
  [ "$leaf" = "$YGD_PIN_SHA1" ] || ygd_fail "the app is signed with a certificate that is not the project's (SHA-1 $leaf); nothing was installed"

  if [ -z "$dest" ]; then
    if [ -w /Applications ]; then dest=/Applications; else dest="$HOME/Applications"; fi
  fi
  mkdir -p "$dest" || ygd_fail "could not create $dest"
  local target="$dest/ygd-editor.app"

  # Quitting it here could start an install-on-quit of an update the app already downloaded.
  if pgrep -f "$target/Contents/MacOS/ygd-editor" >/dev/null 2>&1; then
    ygd_fail "ygd-editor is running from $dest; quit it, then run this command again"
  fi

  if [ -e "$target" ]; then
    mv "$target" "$YGD_TMP/previous.app" || ygd_fail "could not move the existing $target aside; nothing was changed"
  fi
  if ! mv "$app" "$target"; then
    if [ -e "$YGD_TMP/previous.app" ]; then mv "$YGD_TMP/previous.app" "$target" || true; fi
    ygd_fail "could not install into $dest; the previous copy was kept"
  fi

  printf 'ygd-editor %s is installed in %s.\n' "$version" "$dest"
  if [ -z "${YGD_NO_OPEN:-}" ]; then open "$target"; fi
}

ygd_install
