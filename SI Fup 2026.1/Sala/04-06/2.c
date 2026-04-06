#include <stdio.h>

int main(){
    int number, count=2;
    scanf("%d", &number);

    while(count<=number){
        int  denominator =2, prim = 1;

        while(denominator <count){
            if(count%denominator == 0){
                prim = 0;
                break;
            }
            denominator++;
        }
        if(prim){
            printf("%d\n", count);
        }

        count++;
    }
    return 0;
}