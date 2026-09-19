@echo off
rem Test build: release-optimised (so memory is representative) with the DEV
rem menu compiled in. Never ship this APK.
cd /d C:\src\puzzle-app
set PATH=C:\src\flutter\bin;%PATH%
echo === DEV BUILD === > C:\src\rel.log
call flutter analyze >> C:\src\rel.log 2>&1
call flutter build apk --release --dart-define=DGD_DEV=true >> C:\src\rel.log 2>&1
echo EXIT %ERRORLEVEL% >> C:\src\rel.log
