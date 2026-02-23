$ErrorActionPreference = "Stop"
Set-Location -Path (Split-Path -Parent $PSScriptRoot)

if (Test-Path ".venv\\Scripts\\python.exe") {
  $python = ".venv\\Scripts\\python.exe"
} else {
  $python = "python"
}

& $python "src/arxiv_agent.py"
