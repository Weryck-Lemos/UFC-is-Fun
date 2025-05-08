#include <iostream>
#include <cstring>
using namespace std;

int dp[10000]={-1};

int fib(int n,int k, int it=2){
    if(it==k)return dp[it];

    dp[n] = dp[n-1]+dp[n-2];
    fib()
    
}

int main(){
    int n,k;
    cin>>n>>k;

    memset(dp, -1, sizeof(dp));
    dp[0]=2;
    dp[1]=2*n;
    cout<<fib(n,k)<<"\n";
}

//1 1
//2 4
//3 8
//4 