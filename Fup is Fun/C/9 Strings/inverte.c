#include <stdio.h>

int main(){
    char v;
    scanf("%c", &v);

    if(v>='a' && v<='z')printf("%c\n", v-32);
    else if(v >='A' && v<='Z') printf("%c\n", v+32);
    else printf("%c\n", v);
}