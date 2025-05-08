#include  <iostream>
#include <vector>
using namespace std;

int n,m;
int x[]={-1,1,0,0} ,y[]={0,0,1,-1};
char mat[1000][1000];

bool ispossible(int i, int j){
    return (i>=0 && i<n && j>=0 && j<m && mat[i][j]=='#');
}

void tocar_fogo(int i, int j){
    mat[i][j]='o';

    for(int k=0; k<4; k++){
        int di = i+x[k];
        int dj = j+y[k];

        if(ispossible(di,dj)) tocar_fogo(di,dj);
    }

}

int main(){
    int nStart,mStart;
    cin>>n>>m>>nStart>>mStart;
    
    for (int i = 0; i < n; i++) {
        for(int j=0; j<m; j++){
            cin>>mat[i][j];
        }
    }

    cout<<"-------------------\n";

    if(mat[nStart][mStart]=='#')tocar_fogo(nStart,mStart);

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout<<mat[i][j];
        }

        cout<<"\n";
    }
}