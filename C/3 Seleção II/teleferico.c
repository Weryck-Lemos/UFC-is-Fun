#include <stdio.h>

int main(){
    int c,a;
    scanf("%d %d", &c, &a);

    int ans = a/(c-1);
    if(a%(c-1) !=0)ans++;

    printf("%d\n", ans);
}