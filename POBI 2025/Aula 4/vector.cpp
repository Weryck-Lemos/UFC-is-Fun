#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> v ={10, 20, 30};

    cout << v.size() << "\n";  //retorna o tamanho do vetor: 3

    cout<< v.empty() <<"\n";  //retorna 1 se estiver vazio

    cout<< v.front() <<"\n";  //primeiro elemento do vetor

    cout<< v.back() <<"\n";  //ultimo elemento do vetor

    v.clear();               //limpa o vetor
}

