#include <stdio.h>

int main(){
    float n1, n2;
    scanf("%f %f", &n1, &n2);

    float media = (n1+n2)/2;

    if(media>=7) printf("aprovado\n");
    else if(media<4) printf("reprovado\n");
    else{
        float af;
        scanf("%f", &af);

        media = (media+af)/2;
        if(media>=5)printf("aprovado na final\n");
        else printf("reprovado na final\n");
    }
}