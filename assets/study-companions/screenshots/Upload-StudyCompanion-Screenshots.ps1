$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$Repo = 'ornbaumkeith/ornbaumkeith.github.io'
$Url = 'https://github.com/ornbaumkeith/ornbaumkeith.github.io.git'
$Names = @(
  'ArcGISProPro.png',
  'ArcGISEnterpriseAdminPro.png',
  'ArcGISEnterpriseGeoDataManagementPro.png',
  'ArcGISEnterpriseSystemDesignPro.png'
)
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
foreach ($name in $Names) {
  if (-not (Test-Path -LiteralPath (Join-Path $Root $name))) { throw "Missing original screenshot $name; extract the complete ZIP before running." }
}
if (-not (Get-Command 'git' -ErrorAction SilentlyContinue)) { throw 'Git is not available on PATH.' }
if (-not (Get-Command 'gh' -ErrorAction SilentlyContinue)) { throw 'GitHub CLI is not available on PATH.' }
& gh auth status
if ($LASTEXITCODE -ne 0) {
  Write-Host 'Authenticate with your browser using the code displayed by GitHub.'
  & gh auth login --hostname github.com --git-protocol https --web --clipboard
  if ($LASTEXITCODE -ne 0) { throw 'GitHub authentication failed.' }
}
& gh auth setup-git
if ($LASTEXITCODE -ne 0) { throw 'GitHub Git authentication setup failed.' }
$Temp = Join-Path $env:TEMP ("study-companions-screenshots-" + [guid]::NewGuid().ToString('N'))
try {
  & git clone --depth 1 --branch master $Url $Temp
  if ($LASTEXITCODE -ne 0) { throw 'Cloning portfolio repository failed.' }
  $Dest = Join-Path $Temp 'assets\study-companions\screenshots'
  New-Item -Path $Dest -ItemType Directory -Force | Out-Null
  foreach ($name in $Names) {
    $Source = Join-Path $Root $name
    $Target = Join-Path $Dest $name
    Copy-Item -LiteralPath $Source -Destination $Target -Force
    if ((Get-FileHash -Algorithm SHA256 -LiteralPath $Source).Hash -ne (Get-FileHash -Algorithm SHA256 -LiteralPath $Target).Hash) {
      throw "Screenshot hash mismatch: $name"
    }
  }
  Push-Location $Temp
  try {
    & git add -- assets/study-companions/screenshots
    if ($LASTEXITCODE -ne 0) { throw 'Git add failed.' }
    & git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
      Write-Host 'Screenshots are already identical; no new commit needed.'
    } else {
      & git -c user.name='Keith Ornbaum' -c user.email='66328923+ornbaumkeith@users.noreply.github.com' commit -m 'Add original Study Companions screenshots'
      if ($LASTEXITCODE -ne 0) { throw 'Git commit failed.' }
      & git push origin master
      if ($LASTEXITCODE -ne 0) { throw 'Git push failed. The remote may have changed; rerun this script to clone the latest version.' }
    }
  } finally { Pop-Location }
  Write-Host "`nOriginal screenshot upload completed." -ForegroundColor Green
  Write-Host 'Images directory: https://github.com/ornbaumkeith/ornbaumkeith.github.io/tree/master/assets/study-companions/screenshots'
  Write-Host 'Live page: https://ornbaumkeith.github.io/projects/study-companions/index.html'
  Start-Process 'https://ornbaumkeith.github.io/projects/study-companions/index.html'
} finally {
  if (Test-Path -LiteralPath $Temp) { Remove-Item -LiteralPath $Temp -Recurse -Force }
}
