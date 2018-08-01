/**
 * @file array.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 30/07/2018
 *
 * Arrays and Slices
 */
package main

import (
	"fmt"
	"reflect"
)

func main() {

	// Declaration of an array of integers
	//var varName [arraySize]type

	// Array of strings
	var urls [5]string

	urls[0] = "https://random-status-code.herokuapp.com/"
	urls[1] = "https://www.alura.com.br"
	urls[2] = "https://www.caelum.com.br"

	fmt.Println(urls)

	// Slices are not fixed sized arrays
	names := []string{"Alan Turing", "Bernhard Riemann"}

	fmt.Println(names)
	fmt.Println(names[0])

	fmt.Println("Types:", reflect.TypeOf(urls), reflect.TypeOf(names))
	fmt.Println("Sizes:", len(urls), len(names))

	// Adding more things to a Slice
	names = append(names, "Ada Lovelace")

	fmt.Println(names)

	// But a Slice also has a capacity:
	fmt.Println("Slice capacity:", cap(names))

	names = append(names, "Lorem Ispum")
	names = append(names, "Hello World")

	fmt.Println(names)

	fmt.Println("Slice new capacity:", cap(names))

}
