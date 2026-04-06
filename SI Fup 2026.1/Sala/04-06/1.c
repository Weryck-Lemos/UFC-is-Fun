#include <stdio.h>

int main(){
    int number, denominator=2;
    scanf("%d", &number);

    while(denominator <number){
        if(number%denominator == 0){
            printf("Não é primo\n");
            return 0;
        }
        denominator++;
    }

    printf("É primo\n");
    return 0;
}