#include <stdio.h>

int main(){
    int n, vet[100], tot=0;
    scanf("%d", &n);
    
    for(int i=0; i<n; i++){
        scanf("%d", &vet[i]);
        tot += vet[i];
    }

    float ans = tot/n;
    printf("%.1f\n", ans);
}