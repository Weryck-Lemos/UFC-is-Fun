#include <stdio.h>

int main(){
    int n, vet[50];
    scanf("%d", &n);

    for(int i=0; i<n; i++)scanf("%d", &vet[i]);

    printf("[ ");
    for(int i=n-1; i>=0; i--)printf("%d ", vet[i]);
    printf("]\n");
}