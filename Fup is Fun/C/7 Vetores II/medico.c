#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int vet[n];
    for (int i =0; i<n; i++) scanf("%d", &vet[i]);

    int desprotegidos = 0;
    for (int i=0; i< n; i++) {
        if (vet[i]==0) {
            int protegido = 0;

            if (i>0 && vet[i-1] == 1) protegido = 1;
            if (i < n -1 && vet[i+1] == 1) protegido = 1;
            if (!protegido)desprotegidos++;
        }
    }

    printf("%d\n", desprotegidos);
}
