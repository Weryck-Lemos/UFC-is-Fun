#include <bits/stdc++.h>
using namespace std

int main() {
    
    int n;
    cin>>n;

    if(n<2){
        cout<<"Nao e primo\n";
    }

    for(int i=2; i*i<=n; i++){
        if(n%i==0){
            cout<<"Nao e primo\n";
            return 0;
        }
    }

    cout<<"E primo\n";
}


