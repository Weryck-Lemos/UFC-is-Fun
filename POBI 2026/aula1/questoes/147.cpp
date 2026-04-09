#include <iostream>
using namespace std;

int main(){
    double n1, n2;
    cin>>n1>>n2;

    double media = (n1*2+ n2*3) /5;

    if(media>= 7){
        cout<<"Aprovado\n";
    }
    else if(media<3){
        cout<<"Reprovado\n";
    }

    else{
        cout<<"Final\n";
    }
}