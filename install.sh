#!/bin/bash
# ygd-editor for macOS, installed from Terminal:
#
#   curl -fsSL https://mhguitarte.github.io/ygd-editor/install.sh | bash
#
# The app is signed with the project's own certificate, not an Apple Developer ID, so a copy
# downloaded through a browser makes macOS ask for "Open Anyway" in System Settings. A file curl
# writes carries no quarantine attribute and macOS does not ask. What Gatekeeper would have checked,
# this checks instead, and stops at the first check that fails: the signature of the release's
# SHA256SUMS.txt against the project certificate embedded below, the zip against that SHA256SUMS.txt,
# and the app's code signature against the same certificate's pinned fingerprint
# (https://mhguitarte.github.io/ygd-editor/#genuine). Run it again at any time to reinstall the latest
# version. Nothing here uses sudo.
#
# Everything runs from the call on the last line, so a download cut off halfway runs nothing.
set -euo pipefail

# SHA-1 of the project certificate (release-signing.pem); tools/build.py fails when they differ.
YGD_PIN_SHA1='79A40643BDFE500AB6730154B03B336C1809C57C'
# The project certificate itself, byte for byte release-signing.pem (tools/build.py fails when they
# differ). Its key signs SHA256SUMS.txt, so the checksums are trusted only once that signature verifies.
YGD_CERT='-----BEGIN CERTIFICATE-----
MIIElDCCAvygAwIBAgIUYI5mADQb+6nXJXTyqf2T2kEVijkwDQYJKoZIhvcNAQEL
BQAwRzEjMCEGA1UEAwwaeWdkLWVkaXRvciByZWxlYXNlIHNpZ25pbmcxEzARBgNV
BAoMCk1IR3VpdGFydGUxCzAJBgNVBAYTAkVTMB4XDTI2MDkxMzExMjUxMFoXDTM2
MDkxMDExMjUxMFowRzEjMCEGA1UEAwwaeWdkLWVkaXRvciByZWxlYXNlIHNpZ25p
bmcxEzARBgNVBAoMCk1IR3VpdGFydGUxCzAJBgNVBAYTAkVTMIIBojANBgkqhkiG
9w0BAQEFAAOCAY8AMIIBigKCAYEAyKVyUZBcX8rFIwH+PfJxP1bcoQvvbQgCsTYP
INLHZqkFZjCKPKa91yFaFIRvRJF3mj61nIkibwhdAda8RqYJlRxrrnOw/dfaYzF6
lySg0FGerzdCx11Bvx6DxrjOc2cD2zTQzt5+A3ff8zdaDpZM/7RyWF5Mijq6Ax8X
d/6i30P/sQRzqfqUNWVh9S3iT17p3iI4mnyI6o0cvZIYUbFgpiVkoJoX7ZH/JZDE
sTTjvj2v/PpGqGTMfRgw8iauLIvQpq8ohC5nU2iY5RsidFIeeP/OI6sh424Yi370
fyTKE4hjJcxB08AVggV1sOGrcqGF9zFcl8IoqCwYxf6fnkiAjtuNrFTMpCb000VQ
KLSHEcnrWeQAj8nfDvdSpx9s6efRwMGLaPT4QJtR8IiOySxqXxg9Rw0UC+K97fFT
9xntTujxn+A9Az+Im+RDhAJLeUZw6yha75HVYGOCpec/Qvk1KqW/mT+Irtcjs8vJ
Qt35uIgNHH6i+F3nF57NYQlOYco7AgMBAAGjeDB2MB8GA1UdIwQYMBaAFILQIXJd
o1NpT1ZUIuhez3SZKnVVMA4GA1UdDwEB/wQEAwIHgDAWBgNVHSUBAf8EDDAKBggr
BgEFBQcDAzAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBSC0CFyXaNTaU9WVCLoXs90
mSp1VTANBgkqhkiG9w0BAQsFAAOCAYEAZdBMyiNUZHGwX+nQbHkZDVbQkqKOgAUK
y4LpFMPjx/Gf06E8ceeAN7HIi0l/D+XkUIGEZFAsaV7Hyw7r6T8TJYwfp5pFGmpB
2UXmozAbp4uPJmtVJB+j6EMgE0S8hftgy/980A1uCQnS0aubet4SoA1MFiewqrt6
11iU4uDGzFSza91CHsAJLn1Ny3JAuqAPwEYiDXEIe/r/famM2SSN4Ll3cg4emzBV
SujNPrRBLv7MpIG9rkAuejOyBkrAGA7X5EVprLqZzI3kMJKmiDxiWqH6nMdqZJE6
l+SHeFMmFQpo88rqcyEoexNA2NUHNAbnrD8lGBYqU/wbgWlW+kjCe8hmmztGIf4U
2VUeSaFvLeoOM5O8HoW309si3VA126wtYcRuAjsmxvfRw+kc1oAKfFc8YsXn3HZl
ZTdaN5Bj+Ra/hyZwoBmKjhT82Diw2UjNGO+pI9yrhISiolK0SQgw9V0boltdzcjv
YuSF16BUySENRG1pVnkiioL+Cn0xxvCC
-----END CERTIFICATE-----'
YGD_PAGE='https://mhguitarte.github.io/ygd-editor/'
YGD_TMP=

ygd_fail() {
  printf 'ygd-editor: %s\n' "$*" >&2
  exit 1
}

ygd_install() {
  # Test-only overrides: where the release is read from, where the app goes, not opening it, and a
  # certificate file to check SHA256SUMS.txt.sig against instead of YGD_CERT (tools/test-install.sh
  # signs its own checksums to reach the later checks). The code-signature pin has no override.
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

  # SHA256SUMS.txt gives the file name, the version and the hash, with no API rate limit. It comes from
  # the same server as the zip, so it counts only once its signature verifies against the project key:
  # a release without SHA256SUMS.txt.sig, or with one the key did not make, installs nothing.
  command -v openssl >/dev/null 2>&1 || ygd_fail "openssl, which checks the release's signature, was not found; nothing was installed"
  printf 'Looking for the latest ygd-editor for macOS (%s)…\n' "$arch"
  curl -fsSL "$releases/SHA256SUMS.txt" -o "$YGD_TMP/SHA256SUMS.txt" || ygd_fail "could not read $releases/SHA256SUMS.txt"
  curl -fsSL "$releases/SHA256SUMS.txt.sig" -o "$YGD_TMP/SHA256SUMS.txt.sig" || ygd_fail "could not read $releases/SHA256SUMS.txt.sig, the signature of the checksums; nothing was installed"
  if [ -n "${YGD_TEST_SIGNING_CERT:-}" ]; then
    cp "$YGD_TEST_SIGNING_CERT" "$YGD_TMP/release-signing.pem"
  else
    printf '%s\n' "$YGD_CERT" > "$YGD_TMP/release-signing.pem"
  fi
  openssl x509 -in "$YGD_TMP/release-signing.pem" -pubkey -noout > "$YGD_TMP/release-signing.pub" 2>/dev/null || ygd_fail "could not read the project certificate; nothing was installed"
  openssl dgst -sha256 -verify "$YGD_TMP/release-signing.pub" -signature "$YGD_TMP/SHA256SUMS.txt.sig" "$YGD_TMP/SHA256SUMS.txt" >/dev/null 2>&1 \
    || ygd_fail "the signature of SHA256SUMS.txt does not verify against the project certificate, so the checksums are not the project's; nothing was installed"
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
