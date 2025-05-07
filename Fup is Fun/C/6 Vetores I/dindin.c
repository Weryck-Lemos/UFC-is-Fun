#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int chocolate =0, limao =0,manha =0, tarde =0;
    for (int i = 0; i < n; i++) {
        char s,t;
        scanf(" %c %c", &s,&t);

        if(s=='c') chocolate++;
        else if(s=='l') limao++;

        if(t=='m') manha++;
        else if(t== 't') tarde++;
    }

    if(chocolate > limao)printf("c\n");
    else if(limao > chocolate)printf("l\n");
    else printf("empate\n");

    if (manha <tarde) printf("m\n");
    else if (tarde < manha)printf("t\n");
    else printf("empate\n");
}
