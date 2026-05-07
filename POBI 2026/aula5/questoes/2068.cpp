#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    //vector<vector<int>> mat(n, vector<int>(n));
    int mat[11][11];
    int zi, zj;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> mat[i][j];
            if(mat[i][j] == 0) zi = i, zj = j;
        }
    }

    int soma_ref = 0;

    for(int i = 0; i < n; i++){
        bool tem_zero = false;
        for(int j = 0; j < n; j++)
            if(mat[i][j] == 0) tem_zero = true;

        if(!tem_zero){
            for(int j = 0; j < n; j++)
                soma_ref += mat[i][j];
            break;
        }
    }

    int soma_linha_zero = 0;
    for(int j = 0; j < n; j++)
        soma_linha_zero += mat[zi][j];

    int valor = soma_ref - soma_linha_zero;

    cout << valor << '\n';
    cout << zi + 1 << '\n';
    cout << zj + 1 << '\n';
}