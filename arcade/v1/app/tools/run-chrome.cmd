@echo off
set "PATH=C:\src\flutter\bin;%PATH%"
cd /d C:\src\puzzle-app
call flutter run -d chrome --release --web-port 5173
