#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >>n;

    map<string, string> dic;
    string eng, ptbr;

    for (int i = 0; i < n; i++) {
        cin >> eng >> ptbr;
        dic[eng] = ptbr;
    }

    string word;
    while (cin >> word) {
        cout << dic[word] << " ";
    }
    cout << "\n";
}


