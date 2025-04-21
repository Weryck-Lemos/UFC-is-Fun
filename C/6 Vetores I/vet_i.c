#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int vet[n];
    for(int i=0; i<n; i++)scanf("%d", &vet[i]);
    for(int i=0; i<n; i++)printf("%d\n", vet[i]);
}