#include <stdio.h>

int main(){
    int wifi, login, admin;
    scanf("%d %d %d", &wifi, &login, &admin);

    if(wifi==0)printf("you must connect to wifi\n");
    else if(login==0)printf("you need to login first\n");
    else if(admin==0)printf("you must to login as admin\n");
    else printf("done\n");

}