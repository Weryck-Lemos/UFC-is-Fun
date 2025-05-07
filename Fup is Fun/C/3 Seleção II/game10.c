#include <stdio.h>

int main(){
    int n,d,a;
    scanf("%d %d %d", &n, &d, &a);

    int pos = (d-a+n)%n;

    printf("%d\n", pos);
}