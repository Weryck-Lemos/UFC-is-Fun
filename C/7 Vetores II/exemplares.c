#include <stdio.h>

int main(){
    int n, vet[50], id=0;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        int x;
        scanf("%d", &x);

        int existe=0;

        for(int j=0; j<id; j++){
            if(vet[j]==x){
                existe=1;
                break;
            }
        }

        if(!existe){
            vet[id]= x;
            id++;
        }
    }

    for(int i=0; i<id-1; i++){
        for(int j=0; j<id-i-1; j++){
            if(vet[j]> vet[j+1]){
                int temp= vet[j];
                vet[j] = vet[j+1];
                vet[j+1] = temp;
            }
        }
    }

    for(int i=0; i<id; i++){
        printf("%d", vet[i]);
        if(i< id-1)printf(" ");
    }
    printf("\n");
}