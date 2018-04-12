param($Search, $FileName)

$ErrorActionPreference = "Stop"

$nameExpr = @{
	Label = "File Name";
	Expression = { $_.Name }
}

$lengthExpr = @{
	Label = "File Length";
	Expression = { "{0:N2} KB" -f ( $_.Length / 1KB ) }
}

$query = @($nameExpr, $lengthExpr)

Get-ChildItem -Recurse -File |
	Where-Object Name -CLike *$Search* |
	Where-Object { $_.extension -eq ".c" } |
	Select-Object $query |
	Sort-Object -Property Length -Descending |
    ConvertTo-Json |
    Out-File ".\$FileName"
