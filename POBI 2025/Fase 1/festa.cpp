#include <iostream>
using namespace std;

int main(){
    int e,s,l;
    cin>>e>>s>>l;

    int traj1 = abs(e-s)+ abs(s-l)+ abs(l-e);
    cout<<traj1<<"\n";
}