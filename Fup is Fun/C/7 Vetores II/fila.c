#include <stdio.h>

int main(){
    int n, par[50], impar[50], pr=0, im=0;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        int x;
        scanf("%d", &x);

        if(x%2==0){
            par[pr]=x;
            pr++;
        }

        else{
            impar[im]=x;
            im++;
        }
    }

    printf("[ ");
    for(int i=0; i<im; i++)printf("%d ", impar[i]);
    printf("]\n");

    printf("[ ");
    for(int i=0; i<pr; i++)printf("%d ",par[i]);
    printf("]\n");
}