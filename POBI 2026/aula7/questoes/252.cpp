#include <iostream>
#include <set>
using namespace std;

int main(){
    int n;
    cin>>n;
    set<int> presenca;

    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        presenca.insert(x);
    }

    cout<<presenca.size()<<endl;
}