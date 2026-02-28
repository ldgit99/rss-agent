param(
  [Parameter(Mandatory = $true)]
  [ValidateSet("status", "run-once", "schedule-8am", "git-pull", "git-push")]
  [string]$Action
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -Path $repoRoot

function Get-PythonCommand {
  $candidates = @(
    ".venv\Scripts\python.exe",
    "C:\Users\user\AppData\Local\Python\bin\python.exe",
    "py",
    "python"
  )
  foreach ($candidate in $candidates) {
    if ($candidate -eq "py" -or $candidate -eq "python") {
      try {
        & $candidate --version | Out-Null
        return $candidate
      } catch {
        continue
      }
    } elseif (Test-Path $candidate) {
      return $candidate
    }
  }
  throw "Python executable not found."
}

switch ($Action) {
  "status" {
    $task = Get-ScheduledTask -TaskName "ArxivDailyAgent" -ErrorAction SilentlyContinue
    if ($task) {
      $info = Get-ScheduledTaskInfo -TaskName "ArxivDailyAgent"
      [PSCustomObject]@{
        TaskName = $task.TaskName
        State = $task.State
        LastRun = $info.LastRunTime
        LastResult = $info.LastTaskResult
        NextRun = $info.NextRunTime
      } | Format-List
    } else {
      "ArxivDailyAgent task is missing."
    }
  }
  "run-once" {
    $python = Get-PythonCommand
    & $python "src/arxiv_agent.py"
  }
  "schedule-8am" {
    $runner = Join-Path $repoRoot "scripts\run_daily.ps1"
    if (-not (Test-Path $runner)) { throw "Runner not found: $runner" }
    $actionObj = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$runner`""
    $trigger = New-ScheduledTaskTrigger -Daily -At 8:00AM
    $settings = New-ScheduledTaskSettingsSet -WakeToRun -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
    Register-ScheduledTask -TaskName "ArxivDailyAgent" -Action $actionObj -Trigger $trigger -Settings $settings -Force | Out-Null
    "ArxivDailyAgent updated to daily 08:00."
  }
  "git-pull" {
    git pull origin main
  }
  "git-push" {
    git push origin main
  }
}
