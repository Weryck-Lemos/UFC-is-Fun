#include <stdio.h>

int main(){
    int n1,n2,n3, maior, menorA,menorB;
    scanf("%d %d %d", &n1, &n2, &n3);

    if((n1>n2) && (n1>n3)){
        maior=n1, menorA=n2, menorB=n3;
    }
    else if((n2>n1) && (n2>n3)){
        maior = n2, menorA=n1, menorB = n3;
    } 
    else{
        maior = n3, menorA = n1, menorB =n2;
    }

    if(maior < (menorA + menorB)) printf("True\n");
    else printf("False\n");
}