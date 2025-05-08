#include <iostream>
#include <string>
using namespace std;

void printStr(string str, int it=0){
    if(str[it]=='\0')return;
    cout<<str[it];
    printStr(str, it+1);
}

void printTower(string str, int it=0){
    if(str[it]=='\0') return;

    printTower(str, it+1);
    printStr(str, it);
    cout<<"\n"; 
}

int main(){

    string str;
    cin>>str;

    printTower(str);
}