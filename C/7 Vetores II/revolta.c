#include <stdio.h>

int main(){
    int n, vet[50], impar=0, par=0;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%d", &vet[i]);

        if(vet[i]%2 ==0)par+=vet[i];
        else impar+= vet[i];
    }

    if(impar>par)printf("soldados\n");
    else if(impar<par)printf("rebeldes\n");
    else printf("empate\n");
}