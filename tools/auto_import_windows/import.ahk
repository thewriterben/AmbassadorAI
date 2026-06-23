; AutoHotkey script: import.ahk
; Usage: import.ahk "C:\path\to\SKILL.md"
; Reads the file argument and pastes it into the currently focused control via clipboard + Ctrl+V

#NoTrayIcon
#SingleInstance, Force
SetTitleMatchMode, 2
SetKeyDelay, 50, 50

; Get first command-line parameter
skillPath := %1%
if (!FileExist(skillPath))
{
    MsgBox, 48, Error, File not found:`n%skillPath%
    ExitApp
}

FileRead, fileContents, %skillPath%
if (ErrorLevel)
{
    MsgBox, 48, Error, Could not read file: %skillPath%
    ExitApp
}

; Place contents on clipboard
clipboard := fileContents
ClipWait, 2
if (ErrorLevel)
{
    MsgBox, 48, Error, Clipboard did not become available
    ExitApp
}

; Small pause
Sleep, 300

; Send paste (Ctrl+V)
Send, ^v

ExitApp
