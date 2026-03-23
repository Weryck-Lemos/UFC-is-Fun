#include <stdio.h>

int main(){
    float a,b;
    scanf("%f %f", &a, &b);

    printf("%d\n", (int)(a/b));
    printf("%d\n", (int)a%(int)b);
    printf("%.2f\n", a/b);
}