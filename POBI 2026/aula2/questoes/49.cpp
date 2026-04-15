#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, inf = 1e9;
    cin>>n;

    vector<int> vet(n);
    for(int i=0; i<n; i++){
        int x;
        cin>>x;

        if(!x) vet[i]=0;
        else vet[i]=inf;
    }

    for(int i=1; i<n; i++){
        vet[i] = min(vet[i], vet[i-1]+1);
    }

    for(int i=n-2; i>=0; i--){
        vet[i] = min(vet[i], vet[i+1]+1);
    }

    for(int i=0; i<n; i++){
        vet[i] = min(vet[i], 9);
    }

    for(int i=0; i<n; i++)cout<<vet[i]<<" ";
}