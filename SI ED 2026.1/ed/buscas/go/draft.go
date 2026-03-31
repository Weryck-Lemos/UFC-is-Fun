package main

import ("fmt")

func matchingStrings(strings []string, queries []string) []int {

	frequencias := make(map[string]int)

	for _, s := range strings {
		frequencias[s]++
	}

	var resultados []int

	for _, q := range queries {
		resultados = append(resultados, frequencias[q])
	}

	return resultados
}

func main() {
	var tamanhoConsultas int
	if _, err := fmt.Scan(&tamanhoConsultas); err != nil {
		return
	}

	
	consultas := make([]string, tamanhoConsultas)
	for i := 0; i < tamanhoConsultas; i++ {
		fmt.Scan(&consultas[i])
	}


	var tamanhoBuscas int
	fmt.Scan(&tamanhoBuscas)


	buscas := make([]string, tamanhoBuscas)
	for i := 0; i < tamanhoBuscas; i++ {
		fmt.Scan(&buscas[i])
	}


	respostas := matchingStrings(buscas, consultas)

	for i, qtd := range respostas {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(qtd)
	}
	fmt.Println()
}
