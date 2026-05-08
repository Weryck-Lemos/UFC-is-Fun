#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin>>n;
    cin.ignore();

    stack<char> s;
    bool balanceado = true;

    for(int i=0; i<n; i++){
        string line;
        getline(cin, line);

        for(char c : line){
            if(c =='{'){
                s.push(c);
            }
            else if(c == '}'){
                if(s.empty() || s.top()!='{'){
                    balanceado = false;
                    break;
                }
                s.pop();
            }
        }
        if(!balanceado) break;
    }

    if(!s.empty()){
        balanceado = false;
    }

    if(balanceado) cout<<'S'<<endl;
    else cout<<'N'<<endl;
}