#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cin>>n;

    vector<int> vet(n);
    for(int &i : vet)cin>>i;

    int ans=0, maior =0;
    for(int i=n-1; i>=0; i--){
        if(vet[i]<=maior){
            ans++;
        }

        if(vet[i]>maior){
            maior = vet[i];
        }
        
    }

    cout<<ans<<"\n";
}