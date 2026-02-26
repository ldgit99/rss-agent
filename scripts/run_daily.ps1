$ErrorActionPreference = "Stop"
Set-Location -Path (Split-Path -Parent $PSScriptRoot)

$pythonCandidates = @(
  ".venv\\Scripts\\python.exe",
  "C:\\Users\\user\\AppData\\Local\\Python\\bin\\python.exe",
  "py",
  "python"
)

$python = $null
foreach ($candidate in $pythonCandidates) {
  if ($candidate -eq "py" -or $candidate -eq "python") {
    try {
      & $candidate --version | Out-Null
      $python = $candidate
      break
    } catch {
      continue
    }
  } elseif (Test-Path $candidate) {
    $python = $candidate
    break
  }
}

if (-not $python) {
  throw "Python executable not found."
}

& $python "src/arxiv_agent.py"
