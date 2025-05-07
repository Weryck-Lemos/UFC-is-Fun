#include <stdio.h>

int main(){
    float a,b, area=160*70;
    scanf("%f %f", &a, &b);

    float felix = (a+b)*70/2, marzia = area - felix;

    if(felix > marzia)printf("1\n");
    else if(marzia > felix)printf("2\n");
    else printf("0\n");
}