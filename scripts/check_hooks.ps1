$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo

if (Get-Command python -ErrorAction SilentlyContinue) {
  $env:PYTHONPYCACHEPREFIX = $env:TEMP
  python -m py_compile "04_KITS/v0_minimal/.claude/hooks/prompt_guard.py" "04_KITS/v0_minimal/.claude/hooks/pretool_guard.py" "04_KITS/v0_minimal/.claude/hooks/stop_guard.py"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
  $env:PYTHONPYCACHEPREFIX = $env:TEMP
  py -m py_compile "04_KITS/v0_minimal/.claude/hooks/prompt_guard.py" "04_KITS/v0_minimal/.claude/hooks/pretool_guard.py" "04_KITS/v0_minimal/.claude/hooks/stop_guard.py"
} else {
  Write-Error "Python is unavailable."
}
