#include <bits/stdc++.h>
using namespace std;

int main(){
    //vector<vector<int>> mat(3, vector<int> 3);
    int mat[3][3];

    for(int i=0; i<3; i++){
        int suml = 0
        for(int j=0; j<3; j++){
            cin>>mat[i][j];
            suml+=mat[i][j];
        }
        cout<<"Linha "<<i<<": "<<suml<<"\n";
    }

}