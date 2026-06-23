# PowerShell wrapper to call AutoHotkey import script
param(
    [Parameter(Mandatory=$true)]
    [string]$SkillPath,
    [string]$AutoHotkeyExe = "C:\Program Files\AutoHotkey\AutoHotkey.exe",
    [string]$AhkScript = "$PSScriptRoot\import.ahk"
)

if (-not (Test-Path $SkillPath)) {
    Write-Error "Skill file not found: $SkillPath"
    exit 2
}

if (-not (Test-Path $AutoHotkeyExe)) {
    Write-Error "AutoHotkey executable not found at $AutoHotkeyExe. Please install AutoHotkey and set the path accordingly."
    exit 3
}

$escaped = $SkillPath -replace '"','\"'
& "$AutoHotkeyExe" "$AhkScript" "$escaped"

Write-Host "Ran AutoHotkey import helper for $SkillPath. If nothing was pasted, ensure the Cowork import text area is focused and try again."
