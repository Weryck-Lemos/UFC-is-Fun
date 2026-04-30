#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {


    string s = "Exemplo De Texto";

    for (int i=0; i<s.size(); i++) s[i] = tolower(s[i]);
    cout << "minusculo: " << s << endl;

    for (int i=0; i<s.size(); i++) s[i] = toupper(s[i]);
    cout << "maiusculo: " << s << endl;

  
}