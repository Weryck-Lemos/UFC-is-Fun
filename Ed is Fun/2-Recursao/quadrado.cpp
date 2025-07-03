#include <iostream>
using namespace std;

void ida(int n){
    if(n == 1){
        cout<<"1^2 = 1\n";
        return ;
    }

    cout<<n<<"^2 = "<<n-1<<"^2 + 2*"<<n-1<<" + 1 = ?\n";
    ida(n-1);
}

void volta(int n, int k){
    if(n>=k) return ;

    cout<<n+1<<"^2 = "<<n<<"^2 + 2*"<<n<<" + 1 = "<<n*n + 2*n + 1<<"\n";
    volta(n+=1, k);
}

int main(){
    int k;
    cin>>k;

    ida(k);
    volta(1,k);
}