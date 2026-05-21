#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    while(n--){
        string str;
        cin>>str;

        bool ok = true;
        stack<char> st;
        for(char c : str){
            if(c == '(' || c=='[' || c=='{'){
                st.push(c);
            }

            else{
                if(st.empty()){
                    ok = false;
                    break;
                }

                char topo = st.top();
                st.pop();

                if(c==')' && topo != '(' ||
                   c== ']' && topo != '[' ||
                   c== '}' && topo != '{'){
                    ok = false;
                    break;
                }
            }
        }

        if(!st.empty()){
            ok = false;
        }

        if(ok)cout<<"S\n";
        else cout<<"N\n";
    }

    
}