#include <stdio.h>
#include <math.h>

int main() {
    float t;
    scanf("%f", &t);
    int troco = round(t *100);

    int valores[] = {10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10,5};
    int quantidade[11] = {0};
    int n =11;

    for (int i=0; i<n; i++) {
        quantidade[i] = troco / valores[i];
        troco = troco % valores[i];
    }

    for (int i =0; i<n; i++) {
        if (quantidade[i] >0) printf("%d de %.2f\n", quantidade[i], valores[i]/100.0);
    }

    if (troco>0) printf("Falta %.2f\n", troco /100.0);
}
