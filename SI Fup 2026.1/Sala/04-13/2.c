//Devolver a raiz quadrada de N em int

#include <stdio.h>

int main(){
    int n, i=0;
    scanf("%d", &n);

    while((i+1)* (i+1) <= n){
        i++;
    }

    printf("%d", i);
}