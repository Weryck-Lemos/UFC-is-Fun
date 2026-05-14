#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    if (n == 0) {
        cout << 0 <<"\n";
        return 0;
    }

    stack<int> s;
    while (n > 0) {
        s.push(n % 2);
        n /= 2;
    }

    while (!s.empty()) {
        cout << s.top();
        s.pop();
    }
    cout <<"\n";
}