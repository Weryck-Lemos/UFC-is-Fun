#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool greedy(vector<ll> vet, ll c, ll t){
    ll tot=1, pipo=0;

    for(int i: vet){
        if(i>t){
            return false;
        }

        if(pipo+i > t){
            tot+=1;
            pipo=i;
        }else{
            pipo+=i;
        }

    }
    return tot<=c;
}

int main(){
    ll n,c,t;
    cin>>n>>c>>t;

    ll e = 1, d=0;
    vector<ll> vet(n);
    for(int i=0; i<n; i++){
        cin>>vet[i];
        d+=vet[i];
    }
    

    
    ll meio, ans;
    while(e<=d){
        meio = (e+d)/2;

        if(greedy(vet, c , t*meio)){
            d= meio-1;
            ans = meio;
        }
        else e = meio+1;
    }  
    cout<<ans<<"\n";
}