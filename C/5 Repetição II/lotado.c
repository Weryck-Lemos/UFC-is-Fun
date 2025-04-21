#include <stdio.h>

int main(){
    int c, tot=0;
    scanf("%d", &c);

    while(1){
        int m;
        scanf("%d", &m);

        tot+=m;
        
        if(tot==0)printf("vazio\n");
        else if(tot<c)printf("ainda cabe\n");
        else if(tot>=c && tot<c*2)printf("lotado\n");
        else{
            printf("hora de partir\n");
            break;
        }
    }
}