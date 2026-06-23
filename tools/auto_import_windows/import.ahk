; AutoHotkey script: import.ahk
; Usage: import.ahk "C:\path\to\SKILL.md"
; Reads the file argument and pastes it into the currently focused control via clipboard + Ctrl+V
; This script is written for AutoHotkey v1.1 (legacy syntax) and avoids mixing expression and legacy expansion.

#NoTrayIcon
#SingleInstance, Force
SetTitleMatchMode, 2
SetKeyDelay, 50, 50

; Read first command-line parameter (legacy %1% expansion)
skillPath = %1%
if skillPath =
{
    MsgBox, 48, Error, No file path provided.`nUsage: import.ahk "C:\path\to\SKILL.md"
    ExitApp
}

; Verify file exists
if !FileExist(skillPath)
{
    MsgBox, 48, Error, File not found:`n%skillPath%
    ExitApp
}

; Read file into a variable
FileRead, fileContents, %skillPath%
if ErrorLevel
{
    MsgBox, 48, Error, Could not read file: %skillPath%
    ExitApp
}

; Show a short preview and confirm with the user before pasting
preview := SubStr(fileContents, 1, 400)
StringReplace, preview, preview, `r`n, `n, All
MsgBox, 4, Confirm paste, About to paste the contents of:`n%skillPath%`n`nPreview (first ~400 chars):`n`n%preview%`n`nProceed to paste into the currently focused input?`n(Click Yes to paste, No to cancel)
IfMsgBox, No
{
    MsgBox, 64, Cancelled, Paste cancelled by user.
    ExitApp
}

; Backup current clipboard
ClipSaved := ClipboardAll

; Put file contents on clipboard
clipboard := fileContents
ClipWait, 2
if ErrorLevel
{
    MsgBox, 48, Error, Clipboard did not become available
    ; Attempt to restore clipboard before exiting
    if (ClipSaved)
        Clipboard := ClipSaved
    ExitApp
}

; Small pause to ensure focus is stable
Sleep, 250

; Send paste (Ctrl+V)
Send, ^v

; Brief pause then restore original clipboard
Sleep, 300
if (ClipSaved)
    Clipboard := ClipSaved

ExitApp
