#include <stdio.h>
#define n 10

int main(){
    int vet[n];

    for(int i=0; i<n; i++)scanf("%d",&vet[i]);

    for(int i=0; i<n-1; i++){
        for(int j=0; j<n-i-1; j++){
            if(vet[j]>vet[j+1]){
                int temp = vet[j];
                vet[j] = vet[j+1];
                vet[j+1]=temp;
            }
        }
    }

    for(int i=0; i<n; i++)printf("%d ",vet[i]);
}