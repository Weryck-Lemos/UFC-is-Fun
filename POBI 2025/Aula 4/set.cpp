#include <iostream>
#include <set>
using namespace std;

int main(){
    set<int> st;

    // Inserindo elementos no set
    st.insert(10);
    st.insert(2);
    st.insert(4);
    st.insert(2); // Duplicata — será ignorada automaticamente

    // Acessando o menor elemento (primeiro na ordem crescente)
    cout<<*st.begin()<<"\n";

    // Acessando o maior elemento (último na ordem crescente)
    cout<< *st.rbegin() <<"\n";

    //Faça assim para printar os elementos
    for(int i : st){
        cout<<i<<" ";
    }
    cout<< st.count(4); //retorna se determinado elemento está no set 
    st.erase(4);        //remove o elemento 4
}

