package main

import (
	"fmt"
	"strconv"
)

func main() {
	var A int
	var B string
	fmt.Scanln(&A)
	fmt.Scanln(&B)
	for i := 2; i >= 0; i-- {
		temp, _ := strconv.Atoi(string(B[i]))
		fmt.Println(A * temp)
	}
	temp, _ := strconv.Atoi(B)
	fmt.Println(A * temp)
}
