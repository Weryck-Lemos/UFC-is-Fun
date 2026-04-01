#include <stdio.h>

int main(){
    int A_votes = 0, B_votes = 0, null_votes = 0;
    char vote;
    printf("faça seu voto\n");
    do{
        scanf("%c", &vote);

        switch (vote)
        {
            case 'a':
                A_votes++;
                break;
            
            case 'b':
                B_votes++;
                break;
            

            case 'n':
                null_votes++;
                break;
        }

    }while(vote != 's');

    printf("Votos A: %d\nVotos B: %d\nNulo: %d\n", A_votes, B_votes, null_votes);
}