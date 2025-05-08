#include <iostream>
using namespace std;

void space(int n){
    if(n==0)return;
    cout<<" ";
    space(n-1);
}

void diag(string word,int it=0){
    if(it>= int(word.size())) {
        return;
    }
    
    space(it);
    cout<<word[it]<<"\n";
    diag(word, it+=1);
}

int main(){
    string w;
    cin>>w;

    diag(w);
}