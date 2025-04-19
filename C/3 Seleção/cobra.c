#include <stdio.h>

int main(){
    int n,x,y,s;
    char c;
    scanf("%d %d %d %c %d", &n, &x, &y, &c, &s);

    int ansX=x, ansY=y;

    if(s>n)s %= n;
    
    if(c=='U'){
        ansY -= s;
        if(ansY <0)ansY= ansY+n;
    }

    else if(c=='D'){
        ansY += s;
        if(ansY >n) ansY= ansY-n;
    }

    else if(c=='L'){
        ansX -=s;
        if(ansX <0)ansX = ansX+n;
    }

    else{
        ansX +=s;
        if(ansX >n)ansX = ansX-n;
    }
    
    printf("%d %d\n",ansX, ansY);
}