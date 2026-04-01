#include <stdio.h>

int main(){
    float notaf;
    scanf("%f", &notaf);

    int nota = (int)notaf;

    switch (nota)
    {
    case 9 ... 10:
        printf("excelente\n");
        break;
    
    case 7 ... 8:
        printf("bom\n");
        break;

    case 5 ... 6:
        printf("mediano\n");
        break;

    default:
        printf("reprovado\n");
        break;
    }
}