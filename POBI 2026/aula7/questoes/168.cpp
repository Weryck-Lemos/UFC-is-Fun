#include <bits/stdc++.h>
using namespace std;

int main() {

    int n, c, m;
    cin >>n>>c>>m;

    map<int, bool> faltando;

    for (int i = 0; i<c; i++) {
        int x;
        cin>>x;
        faltando[x] = true; 
    }

    for (int i = 0; i<m;i++) {
        int y;
        cin>>y;


        auto it=faltando.find(y);

        if (it != faltando.end()) {
            faltando.erase(it);
        }
    }

    cout << faltando.size()<<"\n";
}