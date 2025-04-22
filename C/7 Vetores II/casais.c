#include <stdio.h>

int main(){
    int n, vet[50], m=0, f=0;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%d", &vet[i]);

        if(vet[i]>0)m++;
        else f++;
    }

    if(m<f)printf("%d\n", m);
    else printf("%d\n", f);

}