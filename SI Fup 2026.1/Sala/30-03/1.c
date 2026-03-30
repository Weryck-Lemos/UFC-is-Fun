#include <stdio.h>

int main(){
    int num1, num2;
    char op;

    scanf("%d %c %d", &num1, &op, &num2);

    switch(op){
        case '+':{
            printf("%d\n", num1+num2);
            break;
        }

        case '-':{
            printf("%d\n", num1-num2);
            break;
        }

        case '*':{
            printf("%d\n", num1*num2);
            break;
        }

        case '/':{
            if(!num2){
                printf("denominador inválido\n");
                return 0;
            }

            printf("%d\n", num1/num2);
            break;
        }
    }

    return 0;
}