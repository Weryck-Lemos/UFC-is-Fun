#include <stdio.h>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);

    printf("[ ");
    for(int i=n, j=m; i<=m; i++, j--){
        printf("%d %d ", i, j);
    }
    printf("]\n");
}