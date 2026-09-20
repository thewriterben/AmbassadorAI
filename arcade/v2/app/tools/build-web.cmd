@echo off
set "PATH=C:\src\flutter\bin;%PATH%"
set "ProgramFiles(x86)=C:\Program Files (x86)"
cd /d C:\src\puzzle-app
echo START %date% %time% > C:\src\web.log
call flutter config --enable-web >> C:\src\web.log 2>&1
call flutter create . --platforms=web >> C:\src\web.log 2>&1
rem --no-web-resources-cdn: ship the renderer with the bundle so a WebView
rem with a strict allowlist (no gstatic.com) still loads.
call flutter build web --release --wasm --no-web-resources-cdn --base-href /arcade/ %* >> C:\src\web.log 2>&1
rem Debug symbol maps are never fetched by browsers; drop them (~6 MB).
rem Keep every renderer variant: the loader picks skwasm on wasm-gc browsers
rem and falls back to CanvasKit on older iOS WebViews.
del /q C:\src\puzzle-app\build\web\canvaskit\*.symbols C:\src\puzzle-app\build\web\canvaskit\chromium\*.symbols 2>nul
echo EXIT %errorlevel% >> C:\src\web.log
echo END %date% %time% >> C:\src\web.log
