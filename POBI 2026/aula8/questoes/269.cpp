#include <iostream>
using namespace std;

bool primo(int n){
    if(n<2) return false;

    for(int i=2; i*i<=n; i++){
        if(n%i == 0) return false;
    }

    return true;
}

int main(){
    int a;
    cin>>a;

    for(int i=2; i<=a; i++){
        if(primo(i)) cout<<i<<" ";
    }
}