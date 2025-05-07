#include <stdio.h>

int main(){
    int n, vet[51]={0}, max=0;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        int x;
        scanf("%d", &x);

        vet[x]++;
        if(vet[x]>max)max=vet[x];
    }

    printf("[ ");
    for(int i=0; i<51; i++){
        if(max==vet[i])printf("%d ", i);
    }
    printf("]\n");
}