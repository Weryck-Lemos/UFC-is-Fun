#include <stdio.h>

int main(){
    int number, count=2, ans=0;
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
            ans++;
            printf("%d\n", count);
        }

        count++;
    }

    printf("\ntotal de primos: %d\n", ans);
}