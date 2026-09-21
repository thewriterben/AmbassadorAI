@echo off
rem ======================================================= v1 SIDELOAD build
rem Internal demo, sideloaded: Coin Quest only, no backend.
rem
rem DEV menu off. Tablet Run, the Daily Ledger and the standings bar are
rem hidden because they are server-authoritative.
rem
rem Still debug-signed — fine for sideloading, rejected by Play. The real
rem internal-testing build is demobuild.cmd, which needs the keystore and a
rem hosted backend. See arcade\RELEASE.md.
set SRC=C:\src\puzzle-app
set WANT=main
set LOG=C:\src\v1-demo.log

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
echo === v1 COIN QUEST DEMO === > %LOG%
call flutter analyze >> %LOG% 2>&1
call flutter test >> %LOG% 2>&1
call flutter build apk --release --dart-define=DGD_DEMO=true >> %LOG% 2>&1
echo EXIT %ERRORLEVEL% >> %LOG%
