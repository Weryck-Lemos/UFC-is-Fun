#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, x;
    cin>>n;

    vector<int> vet(2001);

    for(int i=0; i<n; i++){
        cin>>x;

        vet[x]++;
    }

    int ans, oco= INT_MAX;
    for(int i=2001; i>=0; i--){
        if(vet[i]<=oco && vet[i]!=0){
        oco = vet[i];
        ans=i;
        }
    }

    cout<<ans<<"\n";
}