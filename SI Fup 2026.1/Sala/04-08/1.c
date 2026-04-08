#include <stdio.h>

int main(){
    int number, values, max, min;
    scanf("%d", &number);

    for(int i=0; i<number; i++){
        scanf("%d", &values);

        if(i==0){
            max = values;
            min = values;
        }

        if(values > max) max = values;
        else if(values < min) min = values;
    }

    printf("maior valor: %d\nmenor valor: %d\n",max, min);
}