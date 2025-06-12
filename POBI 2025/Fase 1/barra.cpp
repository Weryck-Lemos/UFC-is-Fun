#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, maior=0;
    cin>>n;

    vector<int> vet(n);
    for(int i=0; i<n; i++){
        cin>>vet[i];
        maior = max(vet[i], maior);
    }

    for(int i=0; i<n; i++){
        vet[i]-=maior;
    }
    for(int i=0; i<maior; i++){
        for(int j=0; j<n; j++){
            if(vet[j]<0)cout<<0<<" ";
            else cout<<1<<" ";
            vet[j]+=1;
        }
        cout<<"\n";
    }
}