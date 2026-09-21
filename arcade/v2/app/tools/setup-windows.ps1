# One-shot Windows toolchain setup for Puzzle Pack.
# Run:  powershell -ExecutionPolicy Bypass -File tools\setup-windows.ps1
# Logs to C:\src\puzzle-setup.log
$ErrorActionPreference = 'Continue'
$log = 'C:\src\puzzle-setup.log'
function Log($m) { "$(Get-Date -Format HH:mm:ss) $m" | Tee-Object -FilePath $log -Append }
New-Item -ItemType Directory -Force C:\src | Out-Null
"" | Out-File $log

$flutter = 'C:\src\flutter'
$sdk = "$env:LOCALAPPDATA\Android\Sdk"
$env:ANDROID_HOME = $sdk
$env:Path = "$flutter\bin;$sdk\cmdline-tools\latest\bin;$sdk\platform-tools;$env:Path"

# JDK: use Android Studio's bundled one.
$jbr = 'C:\Program Files\Android\Android Studio\jbr'
if (Test-Path $jbr) { $env:JAVA_HOME = $jbr; $env:Path = "$jbr\bin;$env:Path"; Log "JAVA_HOME=$jbr" }

# Persist env for the user.
[Environment]::SetEnvironmentVariable('ANDROID_HOME', $sdk, 'User')
if (Test-Path $jbr) { [Environment]::SetEnvironmentVariable('JAVA_HOME', $jbr, 'User') }
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
foreach ($p in @("$flutter\bin", "$sdk\platform-tools", "$sdk\cmdline-tools\latest\bin")) {
  if ($userPath -notlike "*$p*") { $userPath += ";$p" }
}
[Environment]::SetEnvironmentVariable('Path', $userPath, 'User')
Log "PATH updated"

# 1. Flutter
if (-not (Test-Path "$flutter\bin\flutter.bat")) {
  Log "Cloning Flutter"
  git clone --depth 1 -b stable https://github.com/flutter/flutter.git $flutter 2>&1 | Out-Null
}
Remove-Item "$flutter\bin\cache\lockfile" -ErrorAction SilentlyContinue
Log "flutter --version"
& "$flutter\bin\flutter.bat" --version 2>&1 | Tee-Object -FilePath $log -Append
& "$flutter\bin\flutter.bat" config --no-analytics 2>&1 | Out-Null

# 2. Android cmdline-tools
if (-not (Test-Path "$sdk\cmdline-tools\latest\bin\sdkmanager.bat")) {
  Log "Downloading cmdline-tools"
  $zip = "$env:TEMP\cmdtools.zip"
  Invoke-WebRequest -Uri 'https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip' -OutFile $zip
  Remove-Item "$env:TEMP\cmdtools" -Recurse -Force -ErrorAction SilentlyContinue
  Expand-Archive -Force $zip "$env:TEMP\cmdtools"
  New-Item -ItemType Directory -Force "$sdk\cmdline-tools" | Out-Null
  Move-Item -Force "$env:TEMP\cmdtools\cmdline-tools" "$sdk\cmdline-tools\latest"
  Log "cmdline-tools installed"
}

# 3. SDK packages + licenses
Log "sdkmanager install"
$yes = "y`n" * 20
$yes | & "$sdk\cmdline-tools\latest\bin\sdkmanager.bat" --sdk_root="$sdk" --licenses 2>&1 | Out-Null
& "$sdk\cmdline-tools\latest\bin\sdkmanager.bat" --sdk_root="$sdk" "platform-tools" "platforms;android-35" "build-tools;35.0.0" 2>&1 | Select-String -NotMatch '^\[=' | Tee-Object -FilePath $log -Append

# 4. Flutter licenses + doctor
$yes | & "$flutter\bin\flutter.bat" doctor --android-licenses 2>&1 | Out-Null
Log "flutter doctor"
& "$flutter\bin\flutter.bat" doctor -v 2>&1 | Tee-Object -FilePath $log -Append

# 5. Project
$proj = 'C:\src\puzzle-app'
Set-Location $proj
if (-not (Test-Path "$proj\android")) {
  Log "flutter create"
  & "$flutter\bin\flutter.bat" create . --org com.puzzlepack --project-name puzzle_pack --platforms android,ios 2>&1 | Tee-Object -FilePath $log -Append
}
Log "pub get"
& "$flutter\bin\flutter.bat" pub get 2>&1 | Tee-Object -FilePath $log -Append
Log "analyze"
& "$flutter\bin\flutter.bat" analyze 2>&1 | Tee-Object -FilePath $log -Append
Log "build apk (debug)"
& "$flutter\bin\flutter.bat" build apk --debug 2>&1 | Tee-Object -FilePath $log -Append
Log "DONE"
