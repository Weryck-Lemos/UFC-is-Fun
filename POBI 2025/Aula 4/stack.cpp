#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> stk;

    stk.push(4);  // stk: [4]
    stk.push(6);  // stk: [4, 6]
    stk.push(8);  // stk: [4, 6, 8]
    stk.pop();    // remove 8 → stk: [4, 6]

    cout << stk.top() << "\n";  // 6 elemento no topo
    cout << stk.size() << "\n"; // 2 tamanho da pilha
}
