#include <bits/stdc++.h>
using namespace std;
#define ll long long 

int main(){
    ll n;
    cin>>n;

    vector<ll> vet(n);
    for(ll &x : vet)cin>>x;

    sort(vet.begin(), vet.end());
    ll ans = max(vet[n-1]*vet[n-2]*vet[n-3], vet[0]*vet[1]*vet[n-1]);
    cout<<ans<<"\n";
}