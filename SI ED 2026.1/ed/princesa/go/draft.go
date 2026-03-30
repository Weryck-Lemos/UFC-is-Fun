package main

import "fmt"

func imprimirEstado(vivos []int, pos int) {
	fmt.Print("[ ")
	for i, pessoa := range vivos {
		if i == pos {
			fmt.Printf("%d> ", pessoa)
		} else {
			fmt.Printf("%d ", pessoa)
		}
	}
	fmt.Println("]")
}

func main() {
	var n, e int

	fmt.Scan(&n, &e)

	vivos := make([]int, n)
	for i := 0; i < n; i++ {
		vivos[i] = i + 1
	}

	pos := 0
	for i, pessoa := range vivos {
		if pessoa == e {
			pos = i
			break
		}
	}

	for {
		imprimirEstado(vivos, pos)

		if len(vivos) == 1 {
			break
		}
		killPos := (pos + 1) % len(vivos)

		// pegando tudo antes de killPos e juntando com tudo depois
		vivos = append(vivos[:killPos], vivos[killPos+1:]...)

		pos = killPos % len(vivos)
	}
}
