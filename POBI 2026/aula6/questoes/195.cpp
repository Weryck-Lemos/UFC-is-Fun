#include <bits/stdc++.h>
using namespace std;

vector<int> intToBinary(int n){
    if(n==0) return {0};

    vector<int> binario;

    while(n>0){
        if(n%2==0){
            binario.push_back(0);
        }

        else{
            binario.push_back(1);
        }
        n/=2;
    }

    return binario;

}

int main(){
    int n;
    cin>>n;

    vector<int> binario = intToBinary(n);

    for(int i= binario.size()-1; i>=0; i--){
        cout<<binario[i];
    }

    cout<<endl;
}