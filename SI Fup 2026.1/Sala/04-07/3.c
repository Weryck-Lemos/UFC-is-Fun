#include <stdio.h>

int main(){
    int number;
    scanf("%d", &number);
    
    for(int i=2; i<= number; i++ ){
        int count = 0;
        for(int j=1; j<=i; j++){
            if(i%j == 0)count++;
        }

        if(count==2) printf("%d\n", i);
    }
}