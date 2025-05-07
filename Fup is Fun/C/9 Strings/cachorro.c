#include <stdio.h>

int main(){
    char frase[201], ans[201];
    fgets(frase, sizeof(frase), stdin);

    int i=0, j=0;
    int space =0;
    
    while(frase[i]!='\0'){
        if(frase[i]==' '){
            if(!space){
                ans[j++] = ' ';
                space = 1;
            }
        }
        else{
            ans[j++]=frase[i];
            space=0;
        }
        i++;
    }

    if(j>0 && ans[j-1]==' ')j--;

    ans[j]='\0';
    printf("%s", ans);
}