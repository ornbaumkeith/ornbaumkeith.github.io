# ClearWorth 1.0.0 — Windows release publishing guide

Prepared 2026-10-19 from ClearWorth_Phase30_5_Rev10_Source.zip.
The attached source is 0.30.5, not a compiled or signed 1.0.0 installer.
This guide prepares publication; it does not publish an application release.

## 1. Findings to resolve before calling this 1.0.0
- package.json and both package-lock.json root version fields are 0.30.5; browser-companion/manifest.json is also 0.30.5.
- Validate_Phase30_5.ps1 and scripts/verify-phase305.mjs plus verify-phase305rev2.mjs through verify-phase305rev10.mjs explicitly assert 0.30.5. Update release-identity assertions and expected artifact names deliberately; retain the behavioral assertions. Do not globally replace historical phase references.
- package.json declares Electron 44.2.0 as a dev dependency but build.electronVersion requests 44.3.0. Select and test one runtime, update the lockfile consistently, and rebuild native dependencies against the packaged Electron runtime.
- The attached verification report records source checks only. Full dependency-backed typecheck, native smoke tests, Windows build, signed installer, financial integration and visual UAT remain pending.
- security/audit-baseline.json accepts temporary ExcelJS and UUID UAT risks until 2026-10-31. The strict production audit rejects moderate-or-higher runtime findings regardless of those exceptions. Re-run current audits; resolve findings rather than extending UAT exceptions as production approval.
- Review PHASE30_5_REV9_LICENSE_AUDIT.md and ASSET_PROVENANCE.md, generated installed-package license texts, packaged runtime notices, and rights to distributed artwork. These source reports explicitly leave clearance incomplete.
- Confirm actual/planned/projected reconciliation, goal funding, duplicate-import handling, corrections/void/restore, account isolation, clean installation, upgrade, backup/restore and uninstall using the packaged app. Confirm supported Windows editions and CPU architecture from tested machines before advertising them.

## 2. Prepare the release identity in a separate working copy
Use Node 24.21.x and npm 11.19.x, the project's stated release baseline.
After dependency/runtime alignment:
1. Run npm version 1.0.0 --no-git-tag-version in the app source root; verify package.json and both lockfile identities.
2. Update browser-companion/manifest.json to 1.0.0 if shipping it with the same release identity.
3. Update the validator and current version assertions listed above; create a clearly named 1.0.0 release validator and update any assertion referring to its path. Preserve all meaningful tests.
4. Explicitly set build.nsis.artifactName to "ClearWorth Setup ${version}.exe" for predictable installer naming.
5. Refresh README, release status, release notes, notices and Help captures. Preserve accurate historical records.
6. Tag the exact reviewed application source commit v1.0.0 only after release validation; a renamed 0.30.5 installer is not 1.0.0.

Current candidate validation command (valid for the UNMODIFIED 0.30.5 attachment only):
~~~powershell
Unblock-File .\Validate_Phase30_5.ps1; & .\Validate_Phase30_5.ps1 -StrictBuildBaseline -RequireCodeSigning
~~~
This requires configured signing credentials, valid final signatures, strict license collection and strict runtime auditing. It is expected to stop on unmet gates. It does not run the app or complete manual acceptance.
After promotion, use the updated 1.0.0 validator, not the unchanged phase validator.

## 3. Package and verify on Windows
The existing package scripts include npm run verify, npm run build, npm run security:sbom and npm run package:win.
Use the updated validator to orchestrate these with dependency installation, audits and signing checks. Do not publish by bypassing a failed check.
Keep signing certificates, tokens and passwords outside Git.
Expected release outputs after version promotion:
- dist\ClearWorth Setup 1.0.0.exe — signed Windows installer
- dist\win-unpacked\ClearWorth.exe — local packaged-app test target
- dist\ClearWorth-1.0.0-SBOM.cdx.json — component inventory
- release notes, installation instructions, third-party notices and license texts
- sanitized source ZIP only if intentionally distributing source

