#include <stdio.h>

int main(){
    int n, vet1[50];
    scanf("%d", &n);
    for(int i=0; i<n; i++)scanf("%d", &vet1[i]);
    
    int m, vet2[50];
    scanf("%d", &m);
    for(int i=0; i<m; i++) scanf("%d", &vet2[i]);

    for(int i=0; i<n; i++){
        int contido=0;
        for(int j=0; j<m; j++){
            if(vet1[i]==vet2[j])contido=1;
        }
        if(!contido){
            printf("nao\n");
            return 0;
        }
    }

    printf("sim\n");
}