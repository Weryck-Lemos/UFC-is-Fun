#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, ans=0;
    cin>>n;

    vector<int> dir(61,0), esq(61,0);

    while(n--){
        int valor;
        char lado;

        cin>>valor>>lado;

        if(lado == 'D')dir[valor]++;
        else esq[valor]++;
    }

    for(int i=0; i<=60; i++){
        ans += min(dir[i], esq[i]);
    }

    cout<<ans<<"\n";
}