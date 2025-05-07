#include <stdio.h>

int main(){
    int vet[5], min=31;

    for(int i=0; i<5; i++){
        scanf("%d", &vet[i]);
        if(vet[i]<min)min=vet[i];
    }

    printf("%d\n", min);
}