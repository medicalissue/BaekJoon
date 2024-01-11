package main

import "fmt"

var depthList []int

func main() {
	var A, B int
	fmt.Scanln(&A, &B)
	backTrack(A, B, 0)
	smallest := -1
	for i := 0; i < len(depthList); i++ {
		if depthList[i] == -1 {
			continue
		} else if smallest == -1 {
			smallest = depthList[i]
		} else {
			smallest = min(smallest, depthList[i])
		}
	}
	fmt.Println(smallest)
}

func backTrack(a int, b int, depth int) {
	if a > b {
		depthList = append(depthList, -1)
	} else if a == b {
		depthList = append(depthList, depth+1)
	} else {
		backTrack(a*10+1, b, depth+1)
		backTrack(a*2, b, depth+1)
	}
}
