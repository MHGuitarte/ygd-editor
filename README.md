# ygd-editor — downloads

Desktop app for managing git worktrees and the AI agent sessions running inside them, for macOS,
Windows and Linux.

**Download:** <https://mhguitarte.github.io/ygd-editor-releases/> · **All versions:** [Releases](../../releases)

This repository holds the installers, the update manifests the app reads, and the download page.
The source code is developed in a private repository; questions and bug reports are welcome in
[Issues](../../issues).

## Is my download genuine?

Two independent checks, neither of which needs you to trust a name:

1. **Provenance.** Every release carries `SHA256SUMS.txt` signed with [Sigstore](https://www.sigstore.dev/)
   by the project's release workflow itself:
   ```bash
   cosign verify-blob --bundle SHA256SUMS.txt.sigstore.json \
     --certificate-identity-regexp '^https://github.com/MHGuitarte/ygd-editor/\.github/workflows/release\.yml@refs/tags/v' \
     --certificate-oidc-issuer https://token.actions.githubusercontent.com SHA256SUMS.txt
   sha256sum --check --ignore-missing SHA256SUMS.txt      # shasum -a 256 -c on macOS
   ```
2. **Code signature.** The macOS app and the Windows installer are signed with the project's own
   certificate. Its SHA-256 fingerprint is
   `46:C5:62:27:2A:5C:22:9E:D7:85:E1:A3:0D:47:2A:A3:5B:CE:AC:F0:7D:E4:D8:A3:49:23:C9:7B:D3:74:C3:AB`
   (public key: [`release-signing.pem`](release-signing.pem)). A build signed with any other
   certificate is not ours, whatever name it shows.
   - macOS: `codesign --verify --deep --strict /Applications/ygd-editor.app && codesign -dvv /Applications/ygd-editor.app 2>&1 | grep Authority`
   - Windows (PowerShell): `(Get-AuthenticodeSignature .\ygd-editor-*-setup.exe).SignerCertificate.Thumbprint` → `79A40643BDFE500AB6730154B03B336C1809C57C`

The certificate is not issued by Apple or Microsoft, so the first launch shows their usual prompt
for software from an unidentified developer; the download page explains how to get past it.

## Updates

The app checks this repository shortly after launch and downloads new versions in the background;
Settings › Notifications offers "Restart to update", a manual check, and automatic installation.
