package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func getMen(vet []int) []int {
	var res []int
	for _, v := range vet {
		if v > 0 {
			res = append(res, v)
		}
	}
	return res
}

func getCalmWomen(vet []int) []int {
	var res []int
	for _, v := range vet {
		if v < 0 && v > -10 {
			res = append(res, v)
		}
	}
	return res
}

func sortVet(vet []int) []int {
	res := make([]int, len(vet))
	copy(res, vet)
	sort.Ints(res)
	return res
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func sortStress(vet []int) []int {
	res := make([]int, len(vet))
	copy(res, vet)

	sort.SliceStable(res, func(i, j int) bool {
		return abs(res[i]) < abs(res[j])
	})
	return res
}

func reverse(vet []int) []int {
	res := make([]int, len(vet))
	n := len(vet)
	for i := 0; i < n; i++ {
		res[i] = vet[n-1-i]
	}
	return res
}

func unique(vet []int) []int {
	var res []int
	seen := make(map[int]bool)

	for _, v := range vet {
		if !seen[v] {
			seen[v] = true
			res = append(res, v)
		}
	}
	return res
}
func repeated(vet []int) []int {
	var res []int
	seen := make(map[int]bool)

	for _, v := range vet {
		if seen[v] {
			res = append(res, v)
		} else {
			seen[v] = true
		}
	}
	return res
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for {
		if !scanner.Scan() {
			break
		}
		fmt.Print("$")
		line := scanner.Text()
		args := strings.Split(line, " ")
		fmt.Println(line)

		switch args[0] {
		case "get_men":
			printVec(getMen(str2vet(args[1])))
		case "get_calm_women":
			printVec(getCalmWomen(str2vet(args[1])))
		case "sort":
			printVec(sortVet(str2vet(args[1])))
		case "sort_stress":
			printVec(sortStress(str2vet(args[1])))
		case "reverse":
			array := str2vet(args[1])
			other := reverse(array)
			printVec(array)
			printVec(other)
		case "unique":
			printVec(unique(str2vet(args[1])))
		case "repeated":
			printVec(repeated(str2vet(args[1])))
		case "end":
			return
		}
	}
}

func printVec(vet []int) {
	fmt.Print("[")
	for i, val := range vet {
		if i > 0 {
			fmt.Print(", ")
		}
		fmt.Print(val)
	}
	fmt.Println("]")
}

func str2vet(s string) []int {
	if s == "[]" {
		return nil
	}
	s = s[1 : len(s)-1]
	parts := strings.Split(s, ",")
	var vet []int
	for _, part := range parts {
		n, _ := strconv.Atoi(part)
		vet = append(vet, n)
	}
	return vet
}
