#include <stdio.h>

int main(){
    int n1,n2,n3;
    scanf("%d %d %d", &n1, &n2, &n3);

    if(n1 ==n2 && n2==n3)printf("3\n");
    else if(n1!= n2 && n2!=n3 && n1!=n3) printf("0\n");
    else printf("2\n");
}