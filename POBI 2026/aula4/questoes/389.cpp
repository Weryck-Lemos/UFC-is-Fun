#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    string resp = "";

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'p' && i + 1 < s.size()) {
            resp += s[i + 1];
            i++;
        }
    }

    cout << resp << endl;
}