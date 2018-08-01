/**
 * @file web.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 30/07/2018
 *
 * Working with net/http
 */
package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {

	fmt.Println("HTTP Get")

	var choice int

	// This works like while
	for {
		printMenu()

		choice = getChoice()

		if choice == 5 {
			break
		}

		switch choice {
		case 1:
			fmt.Println("Monitoring local asteroids...")
			webGet()
		case 2:
			fmt.Println("The asteroid impact crashed on earth on September 13th 2018")
		case 0:
			fmt.Println("Ready the engines for space travel")
			os.Exit(0)
		default:
			fmt.Println("Unknown command")
			os.Exit(-1)
		}
	}

}

func getChoice() int {
	var c int

	fmt.Scan(&c)

	return c
}

func webGet() {

	url := "https://www.alura.com.br"
	resp, _ := http.Get(url)

	if resp.StatusCode == 200 {
		fmt.Println("Success! The website", url, "was successfully loaded")
	} else {
		fmt.Println("Uh-Oh! Something happened with the website and returned a status code", resp.StatusCode)
	}

}

func printMenu() {

	fmt.Println("Menu Options")
	fmt.Println("1 - Begin monitoring")
	fmt.Println("2 - Show machine logs")
	fmt.Println("0 - Exit space-time continuum")

}
