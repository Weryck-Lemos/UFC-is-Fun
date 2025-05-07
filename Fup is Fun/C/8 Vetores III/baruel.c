#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d",&n,&m);

    int tem[101]={0};

    for(int i = 0; i<m; i++) {
        int fig;
        scanf("%d", &fig);
        tem[fig]++;
    }
    
    int tem_repetidas =0;
    for(int i =1; i<=n; i++) {
        for(int j =0; j<tem[i]-1; j++) {
            if(tem_repetidas)printf(" ");
            printf("%d", i);
            tem_repetidas = 1;
        }
    }
    if(!tem_repetidas) printf("N");
    printf("\n");

    int falta = 0;
    for(int i = 1; i <= n; i++) {
        if(tem[i] == 0) {
            if(falta) printf(" ");
            printf("%d", i);
            falta = 1;
        }
    }
    if(!falta) printf("N");
    printf("\n");
}
