#include <stdio.h>

int main(){
    int a,b,c, h,l;
    scanf("%d %d %d %d %d", &a, &b, &c, &h, &l);

    int area = h*l;

    if((area>=a*b) || (area>=b*c) || (area>=a*c))printf("S\n");
    else printf("N\n");
}