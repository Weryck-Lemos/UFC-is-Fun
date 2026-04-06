#include <stdio.h>

int main(){
    int x,y, num=1, mdc;

    scanf("%d %d", &x, &y);

    while(num <= x && num <= y){
        if(x%num ==0 && y%num == 0)mdc = num;

        num++;
    }

    printf("MDC: %d\n", mdc);
    return 0;
}