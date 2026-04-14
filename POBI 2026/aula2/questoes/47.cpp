#include <iostream>
using namespace std;

int main(){
    int n, x, verif=0, ans=0;
    cin>>n;

    for(int i=0; i<n; i++){
        cin>>x;

        if(x){
            if(verif==0){
                verif++;
            }
            else{
                verif=1;
            }
        }

        else if(!x){
            if(verif==1 || verif==2){
                verif++;
            }
            else{
                verif=0;
            }
        }

        if(verif==3){
            ans++;
            verif=0;
        }

    }

    cout<<ans<<"\n";
}