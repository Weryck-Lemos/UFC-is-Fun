package main
import "fmt"
func main() {
    var nome string
    var idade int

    fmt.Scan(&nome, &idade)
    fmt.Printf("%s eh ", nome)

    if(idade <12){
        fmt.Printf("crianca\n")
    } else if(idade<18){
        fmt.Printf("jovem\n")
    } else if(idade <65){
        fmt.Printf("adulto\n")
    } else if(idade <1000){
        fmt.Printf("idoso\n")
    } else{
        fmt.Printf("mumia\n")
    }
}
