package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N int
	fmt.Scanln(&N)

	i := 0
	for cnt := 0; cnt <= N; {
		if isReducing(i) {
			cnt++
		}
		i++
	}

	println(i - 1)
}

func isReducing(num int) bool {
	stringNum := strconv.Itoa(num)
	for i := 1; i < len(stringNum); i++ {
		if stringNum[i-1] <= stringNum[i] {
			return false
		}
	}
	return true
}
