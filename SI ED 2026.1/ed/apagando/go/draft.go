package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	filaInicial := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&filaInicial[i])
	}

	var m int
	fmt.Scan(&m)

	sairam := make(map[int]bool)
	for i := 0; i < m; i++ {
		var id int
		fmt.Scan(&id)
		sairam[id] = true
	}

	var filaFinal []int
	for _, id := range filaInicial {

		if !sairam[id] {
			filaFinal = append(filaFinal, id)
		}
	}

	for _, id := range filaFinal {

		fmt.Printf("%d ", id)
	}

	fmt.Println()
}
