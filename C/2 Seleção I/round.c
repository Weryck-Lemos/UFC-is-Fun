#include <stdio.h>
#include <math.h>

int main(){
    char op;
    float n;

    scanf("%c %f", &op, &n);

    if(op=='c') printf("%.0f\n", ceil(n));
    else if(op=='f') printf("%.0f\n", floor(n));
    else printf("%.0f\n", round(n));
}