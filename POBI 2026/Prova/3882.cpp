#include <bits/stdc++.h>
using namespace std;

int main(){
    int n1,n2,n3,n4;

    cin>>n1>>n2>>n3>>n4;

    int ans=0;

    ans+=n4;

    ans+= n3;
    n1-=n3;

    ans += n2/2;
    n2 %= 2;
    if(n2>0){
        ans++;
        n1-=n2*2;
    }

    if(n1>0)ans+=n1/4;
    n1%=4;

    if(n1>0)ans++;

    cout<<ans;
}