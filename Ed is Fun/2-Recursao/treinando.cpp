#include "lib.hpp"
namespace alu {

    //imprime recursivamente os elementos de um vetor
    void __show(int * init, int * end) {
        if(init == end) return;
        cout<<*init<<" ";
        __show(init+1, end)
    }

    void show(int * init, int * end) {
        std::cout << "[ ";
        __show(init, end);
        std::cout << "]";
    }

    //imprime recursivamente os elementos de um vetor de trás pra frente
    void __show_rev(int * init, int * end) {
        if(init == end) return;
        __show_rev(init+1, end);
        cout<<*init<<" ";
    }

    void show_rev(int * init, int * end) {
        std::cout << "[ ";
        __show_rev(init, end);
        std::cout << "]";
    }

    void reverse(int * init, int * end) {
        if(init >= end-1)return;

        int aux = *init;
        init* =  *(end-1);
        *(end-1) = aux;
        reverse(init+1, end-1);
    }

    int sum(int * init, int * end) {
        if(init == end) return 0;

        return *init += sum(init+1, end);
    };

    int mult(int * init, int * end) {
        if(init == end) return 1;
        return *init * mult(init, end);
    };

    int menor(int * init, int * end) {
        if(init+1 == end)return *init;

        int ans = menor(init+1, end);

        if(*init < ans)return *init;
        else return ans;
    };

} // namespace alu