//Devolver x^y

#include <stdio.h>

int main(){
    int x,y;
    unsigned long long ans=1;    // vai até 2^64 -1

    scanf("%d %d", &x, &y);
    for(int i=0; i<y; i++){
        ans *= x;
    }

    printf("%llu", ans);
}