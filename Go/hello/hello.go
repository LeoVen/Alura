/**
 * @file hello.go
 *
 * @author Leonardo Vencovsky (https://github.com/LeoVen)
 * @date 30/07/2018
 *
 * Hello World program
 */
package main

import (
	"fmt"
	"reflect"
)

func main() {

	var name1 string = "Allan Turing"
	var age1 int = 23
	var version1 float32 = 1.1

	// or the same can be made as

	name2 := "Allan Turing"
	age2 := 23
	version2 := 1.1

	fmt.Println("Hello World to", name1, version1, age1)

	fmt.Println("Types: ", reflect.TypeOf(name2), reflect.TypeOf(version2), reflect.TypeOf(age2))

}
