#include <stdio.h>

int main(){
    int n, cont = 0;
    float alt, tot=0;
    scanf("%d", &n);

    while(cont < n){
        scanf("%f", &alt);
        tot += alt;
        cont++;
    }

    printf("%f", tot/n);
}