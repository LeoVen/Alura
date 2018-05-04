# Calcula o hash de todos os arquivos passados pelo comando Get-ChildItem

$ErrorActionPreference = "Stop"

# A variável input representa o conteúdo que é passado pelo pipe-line

function Calculate-DirectoryHash($toFile) {

    if ($toFile -eq "help") {
        Write-Host "`nCalcula o hash de todos os arquivos passados pelo comando Get-ChildItem`n"
    }
    else {
        foreach ($file in $input) {

            $hash = Get-FileHash $file.fullName
    
            if ($toFile -eq $null) {
                Write-Host "$($file.fullName) >> $($hash.Hash)"
            }
            else {
                Write-Output "$($file.fullName) >> $($hash.Hash)" >> $toFile
            }

        }
    }

}