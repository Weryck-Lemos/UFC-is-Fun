#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    printf("[ ");
    for(int i=0; i<10; i++){
        if(i!=n)printf("%d ",i);
    }
    if(n!=10)printf("ceu ");
    printf("]\n");
}