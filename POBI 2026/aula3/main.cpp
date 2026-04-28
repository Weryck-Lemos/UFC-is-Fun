#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> vet(3);

    for(int i=0; i<3; i++){
        cin>>vet[i];
    }

    sort(vet.begin(), vet.end());
    for(int i=0; i<3; i++)cout<<vet[i]<<"\n";
}
