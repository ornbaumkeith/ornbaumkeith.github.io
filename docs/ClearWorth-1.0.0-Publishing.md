# ClearWorth Version 1.0.0 — Windows publishing guide

The portfolio identifies ClearWorth as Version 1.0.0. Website edits do not change the application package, generate an installer, sign an executable, or establish release acceptance. Link a public download only after the final artifact is available and checked.

## Prepare the application release

Use a separate application working copy. Confirm:
- package.json, both root package-lock.json version fields, the shipped browser companion and executable version metadata agree on 1.0.0.
- Update version-sensitive validation assertions and expected output filenames to 1.0.0 while retaining behavioral and financial checks.
- Align the Electron development dependency and packaging runtime; rebuild native dependencies against the chosen packaged runtime.
- Set build.nsis.artifactName to "ClearWorth Setup ${version}.exe" for a predictable installer filename.
- Refresh application README, release notes, software inventory, required notices, installed license texts and Help images.
- Complete Windows typecheck, smoke tests, financial reconciliation, clean-install, upgrade, account-isolation, backup/restore, visual and keyboard acceptance using the packaged app.
- Resolve strict production dependency-audit findings. Temporary UAT exceptions are not production approval.
- Verify distribution rights for the application, brand artwork and bundled third-party material. Keep customer data, backups, credentials and signing files out of public source and media.

The newer review package identifies the application manifest as 1.0.0. Confirm the complete source, lockfile, browser companion and final executable agree before publishing; a partial review package is not evidence of a built installer. Renaming an older executable is insufficient. No production certification is implied by the website.

## Validate and package on Windows

The project's stated release baseline is Node 24.21.x with npm 11.19.x. Use the final release validator after updating its version checks; no new validator is supplied by this website update.

Existing application scripts include:
~~~powershell
npm ci
npm run compliance:licenses:strict
npm run security:audit:strict
npm run security:signatures
npm run verify
npm run build
npm run security:sbom
npm run package:win
~~~
Check each command's exit code and stop on failure. Signing credentials must already be configured before packaging a production installer. Do not bypass failing security or license gates.

Expected artifacts after promotion:
- dist\ClearWorth Setup 1.0.0.exe
- dist\win-unpacked\ClearWorth.exe
- dist\ClearWorth-1.0.0-SBOM.cdx.json
- installation guide, release notes, checksum file and required notices
- optional sanitized source ZIP if source distribution is intended

Verify signatures and launch:
~~~powershell
Get-AuthenticodeSignature ".\dist\ClearWorth Setup 1.0.0.exe" | Format-List Status,StatusMessage,SignerCertificate
Get-AuthenticodeSignature ".\dist\win-unpacked\ClearWorth.exe" | Format-List Status,StatusMessage,SignerCertificate
& ".\dist\win-unpacked\ClearWorth.exe"
& ".\dist\ClearWorth Setup 1.0.0.exe"
# Alternative:
Start-Process -FilePath ".\dist\ClearWorth Setup 1.0.0.exe"
~~~
Both signatures should report Valid and the intended publisher. For source development, use npm run dev after dependency installation.

Hash the final signed installer:
~~~powershell
Get-FileHash -Algorithm SHA256 -LiteralPath ".\dist\ClearWorth Setup 1.0.0.exe" |
  ForEach-Object { "$($_.Hash.ToLower())  $([IO.Path]::GetFileName($_.Path))" } |
  Set-Content -Encoding ASCII ".\dist\SHA256SUMS.txt"
~~~
A checksum verifies matching bytes and does not replace publisher signing.

## Publish through GitHub Releases

Keep the portfolio repository for the website and use an application or downloads repository for release assets. For public downloads with private application source, use a public distribution repository containing documentation and notices. Automatically generated source archives do not contain the compiled installer unless intentionally included.

1. Open the release repository → Releases → Draft a new release.
2. Select tag v1.0.0 and the reviewed release commit.
3. Title: ClearWorth 1.0.0 — Windows.
4. Describe features, tested Windows editions and CPU architecture, installation and upgrade steps, backup guidance, known limitations, support route and licensing.
5. Attach the signed installer, SHA256SUMS.txt, SBOM, installation guide and notices. Add source only if intended.
6. Save a draft until checks are complete. Use pre-release if acceptance is unfinished.
7. When ready, publish, then test an anonymous download and clean Windows installation. Verify the downloaded signature and checksum.
8. Provide the actual public release URL before enabling a website download link.

Suggested product description:
"ClearWorth Version 1.0.0 brings configurable financial dashboards, Planning Studio, income and expense schedules, calendar workspaces, transaction imports, reports and local security controls into a Windows workspace. Actual, planned and projected values remain distinct. Projected savings allocations reduce future available cash without becoming ordinary ledger expenses. Optional integrations require configuration."

## Website media and validation

The page contains fourteen silent controlled walkthroughs and ten current screenshots, plus an expandable earlier-image archive. Captions describe the supplied recordings and note older menu locations. The clip supplied under a backup filename demonstrates Import/Sync and is labeled accordingly; the separate Backup/Restore screenshot illustrates backup settings. Public excerpts omit profile contact fields, populated user lists and OS save dialogs.

These images show the captured workspace and are not proof of final runtime correctness, installer signing, security certification or reconciliation. A visible application audit log is distinct from an independent security audit.

For more media, ZIP a dedicated desktop folder and attach it in chat. Do not share a local Windows path as if it were remotely accessible. Include feature names and suggested captions, and use data intended for public display.

## Official references

- https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases
- https://www.electron.build/docs/nsis/
