#include <iostream>
using namespace std;

void rec(int n){
    if(n==0) return;

    int div = n/2;
    int resto = n%2;
    
    rec(n/2);

    cout<<div<<" "<<resto<<"\n";
}

int main(){
    int n;
    cin>>n;

    rec(n);
}