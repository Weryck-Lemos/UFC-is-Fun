#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){ 
    
    vector<int> vet = {4, 3, 5, 10, 9, 1};
    vector<int> copia = vet;
    sort(copia.begin(), copia.end(), greater<int>());

    for(int x : vet){
        cout<<x<<" ";
    }
}










