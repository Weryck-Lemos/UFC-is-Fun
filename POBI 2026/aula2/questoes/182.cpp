#include <iostream>
using namespace std;

int main(){
    int n, acum=0, tot=0;
    cin>>n;

    for(int i=1; i<=n; i++){
        if(n%i==0){
            acum+=i;
            tot+=1;
        }
    }

    cout<<tot<<" divisor(es): ";
    for(int i=1; i<=n; i++){
        if(n%i==0){
            cout<<i<<" ";
        }
    }

    cout<<"\n"<<"Soma de divisores = "<<acum<<"\n";
    if(tot !=2) cout<<"Nao primo";
    else cout<<"Primo\n";    
}