#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    int vencedor =-1;
    int menor_dif =101;

    for (int i = 0; i <n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);

        if (a <10 || b<10)continue;

        int dif =abs(a - b);
        if (dif < menor_dif) {
            menor_dif =dif;
            vencedor =i;
        }
    }

    if (vencedor == -1)printf("sem ganhador\n"); 
    else printf("%d\n", vencedor);
}
