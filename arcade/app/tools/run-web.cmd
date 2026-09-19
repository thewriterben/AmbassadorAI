@echo off
set "PATH=C:\src\flutter\bin;%PATH%"
cd /d C:\src\puzzle-app
echo START > C:\src\web.log
call flutter run -d web-server --release --web-port 5173 --web-hostname 127.0.0.1 >> C:\src\web.log 2>&1
