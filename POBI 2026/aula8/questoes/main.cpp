#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    ll n;
    cin>>n;

    if(n>=2){
        cout<<2<<" ";
    }

    for(ll i=3; i<=n; i+=2){
        bool isprime = true;
        for(ll j=3; j*j<=i; j+=2){
            if(i%j==0){
                isprime = false;
                break;
            }
        }
        if(isprime){
            cout<<i<<" ";
        }
    }

    
}


