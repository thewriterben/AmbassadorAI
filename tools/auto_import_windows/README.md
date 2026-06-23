# Windows Cowork Import helper (AutoHotkey + PowerShell)

This folder contains a minimal AutoHotkey script and a PowerShell wrapper to help paste a SKILL.md file into Claude Cowork's import text area on Windows 11.

Important notes before using
- This is a helper that automates keyboard input. It cannot reliably open or detect the Cowork import dialog for every Cowork version or user configuration.
- You must have AutoHotkey installed: https://www.autohotkey.com/
- For safety, open the Cowork Skill Import window first, focus the text area where the skill file contents should be pasted, then run the script.
- The script reads the SKILL.md file and places its contents onto the clipboard, then sends Ctrl+V to paste. Always review the clipboard contents before pasting.

Files:
- import.ahk — AutoHotkey script to paste a file into the focused window.
- run-import.ps1 — PowerShell wrapper to run import.ahk with a chosen SKILL.md path.

Usage (example):
1. Install AutoHotkey (https://www.autohotkey.com/) if you don't have it.
2. Open Claude Cowork and open the Import Skill dialog; click the import text area so it's focused.
3. From PowerShell run:
   .\run-import.ps1 -SkillPath 'C:\full\path\to\skills\dgd-video-studio\SKILL.md'
4. The script will copy the file contents to the clipboard and send a Ctrl+V to paste.

If you want a fully automated import (open app, navigate UI, click buttons), we can expand the AutoHotkey script, but I'll need details about your Cowork app paths and UI behavior.
