@echo off
rem ====================================================== v1 PLAY TEST build
rem Tester build for Play internal testing.
rem
rem Differences from devbuild.cmd: no DGD_DEV, so the DEV menu is compiled out
rem entirely, and it produces an .aab rather than an .apk because Play requires
rem an App Bundle for new listings.
set SRC=C:\src\puzzle-app
set WANT=main
set LOG=C:\src\v1-play.log

cd /d %SRC% || (echo Cannot find %SRC% & exit /b 1)
for /f %%b in ('git rev-parse --abbrev-ref HEAD') do set BRANCH=%%b
if not "%BRANCH%"=="%WANT%" (
  echo.
  echo   REFUSING TO BUILD: %SRC% is on branch "%BRANCH%", expected "%WANT%".
  echo   v1 must be built from main. See arcade\VERSIONS.md.
  echo.
  exit /b 1
)

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

set PATH=C:\src\flutter\bin;%PATH%
echo === v1 PLAY BUILD === > %LOG%
echo ARCADE_API=%ARCADE_API% >> %LOG%
call flutter analyze >> %LOG% 2>&1
call flutter test >> %LOG% 2>&1
call flutter build appbundle --release --dart-define=ARCADE_API=%ARCADE_API% >> %LOG% 2>&1
echo EXIT %ERRORLEVEL% >> %LOG%
