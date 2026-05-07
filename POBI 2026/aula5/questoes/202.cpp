#include <bits/stdc++.h>
using namespace std;

int main() {
    int mat[3][3], mx = -1e9;

    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++) {
            cin >> mat[i][j];
            mx = max(mx, mat[i][j]);
        }

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(mat[i][j] == mx) mat[i][j] = -1;
            cout << mat[i][j] << " ";
        }
        cout << '\n';
    }
}