@echo off
set "JAVA_HOME=C:\Program Files\Android\Android Studio\jbr"
set "ANDROID_HOME=%LOCALAPPDATA%\Android\Sdk"
set "ProgramFiles(x86)=C:\Program Files (x86)"
set "PATH=C:\src\flutter\bin;%JAVA_HOME%\bin;%ANDROID_HOME%\platform-tools;%PATH%"
cd /d C:\src\puzzle-app
echo === PUB > C:\src\check.log
call flutter pub get >> C:\src\check.log 2>&1
echo === ANALYZE >> C:\src\check.log
call flutter analyze >> C:\src\check.log 2>&1
echo === TEST >> C:\src\check.log
call flutter test >> C:\src\check.log 2>&1
echo === DONE >> C:\src\check.log
