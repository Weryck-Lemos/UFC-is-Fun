#include <stdio.h>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);
    m--;

    int vet[n], vivos=n;
    for(int i=0; i<n; i++)vet[i]=1;

    while(vivos>1){
        int prox = (m+1)%n;
        while(vet[prox] == 0){
            prox=(prox+1)%n;
        }

        vet[prox]= 0;
        vivos--;

        m = (prox +1)%n;
        while(vet[m]== 0) m = (m+1)%n;
    }

    for(int i=0; i<n; i++){
        if(vet[i]){
            printf("%d\n", i+1);
            break;
        }
    }
}