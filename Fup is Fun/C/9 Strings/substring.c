#include <stdio.h>
#include <string.h>

int main(){
    char frase[101];
    fgets(frase, sizeof(frase), stdin);
    frase[strcspn(frase,"\n")] = '\0';

    int n,m;
    scanf("%d %d", &n, &m);

    for(int i=n; i<n+m; i++){
        if(frase[i]=='\0') break;
        printf("%c", frase[i]);
    }
    printf("\n");
}