#include <stdio.h>

int main(){
    int x,n, tot=0, vet[50];
    scanf("%d %d", &x, &n);

    for(int i=0; i<n; i++){
        scanf(" %d", &vet[i]);
        if(vet[i]==x)tot++;
    }

    printf("%d\n", tot);
}