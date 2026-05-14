#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; 
    cin>>n;

    while(n--){
        string line;
        cin>>line;

        stack<char> caracteres;
        bool ok = true;

        for(char c : line){
            if(c == '{' || c == '[' || c== '(') caracteres.push(c);

            else{
                if (caracteres.empty() || 
                (caracteres.top() != '{' && c == '}') || 
                (caracteres.top() != '[' && c == ']') || 
                (caracteres.top() != '(' && c == ')')) {
                    ok = false;
                    break;
                }
                caracteres.pop();
            } 
        }

        if(!caracteres.empty()) ok = false;

        if(ok)cout<<"S\n";
        else cout<<"N\n";

    }
}