# Directory Hash

param($path)

$ErrorActionPreference = "Stop"

$dir = Get-ChildItem -Path $path -File -Recurse

foreach ($file in $dir.FullName) {

    $hash = Get-FileHash -Algorithm SHA1 $file | Select-Object -Property Hash

    Write-Output "The file << $file >> has a Hash of << $($hash.Hash) >>" >> dirHash.txt

}