#include <stdio.h>

int main(){
    int mae, f1,f2;
    scanf("%d %d %d", &mae, &f1, &f2);

    int f3 = mae -(f1+f2);

    if(f1>f2 && f1>f3)printf("%d\n", f1);
    else if(f2>f1 && f2>f3)printf("%d\n", f2);
    else printf("%d\n", f3);
}