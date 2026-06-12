$ErrorActionPreference = 'Stop'

$projectsRoot = 'C:\projects'
$oldPath = Join-Path $projectsRoot 'protected-agent-kit'
$newName = 'Agentum'
$newPath = Join-Path $projectsRoot $newName

Set-Location -LiteralPath $projectsRoot

if (-not (Test-Path -LiteralPath $oldPath)) {
    throw "Source path not found: $oldPath"
}

if (Test-Path -LiteralPath $newPath) {
    throw "Target path already exists: $newPath"
}

Rename-Item -LiteralPath $oldPath -NewName $newName

Write-Output "RENAMED_TO: $newPath"
