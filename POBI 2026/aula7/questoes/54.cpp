#include <iostream>
#include <set>
using namespace std;

int main(){
    int c, fabricado=0;

    set<int> tacos;
    cin >> c;

    for(int i=0; i<c; i++){
        int consulta;
        cin>>consulta;

        if(tacos.find(consulta)== tacos.end()){
            tacos.insert(consulta);
            fabricado+=2;
        }

        else{
            tacos.erase(consulta);
        }
    }

    cout<< fabricado;
}   