#include <stdio.h>

int main(){
    int n, vet[13];
    scanf("%d", &n);

    for(int i=0; i<n; i++) scanf("%d", &vet[i]);

    printf("[");
    for(int i=0; i<n; i++){
        if(vet[i]==1) printf("A");
        else if(vet[i]==11)printf("J");
        else if(vet[i]==12) printf("Q");
        else if(vet[i]==13) printf("K");
        else printf("%d", vet[i]);

        if(i<n-1)printf(", ");
    }
    printf("]\n");
}