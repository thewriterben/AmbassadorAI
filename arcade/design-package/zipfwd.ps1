# Zip a folder with forward-slash entry names, so it unpacks correctly on a Mac too.
param([string]$Dir, [string]$Zip)
Add-Type -AssemblyName System.IO.Compression, System.IO.Compression.FileSystem
if (Test-Path $Zip) { Remove-Item $Zip }
$root = Split-Path $Dir -Parent
$fs = [IO.File]::Open($Zip, 'CreateNew')
$za = New-Object IO.Compression.ZipArchive($fs, [IO.Compression.ZipArchiveMode]::Create)
foreach ($f in Get-ChildItem $Dir -Recurse -File) {
  $name = $f.FullName.Substring($root.Length + 1).Replace('\', '/')
  $level = if ($f.Extension -in '.png', '.mp3') { [IO.Compression.CompressionLevel]::NoCompression } else { [IO.Compression.CompressionLevel]::Optimal }
  [IO.Compression.ZipFileExtensions]::CreateEntryFromFile($za, $f.FullName, $name, $level) | Out-Null
}
$za.Dispose(); $fs.Dispose()
