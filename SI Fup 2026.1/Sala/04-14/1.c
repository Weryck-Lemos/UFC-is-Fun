#include <stdio.h>
#define n 10
int main(){
    float vet[n], acc=0;
    int qtd=0;

    for(int i=0; i<n; i++){
        scanf("%f", &vet[i]);
        acc += vet[i];
        
    }

    float big =vet[0], small = vet[0], media = acc/n;

    for(int i=0; i<n; i++){
        if(vet[i]>media) qtd++;
        if(vet[i]> big)big=vet[i];
        if(vet[i]<small)small=vet[i];
    }

    printf("Maior Nota: %f\nMenor nota: %f\nMédia: %f\nAlunos acima da média: %d\n", big, small, media, qtd);
}