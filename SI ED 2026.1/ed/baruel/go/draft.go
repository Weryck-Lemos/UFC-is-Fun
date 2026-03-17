package main

import "fmt"

func main() {
    var totalAlbum, totalPossui int
    fmt.Scan(&totalAlbum, &totalPossui)

    album := make([]int, totalAlbum+1)

    repetidas := ""
    ultimo := -1

    for i := 0; i < totalPossui; i++ {
        var fig int
        fmt.Scan(&fig)

        if fig == ultimo {
            repetidas += fmt.Sprintf("%d ", fig)
        }
        
        album[fig] = 1
        ultimo = fig
    }

    if repetidas == "" {
        fmt.Println("N")
    } else {
        fmt.Println(repetidas[:len(repetidas)-1])
    }

    faltando := ""
    for i := 1; i <= totalAlbum; i++ {
        if album[i] == 0 {
            faltando += fmt.Sprintf("%d ", i)
        }
    }

    if faltando == "" {
        fmt.Println("N")
    } else {
        fmt.Println(faltando[:len(faltando)-1])
    }
}