#include <iostream>
using namespace std;

int f(int n, int m =3){
    if(!n)return 0;
    return m + f(n-1, m+2);
}

int main(){
    int n;
    cin>>n;

    cout<<f(n)<<"\n";
}