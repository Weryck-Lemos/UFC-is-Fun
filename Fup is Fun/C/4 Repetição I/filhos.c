#include <stdio.h>

int main(){
    int n,m;
    scanf("%d %d", &n, &m);

    for(int i=n; i<n+(m*2); i+=2)printf("%d\n", i);
}