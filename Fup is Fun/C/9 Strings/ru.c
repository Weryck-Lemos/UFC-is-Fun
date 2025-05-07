#include <stdio.h>

int main(){
    char frase[101];
    fgets(frase, sizeof(frase),stdin );

    char homem[101], mulher[101];
    int h=0, m=0;

    for(int i=0; frase[i]!='\0'; i++){
        if(frase[i]=='\0')break;

        if(frase[i]=='a' || frase[i]=='e'
        || frase[i]=='i' || frase[i]=='o'
        || frase[i]=='u'){
            homem[h]=frase[i];
            h++;
        }

        else{
            if(frase[i]!=' '){
                mulher[m]=frase[i];
                m++;
            }
        }
    }

    homem[h]='\0', mulher[m]='\0';

    printf("%s\n%s", homem, mulher);
}