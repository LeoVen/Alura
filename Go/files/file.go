/**
 * @file file.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 01/08/2018
 *
 * File handling
 */
package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {

	fmt.Println("Reading from a file")

	urls := readFile()

	fmt.Println(urls)

	for _, url := range urls {
		testWebsite(url)
	}

}

func readFile() []string {

	var urls []string

	file, err := os.Open("websites.txt") // This brings a pointer to a file
	//file, err := ioutil.ReadFile("websites.txt") // This brings an array of bytes

	if err != nil {
		fmt.Println(err)
		return nil
	}

	reader := bufio.NewReader(file)

	for {

		line, err := reader.ReadString('\n')

		line = strings.TrimSpace(line) // Removing \n

		urls = append(urls, line)

		if err == io.EOF {
			break
		}
	}

	file.Close()

	return urls
}

func testWebsite(url string) {

	resp, err := http.Get(url)

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(" ")

	fmt.Println("Website", url)

	if resp.StatusCode == 200 {
		fmt.Println("Success! Status code", resp.StatusCode)
		writeLog(url, true)
	} else {
		fmt.Println("Uh-Oh! Something went wrong and returned Status code", resp.StatusCode)
		writeLog(url, false)
	}

}

func writeLog(url string, isOnline bool) {

	file, err := os.OpenFile("log.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)

	if err != nil {
		fmt.Println(err)
	}

	file.WriteString(time.Now().Format("02/01/2006 15:04:05") + " - " + url + " - online: " + strconv.FormatBool(isOnline) + "\n")

	file.Close()

}
