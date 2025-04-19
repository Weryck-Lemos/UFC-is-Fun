#include <stdio.h>

int main(){
    int c, b, g, m;
    scanf("%d %d %d %d", &c, &b, &g, &m);

    int frutas = b+g+m, ans= frutas/c;
    if(frutas%c !=0) ans++;
    printf("%d\n", ans);
}