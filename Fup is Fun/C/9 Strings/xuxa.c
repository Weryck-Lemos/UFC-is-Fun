#include <stdio.h>
#include <string.h>

int main(){
    char frase[101];
    fgets(frase, sizeof(frase), stdin);
    frase[strcspn(frase, "\n")] = '\0';

    int tam = strlen(frase);
    for(int i=tam-1; i>=0; i--){
        printf("%c", frase[i]);
    }
    printf("\n");
}