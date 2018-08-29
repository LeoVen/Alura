# Função  para  a  criação  de  ApplicationPools
# chamados $ApplicationPoolName nos computadores
# listados em $ComputersName.
function Add-ApplicationPool {
    param(
        [String[]] $ComputersName,
        [String] $ApplicationPoolName
    )

    # Faremos este trabalho de forma paralela! Por isso, criamos várias sessões.
    $sessions = $ComputersName | ForEach-Object { New-PSSession -ComputerName $_ }

    # Faremos este trabalho de forma paralela! Por isso, criamos várias sessões.
    $jobs = $sessions | ForEach-Object {
        # A fim de termos  um  Job,  usamos  o  comando  Invoke-Command  com  o 
        # switchargument -AsJob!
        Invoke-Command -Session $_ -ScriptBlock {
            # Nós poderíamos escrever um ScriptBlock com a sintaxe de parâmetros
            # necessários, mas, podemos usar a variável automática $args também!
            "Estamos executando os comandos no computador: $env:COMPUTERNAME"
            $appCmdArgs = "add apppool /name:$($args[0]) /managedRuntimeVersion:v4.0 /managedPipelineMode:Integrated"
            C:\Windows\System32\inetsrv\appcmd.exe $appCmdArgs.Split(' ')
        } -ArgumentList $ApplicationPoolName -AsJob
    }

    # Aguardamos todos os Jobs serem finalizados para, então, termos seu valor.
    $jobs | Wait-Job | Select-Object @{Expression={ Receive-Job $_ };Label="Resultado"},"Name"

    # É importante removermos o Job da sessão do PowerShell...
    $jobs | Remove-Job

    # ... assim como as sessões também!
    $sessions | Remove-PSSession    
}