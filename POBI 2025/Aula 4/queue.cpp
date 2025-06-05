#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> fila;

    fila.push(0); // fila = [0]
    fila.push(1); // fila = [0, 1]
    fila.push(5); // fila = [0, 1, 5]
    fila.push(3); // fila = [0, 1, 5, 3]
    fila.pop();   // remove o 0 fila = [1, 5, 3]

    cout << fila.front() << "\n"; // 1
    cout << fila.size() << "\n";  // 3
}

