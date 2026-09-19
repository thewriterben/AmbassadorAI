@echo off
cd /d C:\src\puzzle-app
set PATH=C:\src\flutter\bin;%PATH%
echo === RELEASE BUILD === > C:\src\rel.log
call flutter build apk --release >> C:\src\rel.log 2>&1
echo EXIT %ERRORLEVEL% >> C:\src\rel.log
