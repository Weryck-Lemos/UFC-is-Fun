#include <iostream>
using namespace std;

int f(int n){
    if(n==0)return 0;
    return 8 + f(n-1);
}

int main(){
    int n;
    cin>>n;

    cout<<f(n)+12<<"\n";
}