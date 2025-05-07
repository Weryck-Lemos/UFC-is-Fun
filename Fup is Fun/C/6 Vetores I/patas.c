#include <stdio.h>
#include <stdlib.h>

int main(){
    int chico, cebolinha,n, tot=0;
    scanf("%d %d %d", &cebolinha, &chico, &n);

    char vet[n];
    for(int i=0; i<n; i++){
        scanf(" %c", &vet[i]);

        if(vet[i]=='c' || vet[i]=='v')tot+=4;
        else tot+=2;
    }

    printf("%d\n", tot);
    if(abs(tot-chico) > abs(tot-cebolinha)) printf("Chico Bento\n");
    else if(abs(tot-chico) < abs(tot-cebolinha)) printf("Cebolinha\n");
    else printf("empate\n");
}