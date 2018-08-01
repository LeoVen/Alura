/**
 * @file scan.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 30/07/2018
 *
 * User input
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
}

func printMenu() {

	fmt.Println("Menu Options")
	fmt.Println("1 - Begin monitoring")
	fmt.Println("2 - Show machine logs")
	fmt.Println("0 - Exit space-time continuum")

}
