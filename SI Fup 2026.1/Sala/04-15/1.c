#include <stdio.h>
#define n 5

int main(){
    int vet1[n], vet2[n], acc=0;

    for(int i=0; i<n; i++)scanf("%d", &vet1[i]);
    for(int i=0; i<n; i++)scanf("%d", &vet2[i]);
    for(int i=0; i<n; i++) acc+= (vet1[i]* vet2[i]);
    
    printf("%d\n", acc);
}