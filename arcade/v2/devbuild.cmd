@echo off
rem ============================================================ v2 DEV build
rem The ten-game catalogue: Coin Quest plus Passage, with more to come.
rem Release-optimised with the DEV menu compiled in. Never ship this APK.
rem
rem Builds C:\src\puzzle-app-v2, which is a git worktree on v2/ten-games.
rem It is a different folder from v1's, so this cannot touch the merge
rem candidate even if it is run by mistake. The branch guard is the second
rem line of defence. See arcade\VERSIONS.md.
set SRC=C:\src\puzzle-app-v2
set WANT=v2/ten-games
set LOG=C:\src\v2-dev.log

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
echo === v2 DEV BUILD === > %LOG%
call flutter analyze >> %LOG% 2>&1
call flutter test >> %LOG% 2>&1
call flutter build apk --release --dart-define=DGD_DEV=true >> %LOG% 2>&1
echo EXIT %ERRORLEVEL% >> %LOG%
