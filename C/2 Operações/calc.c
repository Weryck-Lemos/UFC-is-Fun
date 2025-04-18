#include <stdio.h>

int main(){
    int n1,n2;
    char op;
    scanf("%d %d %c", &n1, &n2, &op);

    if(op=='+')printf("%d", n1+n2);
    else if(op=='-')printf("%d", n1-n2);
    else if(op=='*')printf("%d", n1*n2);
    else printf("%d", n1/n2);
}