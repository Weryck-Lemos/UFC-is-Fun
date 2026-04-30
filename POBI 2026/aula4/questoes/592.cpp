#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    for (char c : s) {
        if (c == '-') {
            cout << '-';
        }
        else if (c >= 'A' && c <= 'C') cout << '2';
        else if (c >= 'D' && c <= 'F') cout << '3';
        else if (c >= 'G' && c <= 'I') cout << '4';
        else if (c >= 'J' && c <= 'L') cout << '5';
        else if (c >= 'M' && c <= 'O') cout << '6';
        else if (c >= 'P' && c <= 'S') cout << '7';
        else if (c >= 'T' && c <= 'V') cout << '8';
        else if (c >= 'W' && c <= 'Z') cout << '9';
    }

    cout << "\n";
}