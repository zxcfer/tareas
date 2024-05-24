package main

import (
	"fmt"
)

func NonrepeatingCharacter(str string) string {

	charCount := make(map[rune]int)

	for _, char := range str {
		charCount[char]++
	}

	for _, char := range str {
		if charCount[char] == 1 {
			return string(char)
		}
	}

	return ""
}

func main() {
	fmt.Println(NonrepeatingCharacter("abcd"))
	fmt.Println(NonrepeatingCharacter("hello world hi hey"))

	// test cases
	fmt.Println(NonrepeatingCharacter("abcd"))
	fmt.Println(NonrepeatingCharacter("hello world hi hey"))
}
