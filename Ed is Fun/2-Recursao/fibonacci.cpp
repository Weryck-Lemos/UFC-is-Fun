#include <iostream>
using namespace std;

int fib(int n,int k){
    if(n==1 || n==2) return 1;

    return fib(n-1, k)+ k*fib(n-2,k);
    
}

int main(){
    int n,k;
    cin>>n>>k;
    cout<<fib(n,k)<<"\n";
}

//1 1
//2 1
//3 1 + 3*1 = 4
//4 4 + 3*1 = 7
//5 7 + 4*3 = 19
//6 19 + 7*3 = 40