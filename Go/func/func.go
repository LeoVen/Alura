/**
 * @file func.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 30/07/2018
 *
 * Functions in Go
 */
package main

import (
	"fmt"
	"os"
)

func main() {

	printMenu()

	choice := getChoice()

	switch choice {
	case 1:
		fmt.Println("Monitoring local asteroids...")
	case 2:
		fmt.Println("The asteroid impact crashed on earth on September 13th 2018")
	case 0:
		fmt.Println("Ready the engines for space travel")
		os.Exit(0)
	default:
		fmt.Println("Unknown command")
		os.Exit(-1)
	}

	fmt.Println("Two returns from a function:")

	div, remn := intDiv(5, 2)

	fmt.Println("The division of [5 by 2] has", div, "as a result and a remnant of", remn)

	// This is a blank identifier, when its result doesn't matter for you

	div, _ = intDiv(9, 4)

	fmt.Println("The division of [9 by 4] results in", div)

}

func printMenu() {

	fmt.Println("Menu Options")
	fmt.Println("1 - Begin monitoring")
	fmt.Println("2 - Show machine logs")
	fmt.Println("0 - Exit space-time continuum")

}

func getChoice() int {
	var c int

	fmt.Scan(&c)

	return c
}

func intDiv(a int, b int) (int, int) {

	return int(a / b), (a % b)
}
