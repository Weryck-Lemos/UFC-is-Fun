#include <stdio.h>

int main(){
    float value, acumulator=0;
    int total=0;

    while(1){
        scanf("%f", &value);
        if(value<=0)break;
        acumulator += value;
        total++;
    }

    printf("%.2f\n", acumulator/total);
}