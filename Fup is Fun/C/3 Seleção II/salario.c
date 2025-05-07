#include <stdio.h>

int main(){
    float salario;
    scanf("%f", &salario);

    if(salario<=1000) salario *=1.2;
    else if(salario<=1500) salario *=1.15;
    else if(salario<=2000) salario *=1.1;
    else salario *=1.05;

    printf("%.2f\n", salario);
}