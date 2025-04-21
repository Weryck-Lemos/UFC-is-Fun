#include <stdio.h>

int main(){
    int a,b;
    scanf("%d %d", &a, &b);

    if(a>b) printf("invalido\n");
    else{
        int tot=0;
        for(int i=a; i<=b; i++){
            if(i%2==0 && i%3==0)tot+=i;
        }
        printf("%d\n", tot);
    }
}