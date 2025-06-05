#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, int> idade;

    idade["Ana"] = 20;
    idade["Bruno"] = 25;
    idade["Carlos"] = 22;

    // Acessando valores
    cout << "Idade de Bruno: " << idade["Bruno"] << "\n"; // 25

    // Verificando se uma chave existe
    if (idade.count("Carlos")) {
        cout << "Carlos está presente.\n";
    }

    // Percorrendo o mapa (em ordem alfabética das chaves)
    for (auto par : idade) {
        cout << par.first << " " << par.second << "\n";
    }
}


