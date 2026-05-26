#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    map<string, string> mp;
    string i, p;
    for(int j=0; j<n; j++){
        cin>>i>>p;
        mp[i] = p;
    }

    string word;
    while(cin>>word){
        cout<<mp[word]<<" ";
    }
    
}