@echo off
rem Tester build for Play internal testing.
rem
rem Differences from devbuild.cmd: no DGD_DEV, so the DEV menu is compiled out
rem entirely, and it produces an .aab rather than an .apk because Play requires
rem an App Bundle for new listings.
cd /d C:\src\puzzle-app
set PATH=C:\src\flutter\bin;%PATH%

if "%ARCADE_API%"=="" (
  echo.
  echo   ERROR: ARCADE_API is not set.
  echo.
  echo   Testers' phones cannot reach your PC, so a build without this points
  echo   at localhost and every server-backed game fails for them. Set it to
  echo   the hosted backend first:
  echo.
  echo     set ARCADE_API=https://arcade.digitalgold.co
  echo.
  exit /b 1
)

echo === DEMO BUILD === > C:\src\demo.log
echo ARCADE_API=%ARCADE_API% >> C:\src\demo.log
call flutter analyze >> C:\src\demo.log 2>&1
call flutter test >> C:\src\demo.log 2>&1
call flutter build appbundle --release --dart-define=ARCADE_API=%ARCADE_API% >> C:\src\demo.log 2>&1
echo EXIT %ERRORLEVEL% >> C:\src\demo.log
