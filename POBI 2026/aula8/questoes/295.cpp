#include <iostream>
using namespace std;

int main(){
    int n;
    cin>>n;

    bool isprime[n +1];

    for(int i=2; i<=n; i++) isprime[i] = true;

    for(int i=2; i<=n; i++){
        if(!isprime[i]) continue;

        for(int j=2*i; j<=n; j+=i) isprime[j] = false;
    }

    for(int i=2; i<=n; i++){
        if(isprime[i]) cout<<i<<" ";
    }

}
