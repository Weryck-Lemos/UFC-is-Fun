#include <iostream>
using namespace std;

int coe(int n, int k){
    if(k==0 || n==k) return 1;

    return coe(n-1, k-1) +coe(n-1,k);
}

int main(){

    int n,m;
    cin>>n>>m;
    cout<<coe(n,m)<<"\n";
}