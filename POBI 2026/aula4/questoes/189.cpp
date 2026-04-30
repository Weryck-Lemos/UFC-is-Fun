#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    int freq[10] = {0};

    while (n--) {
        string s;
        cin >> s;

        for (int i =0; i<s.size(); i++) {
            freq[s[i] - '0']++;
        }
    }

    for (int i = 0; i < 10; i++) {
        cout << i << " - " << freq[i] << endl;
    }
}