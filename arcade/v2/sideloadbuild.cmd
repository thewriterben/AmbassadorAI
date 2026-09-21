@echo off
rem ======================================================= v2 SIDELOAD build
rem The ten-game catalogue with no backend behind it, for sideloading to a
rem phone. Debug-signed: fine for sideloading, rejected by Play.
rem
rem v2 has no Play build script on purpose. It is not a store candidate — v1
rem is. Add one here when v2 is actually going to a store track, and give it
rem a build number in the 200 band. See arcade\VERSIONS.md.
set SRC=C:\src\puzzle-app-v2
set WANT=v2/ten-games
set LOG=C:\src\v2-demo.log

cd /d %SRC% || (echo Cannot find %SRC% & exit /b 1)
for /f %%b in ('git rev-parse --abbrev-ref HEAD') do set BRANCH=%%b
if not "%BRANCH%"=="%WANT%" (
  echo.
  echo   REFUSING TO BUILD: %SRC% is on branch "%BRANCH%", expected "%WANT%".
  echo   v2 must be built from v2/ten-games. See arcade\VERSIONS.md.
  echo.
  exit /b 1
)

set PATH=C:\src\flutter\bin;%PATH%
echo === v2 DEMO BUILD === > %LOG%
call flutter analyze >> %LOG% 2>&1
call flutter test >> %LOG% 2>&1
call flutter build apk --release --dart-define=DGD_DEMO=true >> %LOG% 2>&1
echo EXIT %ERRORLEVEL% >> %LOG%
