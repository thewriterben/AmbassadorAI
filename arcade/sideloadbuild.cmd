@echo off
rem Internal demo, sideloaded: Coin Quest only, no backend.
rem
rem DEV menu off. Tablet Run, the Daily Ledger and the standings bar are hidden
rem because they are server-authoritative; Merge, Words, Blocks, Rope and the
rem three knowledge mini-games are hidden because they are at a rougher finish
rem than Coin Quest and would pull feedback off target.
rem
rem Still debug-signed — fine for sideloading, rejected by Play. The real
rem internal-testing build is demobuild.cmd, which needs the keystore and a
rem hosted backend. See arcade/RELEASE.md.
cd /d C:\src\puzzle-app
set PATH=C:\src\flutter\bin;%PATH%

echo === COIN QUEST DEMO === > C:\src\demo.log
call flutter analyze >> C:\src\demo.log 2>&1
call flutter test >> C:\src\demo.log 2>&1
call flutter build apk --release --dart-define=DGD_DEMO=true >> C:\src\demo.log 2>&1
echo EXIT %ERRORLEVEL% >> C:\src\demo.log
