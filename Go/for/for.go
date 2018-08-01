/**
 * @file for.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 30/07/2018
 *
 * For loops and range
 */
package main

import (
	"fmt"
	"net/http"
	"time"
)

const totalMonitoring = 5
const delay = 5

func main() {

	// Slicer of strings
	var urls []string

	urls = append(urls, "https://random-status-code.herokuapp.com/")
	urls = append(urls, "https://www.alura.com.br")
	urls = append(urls, "https://www.caelum.com.br")
	urls = append(urls, "https://www.google.com.br")
	urls = append(urls, "https://random-status-code.herokuapp.com/")
	urls = append(urls, "https://random-status-code.herokuapp.com/")

	for i := 0; i < len(urls); i++ {
		fmt.Println(urls[i])
	}

	// Using range
	// The blank identifier is the index i, in this case not needed
	for _, url := range urls {
		fmt.Println(url)
	}

	for j := 0; j < totalMonitoring; j++ {

		for i, url := range urls {

			fmt.Println("Testing website", i, "of URL", url)
			testWebsite(url)

		}

		fmt.Println("Now waiting...\n")
		time.Sleep(delay * time.Second)
	}

}

func testWebsite(url string) {

	resp, _ := http.Get(url)

	if resp.StatusCode == 200 {
		fmt.Println("Success! The website[", url, "]was successfully loaded")
	} else {
		fmt.Println("Uh-Oh! Something happened with the website and returned a status code", resp.StatusCode)
	}

}
