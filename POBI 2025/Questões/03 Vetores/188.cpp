#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;

    vector<int> vet(13,0);
    for(int i=0; i<n; i++){
        int x;
        cin>>x;

        vet[x]++;
    }

    //for(int i=0; i<=12; i++ )cout<<vet[i]<<" ";

    

    int maximo = 0;
    for(int i=0; i<13; i++){
        maximo = max(maximo, vet[i]);
    }

    for(int i=0; i<13; i++){
        if(vet[i]== maximo)cout<<i<<" ";
    }
    cout<<"\n";

    
}