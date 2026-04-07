#include <stdio.h>

int main(){
    int x,y, mdc=1;

    scanf("%d %d", &x, &y);

    while(y!=0){
        mdc = x%y;
        x = y;
        y = mdc;
    }
    printf("%d\n", x);
}