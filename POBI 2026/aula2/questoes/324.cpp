#include <iostream>
using namespace std;

int main(){
    int n, ans=0;
    cin>>n;

    for(int i=0; i<n; i++){
        int x,y;
        cin>>x>>y;

        if(x>y)ans+=y;
    }

    cout<<ans<<"\n";
}