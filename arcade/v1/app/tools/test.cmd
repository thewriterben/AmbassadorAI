@echo off
set "PATH=C:\src\flutter\bin;%PATH%"
cd /d C:\src\puzzle-app
call flutter test > C:\src\test.log 2>&1
