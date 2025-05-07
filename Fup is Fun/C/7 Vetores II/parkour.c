#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, vet[50], ans=0;
    scanf("%d", &n);

    for(int i=0; i<n; i++)scanf("%d", &vet[i]);

    for(int i=0; i<n-1; i++){
        if(abs(vet[i]-vet[i+1])>=2)ans++;
    }

    printf("%d\n", ans);
}