@echo off
set "JAVA_HOME=C:\Program Files\Android\Android Studio\jbr"
set "ANDROID_HOME=%LOCALAPPDATA%\Android\Sdk"
set "PATH=C:\src\flutter\bin;%JAVA_HOME%\bin;%PATH%"
cd /d C:\src\puzzle-app
echo START %date% %time% > C:\src\build.log
call flutter build apk --debug >> C:\src\build.log 2>&1
echo EXIT %errorlevel% >> C:\src\build.log
