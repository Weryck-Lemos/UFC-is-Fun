#include <stdio.h>

int main(){
    int n, d1, d2;
    scanf("%d %d %d", &n, &d1, &d2);

    int d= d1+d2;
    if(d%2==0){
        if(n==0) printf("0\n");
        else printf("1\n");
    }

    else{
        if(n==0) printf("1\n");
        else printf("0\n");
    }
}