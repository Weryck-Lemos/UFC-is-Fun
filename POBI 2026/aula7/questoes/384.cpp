#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main(){
    int n, m, pessoa;



    cin>>n;
    vector<int> fila(n);
    for(int i=0; i<n; i++){
        cin>>fila[i];
    }

    cin>>m;
    set<int> sairam;
    for(int i=0; i<m; i++){
        cin>>pessoa;
        sairam.insert(pessoa);
    }

    for(int i=0; i<n; i++){
        if(sairam.find(fila[i]) == sairam.end()){
            cout<< fila[i]<< " ";
        }
    }
    
}