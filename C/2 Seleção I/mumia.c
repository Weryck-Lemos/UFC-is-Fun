#include <stdio.h>
#include <string.h>

int main(){
    char nome[100], ans[100];
    int idade;
    scanf("%s %d", nome, &idade);

    if(idade<12)strcpy(ans, "crianca");
    else if(idade<18) strcpy(ans,"jovem");
    else if(idade<65) strcpy(ans,"adulto");
    else if(idade<1000) strcpy(ans,"idoso");
    else strcpy(ans, "mumia");

    printf("%s eh %s\n", nome, ans);
}