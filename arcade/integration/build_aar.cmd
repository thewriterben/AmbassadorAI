@echo off
rem ===================== Build the arcade v1 embed artefact =====================
rem
rem Regenerates the Flutter module from v1 and builds the AAR that the native
rem DGD app depends on. Run this whenever v1 changes.
rem
rem AAR rather than a source-included Gradle subproject, deliberately: only one
rem person on this project has the Flutter SDK. An AAR means the native app
rem builds on any machine and in CI with no Flutter installed at all, which is
rem the same reasoning as the .xcframework recommendation for iOS.
rem
rem DGD_APP_TAB=true is required, not optional. Arcade plan section 4.3 bars
rem prize-style celebration inside the DGD app, and that flag is what
rem suppresses the fireworks and the spoken winner line. Shipping the embed
rem without it puts a coin-shower in a finance app.
rem
rem JDK 21 is also required, and is the step this script was missing until
rem 2026-09-20. Flutter ignores JAVA_HOME and prefers Android Studio's bundled
rem JBR, which here is JDK 25; on 25 the plugins' Dokka javadoc tasks die and
rem the build fails with six identical JavaDocGenerationTask errors that say
rem nothing about Java versions. The setting is global to the Flutter install,
rem so it is put back afterwards whether the build succeeds or not.
setlocal
set PATH=C:\src\flutter\bin;%PATH%
set MODULE=C:\src\dgd_arcade_module
set NATIVE=C:\src\dgd-native\android
set JDK21=C:\Program Files\Microsoft\jdk-21.0.12.101-hotspot

if not exist "%JDK21%\bin\java.exe" (
  echo.
  echo JDK 21 not found at "%JDK21%".
  echo The AAR cannot be built on JDK 25 - see the note at the top of this file.
  echo Install it ^(winget install Microsoft.OpenJDK.21^) or edit JDK21 above.
  exit /b 1
)

echo ==================== 1. regenerate the module from v1 ====================
python "%~dp0sync_module.py"
if errorlevel 1 (echo SYNC FAILED & exit /b 1)

echo.
echo ==================== 2. point Flutter at JDK 21 ====================
call flutter config --jdk-dir="%JDK21%" >nul
call flutter doctor -v 2>&1 | findstr /C:"Java version"

echo.
echo ==================== 3. build the AAR ====================
cd /d %MODULE%
call flutter clean >nul 2>&1
call flutter pub get
call flutter build aar --no-debug --no-profile --dart-define=DGD_APP_TAB=true
set RC=%ERRORLEVEL%

rem Restore the default before anything else can fail. Leaving the override in
rem place would silently change every other Flutter build on this machine.
call flutter config --jdk-dir="" >nul
echo AAR EXIT %RC%

if not "%RC%"=="0" (endlocal & exit /b %RC%)

echo.
echo ==================== 4. what was produced ====================
dir /S /B "%MODULE%\build\host\outputs\repo\*.aar" 2>nul

echo.
echo ==================== 5. publish into the app's local repo ====================
rem The native app resolves the arcade from android/arcade-repo, a Maven
rem repository checked in beside it, so that the app builds with no Flutter
rem SDK present. Building the AAR without mirroring it there leaves the app
rem silently on the previous arcade - which is exactly what happened on
rem 2026-09-20, and is why this step is part of the script and not a habit.
robocopy "%MODULE%\build\host\outputs\repo" "%NATIVE%\arcade-repo" /MIR /NFL /NDL /NJH /NJS /NP
rem robocopy exit codes below 8 are success ("files copied", "extra files
rem removed"); 8 and above are real failures.
if %ERRORLEVEL% GEQ 8 (echo PUBLISH FAILED & endlocal & exit /b 1)
echo published to %NATIVE%\arcade-repo

endlocal & exit /b 0
