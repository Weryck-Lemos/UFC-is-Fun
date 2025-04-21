#include <stdio.h>

int main(){
    int n;
    char pe;
    scanf("%d %c", &n, &pe);

    printf("[ ");
    for(int i=0; i<10; i++){
        if(i != n){
            printf("%d%c ", i, pe);
        
            if(pe=='d') pe='e';
            else pe='d';
        }
    }

    if(n!=10)printf("ceu ");
    printf("]\n");
}