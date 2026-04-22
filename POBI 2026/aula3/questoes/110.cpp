#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, maxi=1, ans=1;
    cin>>n;

    vector<int> vet(n);
    for(int i=0; i<n; i++)cin>>vet[i];

    for(int i=0; i<n-1; i++){
        if(vet[i] == vet[i+1])maxi++;
        else maxi=1;
        ans = max(ans, maxi);
    }
    cout<<ans<<"\n";
}