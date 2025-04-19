#include <stdio.h>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);

    printf("[ ");
    for(int i=n; i>m; i--)printf("%d ", i);
    printf("]\n");
}