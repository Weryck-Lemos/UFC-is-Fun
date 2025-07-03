#include <iostream>
using namespace std;

long long memo[41] ={0};

long long fib(int n){
    if(n==1 || n==2) return 1;
    if(n==3 || n==4) return 2;
    if (memo[n]){
        return memo[n];
    }

    return memo[n] = fib(n-1)+fib(n-2) - fib(n-4);   
}

int main(){
    long long n;
    cin>>n;

    cout<<fib(n)<<"\n";
}

/*
1   1
2   1
3   2
4   2
5   3
6   4
7   5
8   7
*/