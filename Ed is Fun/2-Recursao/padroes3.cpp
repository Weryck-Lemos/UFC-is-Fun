#include <iostream>
using namespace std;


int main(){
    int n, k;
    cin>>n>>k;
  
    int soma = n-1;
    int vet[20]={0};
    vet[0]=1;
    for(int i=1; i<k; i++){
        vet[i] = vet[i-1]+ soma;
        soma+=n-2;
    }

    cout<<vet[k-1]<<"\n";
}

/*


3:  1   3   6   10
4:  1   4   9   16
5:  1   5   12  22

add:    2    3   4
        3    5   7
        4    7   10


*/