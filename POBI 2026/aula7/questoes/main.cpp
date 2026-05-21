#include <bits/stdc++.h>
using namespace std;

int main(){

    map<string, float> altura;

    altura["Carla"] = 1.68;
    altura["Kamila"] = 1.55;
    altura["Denilson"] = 1.72;


    cout<<"Idade de Denilson "<<altura["Denilson"]<<"\n";


    altura.erase("Denilson");
    cout<<altura.count("Denilson");

    
}