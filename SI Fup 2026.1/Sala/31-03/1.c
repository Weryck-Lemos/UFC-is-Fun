#include <stdio.h>

int main(){
    int contador = 1, n;
    scanf("%d", &n);

    while(contador<=n){
        printf("%d\n", contador);
        contador++;
    }
}