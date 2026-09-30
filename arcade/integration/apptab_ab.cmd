@echo off
rem Does --dart-define=DGD_APP_TAB=true actually reach the Dart compiler?
rem
rem Build the arcade AAR twice from identical source, changing only the define,
rem and compare the AOT snapshot. If the flag lands, libapp.so differs. If it
rem is being silently dropped, the two are byte-identical.
rem
rem Deliberate ordering: the flagless build runs FIRST and is never published.
rem The flagged build runs last and is the one left in arcade-repo. Ending with
rem a flagless arcade in the app's local repo would put fireworks back inside a
rem finance app.
setlocal
set PATH=C:\src\flutter\bin;%PATH%
set MODULE=C:\src\dgd_arcade_module
set JDK21=C:\Program Files\Microsoft\jdk-21.0.12.101-hotspot
set OUT=C:\src\apptab-ab
set AAR=%MODULE%\build\host\outputs\repo\co\digitalgold\arcade\module\flutter_release\1.0\flutter_release-1.0.aar

if exist "%OUT%" rmdir /S /Q "%OUT%"
mkdir "%OUT%"

call flutter config --jdk-dir="%JDK21%" >nul
cd /d %MODULE%

echo ==================== A: WITHOUT the flag ====================
call flutter clean >nul 2>&1
call flutter build aar --no-debug --no-profile > "%OUT%\build_off.log" 2>&1
if not exist "%AAR%" (echo BUILD A FAILED & call flutter config --jdk-dir="" >nul & exit /b 1)
copy /Y "%AAR%" "%OUT%\flag_off.aar" >nul
echo saved flag_off.aar

echo ==================== B: WITH the flag ====================
call flutter clean >nul 2>&1
call flutter build aar --no-debug --no-profile --dart-define=DGD_APP_TAB=true > "%OUT%\build_on.log" 2>&1
if not exist "%AAR%" (echo BUILD B FAILED & call flutter config --jdk-dir="" >nul & exit /b 1)
copy /Y "%AAR%" "%OUT%\flag_on.aar" >nul
echo saved flag_on.aar

call flutter config --jdk-dir="" >nul

echo ==================== restore: republish the FLAGGED build ====================
robocopy "%MODULE%\build\host\outputs\repo" "C:\src\dgd-native\android\arcade-repo" /MIR /NFL /NDL /NJH /NJS /NP >nul
if %ERRORLEVEL% GEQ 8 (echo PUBLISH FAILED & exit /b 1)
echo arcade-repo now holds the DGD_APP_TAB=true build
endlocal
