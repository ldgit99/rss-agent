param(
  [string]$TaskName = "ArxivDailyAgent",
  [string]$Time = "08:00"
)

$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$runner = Join-Path $projectRoot "scripts\\run_daily.ps1"

if (-not (Test-Path $runner)) {
  throw "Runner script not found: $runner"
}

$escapedRunner = $runner.Replace('"', '\"')
$command = "powershell.exe -NoProfile -ExecutionPolicy Bypass -File `"$escapedRunner`""

schtasks /Create `
  /TN $TaskName `
  /SC DAILY `
  /ST $Time `
  /TR $command `
  /F | Out-Null

Write-Host "Created/Updated scheduled task: $TaskName at $Time"
