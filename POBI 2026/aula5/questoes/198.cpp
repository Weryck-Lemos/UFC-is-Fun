#include <bits/stdc++.h>
using namespace std;

int main() {
    int mat[3][3];

    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            cin >> mat[i][j];

    int soma = 0;
    for(int j = 0; j < 3; j++)
        soma += mat[0][j];

    for(int i = 0; i < 3; i++) {
        int s = 0;
        for(int j = 0; j < 3; j++)
            s += mat[i][j];
        if(s != soma) return cout << "NAO", 0;
    }

    for(int j = 0; j < 3; j++) {
        int s = 0;
        for(int i = 0; i < 3; i++)
            s += mat[i][j];
        if(s != soma) return cout << "NAO", 0;
    }

    int dp = 0, ds = 0;
    for(int i = 0; i < 3; i++) {
        dp += mat[i][i];
        ds += mat[i][2 - i];
    }

    if(dp != soma || ds != soma) return cout << "NAO", 0;

    cout << "SIM";
}