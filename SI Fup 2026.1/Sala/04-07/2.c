#include <stdio.h>

int main(){
    int number, count = 0;
    scanf("%d", &number);

    if(number == 1){
        printf("não é primo\n");
        return 0;
    }

    for(int i=1; i<=number; i++){
        if(number%i == 0)count++;
    }

    if(count==2) printf("é primo\n");
    else printf("não é primo\n");
}