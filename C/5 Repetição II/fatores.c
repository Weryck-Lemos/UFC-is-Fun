#include <stdio.h>

int main() {
    int n, i, count;
    scanf("%d", &n);

    for (i =2; i<= n; i++) {
        count =0;
        while(n%i == 0) {
            count++;
            n/= i;
        }
        if(count > 0) {
            printf("%d %d\n", i, count);
        }
    }

    if (n > 1) {
        printf("%d 1\n", n);
    }
}