package main

import (
	"fmt"
	"math/big"
)

func findDigitSum(num *big.Int) int {
	var x string = num.String()

	// iterate over string and add each digit to sum
	var sum int = 0
	for i := 0; i < len(x); i++ {
		sum += int(x[i] - '0')
	}
	return sum
}

func main() {
	var i, e = big.NewInt(2), big.NewInt(2000)
	var x = i.Exp(i, e, nil)

	// fmt.Println(x)
	fmt.Println(findDigitSum(x))
}
