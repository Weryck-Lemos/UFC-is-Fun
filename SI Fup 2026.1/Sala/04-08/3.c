#include <stdio.h>

int main(){

    char op;
    scanf(" %c",&op );
    
    for(int i=0; i<=9; i++){
        for(int j=0; j<=9; j++){
            if(op=='+') printf("%d + %d = %d\n", i, j, i+j);
            else if(op=='-') printf("%d - %d = %d\n", i, j, i-j);
            else if(op=='*') printf("%d * %d = %d\n", i, j, i*j);
            else if(op=='/') {
                if(j==0) continue;
                printf("%d / %d = %.2f\n", i, j, (float)i/j);
            }
        }
        printf("\n");
    }
}