#include <stdio.h>

void imprime(int vet[], int n){
    printf("[");
    for(int i=0; i<n; i++){
        printf("%d", vet[i]);
        if(i<n-1)printf(", ");
    }
    printf("]\n");

}

int main(){
    int n;
    scanf("%d", &n);

    int vet[n];
    for(int i=0; i<n; i++)scanf("%d", &vet[i]);

    imprime(vet, n);
}