#include <stdio.h>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);

    for(int i=n; i<=m; i++){
        if(i%3==0 && i%5==0) printf("zigzag\n");
        else if(i%3==0) printf("zig\n");
        else if(i%5==0) printf("zag\n");
        else printf("%d\n", i);
    }
}