#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    for(int i=1; i<=n; i+=2)printf("%d\n", i);
    for(int i=n-1; i>=0; i-=2)printf("%d\n", i);
}