#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    int N, count = 0;
    cin >> N;
    cin.ignore(); 

    while (count < N) {
        string line;
        getline(cin, line);

        stack<char> caracteres;
        bool ok = true;

        for (char c : line) {
            if (c == '{' || c == '[' || c == '(') {
                caracteres.push(c);
            } else {
                if (caracteres.empty() || (caracteres.top() != '{' && c == '}') || (caracteres.top() != '[' && c == ']') || (caracteres.top() != '(' && c == ')')) {
                    ok = false;
                    break;
                }
                caracteres.pop(); // Remove o caractere de abertura correspondente da pilha
            }
        }

        if (!caracteres.empty()) ok = false;

        if (ok == true) {
            cout << "S" << endl;
        } else {
            cout << "N" << endl;
        }

        count++;
    }

}
