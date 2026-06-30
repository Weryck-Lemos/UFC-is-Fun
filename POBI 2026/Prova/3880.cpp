#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, ans =0;
    cin>>n;

    vector<int> vet(n);
    for(int i=0; i<n; i++)cin>>vet[i];
    
    for(int i=1; i<n; i++){
        ans += abs(vet[i-1]-vet[i]);
    }

    cout<<ans<<"\n";
}