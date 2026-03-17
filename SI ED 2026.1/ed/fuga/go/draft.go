package main

import "fmt"

func main() {
	var h, p, f, d int
	fmt.Scan(&h, &p, &f, &d)

	posicaoAtual := f

	for {
		posicaoAtual += d

		if posicaoAtual > 15 {
			posicaoAtual = 0
		} else if posicaoAtual<0{
			posicaoAtual = 15
		}

		if posicaoAtual == h {
			fmt.Println("S")
			break
		}
		if posicaoAtual == p {
			fmt.Println("N")
			break
		}
	}
}