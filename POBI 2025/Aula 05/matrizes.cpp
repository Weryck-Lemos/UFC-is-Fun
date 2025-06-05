#include <iostream>
using namespace std;

int main(){

    int n=3;
    int matriz[n][n] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout<<matriz[i][j]<<" ";
        }
        cout<<"\n";
    }


    int maior = matriz[0][0];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if (matriz[i][j] > maior)
                maior = matriz[i][j];
        }
    }

    cout<<maior<<"\n";



    
}