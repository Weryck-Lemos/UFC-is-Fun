#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int vet[n];
    for(int i=0; i<n; i++)scanf("%d", &vet[i]);

    printf("[ ");
    for(int i=0; i<n; i++)printf("%d ", vet[i]);
    printf("]\n");
}