#include <iostream>
#include <map>
using namespace std;

int main(){
    int c,n;

    map<int, int> repositorio;
    map<int, int> resposta;

    cin>>c>>n;

    for(int i= 0; i<c; i++){
        int programa, versao;
        cin>>programa>>versao;

        repositorio[programa] = versao;
    }

    for(int i=0; i<n; i++){
        int programa, versao;
        cin>>programa>>versao;

        if(repositorio.find(programa)== repositorio.end()){
            resposta[programa] =versao;
            repositorio[programa] = versao;
        }

        else if(repositorio[programa]< versao){
            resposta[programa] = versao;
            repositorio[programa] = versao;
        }
    }

    for(auto i = resposta.begin(); i != resposta.end(); i++){
        cout<<i->first<<" "<<i->second<<endl;
    }
}