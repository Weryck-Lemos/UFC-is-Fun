#include <stdio.h>

int main(){
    int p,s,e, tot=0;
    scanf("%d %d %d", &p, &s, &e);

    while(1){
        if(tot+s >= p){
            printf("%d saiu\n", tot);
            break;
        }

        printf("%d ", tot);
        
        tot+=s;
        printf("%d\n", tot);

        tot-=e;
    }
}