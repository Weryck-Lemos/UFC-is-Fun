#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin>>n;

    vector<int> vet(n);
    for(int i=0; i<n; i++){
        cin>>vet[i];
    }

    sort(vet.begin(), vet.end());
    cout<<vet[ vet.size()-1]<<"\n"<<vet[0]<<"\n";
    
}