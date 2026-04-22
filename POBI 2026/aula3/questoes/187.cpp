#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> vet(10);
    for(int i=0; i<10; i++){
        cin>>vet[i];
    }

    reverse(vet.begin(), vet.end());

    for(int i=0; i<10; i++){
        cout<<vet[i]<<"\n";
    }
}