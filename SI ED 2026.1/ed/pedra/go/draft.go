package main
import "fmt"
func main() {
    var id  int
    dist :=100
    ans:=-1
    fmt.Scan(&id)


    for i:=0; i<id; i++{
        var x, y int
        fmt.Scan(&x, &y)

        if (x>=10 && y>=10){
            dif := x-y
            if dif <0{
                dif*=-1
            }

            if dif<dist{
                ans=i
                dist = dif
            }
        }
    }
    if ans == -1{
        fmt.Printf("sem ganhador\n")
    }else{
        fmt.Printf("%d\n", ans)
    }
}
