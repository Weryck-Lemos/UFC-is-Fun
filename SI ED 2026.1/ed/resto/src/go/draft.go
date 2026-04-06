package main

import "fmt"

func decompor(n int) {
	if n == 0 {
		return
	}

	resultado := n / 2
	resto := n % 2

	decompor(resultado)

	fmt.Printf("%d %d\n", resultado, resto)
}

func main() {
	var n int
	fmt.Scan(&n)
	if n > 0 {
		decompor(n)
	}
}
