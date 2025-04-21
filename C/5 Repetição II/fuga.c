#include <stdio.h>

int main(){
    int h,p,f,d;
    scanf("%d %d %d %d",&h, &p, &f, &d);

    while(1){
        if(f==h){
            printf("S\n");
            break;
        }

        else if(f==p){
            printf("N\n");
            break;
        }

        f+=d;

        if(f<0)f=15;
        else if(f>15)f=0;
    }
}