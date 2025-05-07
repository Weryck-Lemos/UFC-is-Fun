#include <stdio.h>
#include <string.h>

int main(){
    int n;
    scanf("%d ", &n);

    while(n--){
        char op[100];
        fgets(op, sizeof(op), stdin);

        int tot=0;
        size_t ln = strlen(op);
        for(size_t i=0; i<ln-1; i++){
            if(op[i]=='1')tot+=2;
            else if(op[i]=='7')tot+=3;
            else if(op[i]=='4')tot+=4;
            else if(op[i]=='5' || op[i]=='3' || op[i]=='2')tot+=5;
            else if(op[i]=='6' || op[i]=='9' || op[i]=='0')tot+=6;
            else tot+=7;
        }

        printf("%d leds\n", tot);
    }
}