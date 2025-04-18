#include <stdio.h>

int main() {
    float p1, p2, p3, price1, price2, price3, qtd;
    scanf("%f %f %f", &p1, &p2, &p3);
    scanf("%f %f %f", &price1, &price2, &price3);
    scanf("%f", &qtd);

    float total = (p1*price1)+ (p2*price2) + (p3*price3);
    printf("%.2f\n", qtd -total);
}
