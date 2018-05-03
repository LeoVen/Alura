param($operacao)

if ($operacao -eq "Help") {

	echo "`n`nHelp Menu`n"
	echo "Available commands         Description"
	echo "------------------         -----------"
	echo "    help                   Shows this help menu"
	echo "    start                  Starts fluig services*"
	echo "    stop                   Stops fluig services*"
	echo "    restart                Restarts fluig services*"
	echo "------------------         -----------"
	echo "`n`n* Included services: fluig_Indexer, fluig_RealTime, fluig"
	
} elseif ($operacao -eq "Start") {

	echo "`n`n[ INFO ] Starting fluig services"
	
	$fluig_Indexer = Get-Service -Name fluig_Indexer
	$fluig_RealTime = Get-Service -Name fluig_RealTime
	$fluig = Get-Service -Name fluig
	
	$ok = 1;
	
	if ( $fluig_Indexer.Status -eq "Running" ) {
		
		echo "[ ERROR ] Service fluig_Indexer is already running"
		$ok = 0;
	}
	if ( $fluig_RealTime.Status -eq "Running" ) {
	
		echo "[ ERROR ] Service fluig_RealTime is already running"
		$ok = 0;
	}
	if ( $fluig.Status -eq "Running" ) {
	
		echo "[ ERROR ] Service fluig is already running"
		$ok = 0;
	}
	
	if ($ok -eq 1) {	
		
		echo "Starting fluig_Indexer"
		Start-Service fluig_Indexer
		
		echo "Starting fluig_RealTime"
		Start-Service fluig_RealTime
		
		echo "Starting fluig"
		Start-Service fluig
		
	}

} elseif ($operacao -eq "Stop") {

	echo "`n`n[ INFO ] Stopping fluig services"
	
	$fluig_Indexer = Get-Service -Name fluig_Indexer
	$fluig_RealTime = Get-Service -Name fluig_RealTime
	$fluig = Get-Service -Name fluig
	
	$ok = 1;
	
	if ( $fluig_Indexer.Status -eq "Stopped" ) {
		
		echo "[ ERROR ] Service fluig_Indexer is already running"
		$ok = 0;
	}
	if ( $fluig_RealTime.Status -eq "Stopped" ) {
	
		echo "[ ERROR ] Service fluig_RealTime is already running"
		$ok = 0;
	}
	if ( $fluig.Status -eq "Stopped" ) {
	
		echo "[ ERROR ] Service fluig is already running`n`n"
		$ok = 0;
	}
	
	if ($ok -eq 1) {
	
		echo "Stopping fluig"
		Stop-Service fluig
		
		echo "Stopping fluig_RealTime"
		Stop-Service fluig_RealTime
		
		echo "Stopping fluig_Indexer"
		Stop-Service fluig_Indexer
	}
		
} elseif ( $operacao -eq "Restart" ) {

	echo "`nRestarting fluig services"
	
	$fluig_Indexer = Get-Service -Name fluig_Indexer
	$fluig_RealTime = Get-Service -Name fluig_RealTime
	$fluig = Get-Service -Name fluig
	
	if ( $fluig.Status -eq "Running" ) {
	
		echo "Stopping fluig"
		Stop-Service fluig
	}
	if ( $fluig_RealTime.Status -eq "Running" ) {
	
		echo "Stopping fluig_RealTime"
		Stop-Service fluig_RealTime
	}
	if ( $fluig_Indexer.Status -eq "Running" ) {
		
		echo "Stopping fluig_Indexer"
		Stop-Service fluig_Indexer
	}
	
	echo "Starting fluig_Indexer"
	Start-Service fluig_Indexer
	
	echo "Starting fluig_RealTime"
	Start-Service fluig_RealTime
	
	echo "Starting fluig"
	Start-Service fluig

} else {

	echo "Invalid command"

}

echo "`n`n"