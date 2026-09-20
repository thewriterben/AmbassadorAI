@echo off
rem ============================================================ v1 DEV build
rem Coin Quest only. Release-optimised so memory is representative, with the
rem DEV menu compiled in. Never ship this APK.
rem
rem This script builds v1 and ONLY v1. The branch guard below is not
rem ceremony: v1 is the merge candidate for the main DGD app and must not
rem silently acquire v2 code. If you want the ten-game catalogue, use
rem arcade\v2\devbuild.cmd, which builds a different folder entirely.
set SRC=C:\src\puzzle-app
set WANT=main
set LOG=C:\src\v1-dev.log

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
echo === v1 DEV BUILD === > %LOG%
call flutter analyze >> %LOG% 2>&1
call flutter test >> %LOG% 2>&1
call flutter build apk --release --dart-define=DGD_DEV=true >> %LOG% 2>&1
echo EXIT %ERRORLEVEL% >> %LOG%
