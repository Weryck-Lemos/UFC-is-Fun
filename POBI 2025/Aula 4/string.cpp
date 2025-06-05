#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main(){
    /*
    string str = "Hello";

    cout<<str.size()<<"\n";     //tamanho da string
    
    str += " World!";   //agora str == "Hello World!"

    int pos = str.find("Wor");   //verificar se tem uma substring
    if(pos == string::npos){      // se nao estiver, retorna: string::npos
        cout<<"substring nao contida\n";
    }
    else{
        cout<<"substring contida\n";
    }
    */

    /*
    string nome;

    // se a entrada for "Ana Beatriz"
    getline(cin, nome);  //nome vai receber "Ana Beatriz"

    if(nome =="Ana Beatriz"){
        cout<<"true\n";
    }

    */


    string str = "aA45BB-";

    int qtd = 0;

    for(int i=0; i<str.size(); i++){
        if( isdigit(str[i]) ) qtd++; //conta a quantidade de numeros
    }

    cout<<qtd<<"\n"; //2

    // isalpha()     verifica se é letra (a-z ou A-Z)
    // isdigit()     verifica se é dígito (0-9)
    // islower()     verifica se é minúscula
    // isupper()     verifica se é maiúscula
    // ispunct()     verifica se é pontuação (!,?,.)
}