Verify and test:
~~~powershell
Get-AuthenticodeSignature ".\dist\ClearWorth Setup 1.0.0.exe" | Format-List Status,StatusMessage,SignerCertificate
Get-AuthenticodeSignature ".\dist\win-unpacked\ClearWorth.exe" | Format-List Status,StatusMessage,SignerCertificate
& ".\dist\win-unpacked\ClearWorth.exe"
& ".\dist\ClearWorth Setup 1.0.0.exe"
# Alternative installer launch:
Start-Process -FilePath ".\dist\ClearWorth Setup 1.0.0.exe"
~~~
Both signatures should report Valid and the intended publisher. Capture Windows UAT results.
Hash the final signed artifact, after all signing changes:
~~~powershell
Get-FileHash -Algorithm SHA256 -LiteralPath ".\dist\ClearWorth Setup 1.0.0.exe" |
  ForEach-Object { "$($_.Hash.ToLower())  $([IO.Path]::GetFileName($_.Path))" } |
  Set-Content -Encoding ASCII ".\dist\SHA256SUMS.txt"
~~~
A hash verifies matching bytes; it does not replace publisher signing.
For source development: npm run dev from the extracted source root after dependencies are installed.

## 4. Choose the GitHub repository
Recommended new application repository: ornbaumkeith/ClearWorth (proposed name; not created or verified here).
Keep ornbaumkeith.github.io for the portfolio. Store installer binaries as GitHub Release assets, not as files in the website Git history.
- Public application source: publish a sanitized, reviewed source tree and its intended license.
- Downloads only: use a public distribution repository with README, release notes and notices; keep development source private.
A private repository's release assets are not anonymous public downloads.
Do not upload live databases, backups, account exports, credentials, signing files or screenshots showing private financial information. Review tracked files as well as .gitignore; ignoring a file does not remove an existing tracked copy.
GitHub's automatically generated source archives contain the release repository, not the compiled installer.

## 5. Create the release in GitHub
1. Open the chosen repository → Releases → Draft a new release.
2. Choose tag v1.0.0 and the exact reviewed application release commit (or distribution commit for a downloads-only repository; record the private source commit internally).
3. Title: ClearWorth 1.0.0 — Windows.
4. Paste reviewed release notes, known limitations, tested Windows/architecture details, install/upgrade/backup guidance, support route and license information.
5. Attach the signed installer, SHA256SUMS.txt, SBOM, installation guide and notices; optionally attach a sanitized source ZIP.
6. Save as draft while verifying every asset and its checksum. Use pre-release if Windows acceptance is unfinished. Publish as a stable latest release only when ready.
7. Test an anonymous download and a clean Windows install using the downloaded file. Compare SHA-256 and Authenticode against the release.
8. Send the actual published release URL so the portfolio can link the verified installer. No speculative download URL is live on the site.

Proposed release notes to review after validation:
"ClearWorth 1.0.0 brings income, expenses, budgets, configurable financial dashboards, Planning Studio, calendar workspaces, transaction imports and reporting into a local-first Windows application. Planning keeps actual records, planned schedules and projected scenarios distinct. Savings goal allocations reduce projected available cash without becoming ordinary ledger expenses. Transactions & Expense Tracking is available under Import. Optional integrations require configuration."
Add the actual tested platforms, installer filename, known limitations and support details. Do not claim a security certification or complete offline operation for optional integrations.

## 6. Share website media from your desktop
This chat cannot open C:\Users\... or a Windows network share by path.
Create a dedicated ClearWorth-Website-Media folder containing only intended website material:
- screenshots: dashboard, Planning Studio, Budget, Calendar, Import, Settings, light/dark views
- videos: short focused demonstrations
- media-notes.txt: filename, page/feature, suggested caption, theme and app version; identify any example values
Use synthetic financial records and remove visible private information before sharing.
Right-click the folder → Compress to ZIP (Windows 11) or Send to → Compressed (zipped) folder (Windows 10), then attach the ZIP here. Split into smaller ZIPs if the interface rejects the size.
PowerShell alternative for a modest folder:
~~~powershell
$mediaFolder = Join-Path ([Environment]::GetFolderPath('Desktop')) 'ClearWorth-Website-Media'
$mediaZip = Join-Path ([Environment]::GetFolderPath('Desktop')) 'ClearWorth-Website-Media.zip'
Compress-Archive -Path $mediaFolder -DestinationPath $mediaZip
~~~
If you prefer cloud sharing, connect the storage provider and share the dedicated folder through that connected service; do not make personal desktop folders public. ZIP upload is the simplest route available now.
Videos and images have not yet been supplied for this update. Existing site captures are labeled earlier development screenshots.

## References
- GitHub release publishing: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- GitHub release links: https://docs.github.com/en/repositories/releasing-projects-on-github/linking-to-releases
- electron-builder NSIS artifact naming: https://www.electron.build/docs/nsis/
