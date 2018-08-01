/**
 * @file switch.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 30/07/2018
 *
 * Switch statement in Go
 */
package main

import (
	"fmt"
)

func main() {

	printMenu()

	var choice int

	// Both are the same
	//fmt.Scanf("%d", &choice)
	fmt.Scan(&choice)

	fmt.Println("The value of my choice is", choice)
	fmt.Println("Its memory address is", &choice)

	switch choice {
	case 1:
		beginMonitoring()
		// break is not necessary
	case 2:
		showMachineLogs()
	case 0:
		exitSpaceTime()
	default:
		fmt.Println("Unknown command")
	}

}

func printMenu() {

	fmt.Println("Menu Options")
	fmt.Println("1 - Begin monitoring")
	fmt.Println("2 - Show machine logs")
	fmt.Println("0 - Exit space-time continuum")

}

func beginMonitoring() {
	fmt.Println("Monitoring local asteroids...")
	fmt.Println("Asteroid AL-D331 detected...")
	fmt.Println("...")
	fmt.Println("Tracing trajectory...")
	fmt.Println("Impact on earth is eminent !")
	fmt.Println("RUN FOR YOUR LIVES")
}

func showMachineLogs() {
	fmt.Println("The asteroid impact crashed on earth on September 13th 2018")
	fmt.Println("It killed billions of humans")
	fmt.Println("Only a small minority managed to survive")
	fmt.Println("And here we are, left out in this dying world")
}

func exitSpaceTime() {
	fmt.Println("Ready the engines for space travel")
	fmt.Println("Time to get out of here")
	fmt.Println("WUUUUSH")
	fmt.Println("We have entered light travel")
}
