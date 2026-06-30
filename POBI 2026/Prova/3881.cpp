#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<int> vet(32, 0);

    for(int i=0; i<3; i++){
        int x, y;
        cin>>x>>y;

        for(int j=x; j<=y; j++){
            vet[j]++;
        }
    }

    int ans=0;
    for(int i=0; i<32; i++){
        if(vet[i]==3)ans++;
    }

    cout<<ans<<"\n";
}