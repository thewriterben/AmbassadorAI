@echo off
rem ======================================================== v1 RELEASE build
rem Plain release APK, ship configuration: no DEV menu, no demo flag.
rem This is what the merge into the main DGD app is built from.
set SRC=C:\src\puzzle-app
set WANT=main
set LOG=C:\src\v1-rel.log

cd /d %SRC% || (echo Cannot find %SRC% & exit /b 1)
for /f %%b in ('git rev-parse --abbrev-ref HEAD') do set BRANCH=%%b
if not "%BRANCH%"=="%WANT%" (
  echo.
  echo   REFUSING TO BUILD: %SRC% is on branch "%BRANCH%", expected "%WANT%".
  echo   v1 must be built from main. See arcade\VERSIONS.md.
  echo.
  exit /b 1
)

set PATH=C:\src\flutter\bin;%PATH%
echo === v1 RELEASE BUILD === > %LOG%
call flutter analyze >> %LOG% 2>&1
call flutter test >> %LOG% 2>&1
call flutter build apk --release >> %LOG% 2>&1
echo EXIT %ERRORLEVEL% >> %LOG%
