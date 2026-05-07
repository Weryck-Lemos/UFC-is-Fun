#include <bits/stdc++.h>
using namespace std;

int main() {
    int mat[3][3];

    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            cin >> mat[i][j];

    int dp = 0, ds = 0;

    for(int i = 0; i < 3; i++) {
        dp += mat[i][i];
        ds += mat[i][2 - i];
    }

    cout << "Diagonal principal: " << dp << '\n';
    cout << "Diagonal secundaria: " << ds << '\n';
}