#include <stdio.h>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);

    printf("[ ");
    for(int i=n; i<m; i++){
        if(i%2==0)continue;
        printf("%d ", i);
    }
    printf("]\n");
}