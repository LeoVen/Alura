# Directory Hash

$ErrorActionPreference = "Stop"

Get-DirectoryHash 

function Get-DirectoryHash() {

    $dir = Get-ChildItem -Recurse -File

    $output = New-Object System.Text.StringBuilder

    foreach ($file in $dir) {
        
        $hash = Get-FileHash -Algorithm SHA1 $file

        $output.Append($hash.Name) > $null
        $output.Append($hash) > $null

    }

}