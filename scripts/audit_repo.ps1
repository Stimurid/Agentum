$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo

Write-Output "STATUS"
git status --short

Write-Output "PLACEHOLDERS"
Select-String -Path (Get-ChildItem -Recurse -File | Select-Object -ExpandProperty FullName) -Pattern "TODO","TBD","placeholder","PLACEHOLDER","stub","fill later","to be written","not yet implemented"

Write-Output "BACKUP_TEMP"
Get-ChildItem -Recurse -File | Where-Object { $_.Name -match "\.bak$|\.tmp$|~$" } | Select-Object FullName

Write-Output "HOOKS"
if (Get-Command python -ErrorAction SilentlyContinue) {
  $env:PYTHONPYCACHEPREFIX = $env:TEMP
  python -m py_compile "04_KITS/v0_minimal/.claude/hooks/prompt_guard.py" "04_KITS/v0_minimal/.claude/hooks/pretool_guard.py" "04_KITS/v0_minimal/.claude/hooks/stop_guard.py"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
  $env:PYTHONPYCACHEPREFIX = $env:TEMP
  py -m py_compile "04_KITS/v0_minimal/.claude/hooks/prompt_guard.py" "04_KITS/v0_minimal/.claude/hooks/pretool_guard.py" "04_KITS/v0_minimal/.claude/hooks/stop_guard.py"
} else {
  Write-Output "python_unavailable"
}

Write-Output "COUNTS"
"v0_minimal=$((Get-ChildItem '04_KITS/v0_minimal' -Recurse -File).Count)"
"persona_fragments=$((Get-ChildItem '04_KITS/persona_fragments' -File).Count)"
"test_prompts=$((Get-ChildItem '06_EVALS/TEST_PROMPTS' -File).Count)"
"profiles=$((Get-ChildItem '05_PROFILES' -Recurse -File).Count)"
