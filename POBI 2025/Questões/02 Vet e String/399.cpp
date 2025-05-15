#include <iostream>
#include <string>
using namespace std;

int main(){
    string str;
    cin>>str;

    string vogais="", cons = "";

    for(int i=0; i<str.size(); i++){
        if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u'){
            vogais.push_back(str[i]);
        }

        else{
            cons.push_back(str[i]);
        }
    }

    cout<<"Vogais: "<<vogais<<"\n"<<"Consoantes: "<<cons<<"\n";

}