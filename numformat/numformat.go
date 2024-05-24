package main

import (
	"fmt"
	"strconv"
	"strings"
)

// hello world
func main() {
	fmt.Println("Hello, World!")
	string := "12,312.00"

	// split the string in the point
	splitString := strings.Split(string, ".")

	// check if second part is integer
	if _, err := strconv.ParseInt(splitString[1], 10, 64); err == nil {
		leftParts := strings.Split(splitString[0], ",")

		// check if all parts have 3 digits or less
		for _, part := range leftParts {
			if len(part) > 3 {
				fmt.Println("Part has more than 3 digits")
				return
			}
		}

		fmt.Println("Second part is numerical")
	} else {
		fmt.Println("Second part is not numerical")
	}

}
