#include <iostream>
#include <iomanip>
using namespace std;

float f(float n, float c){
    if(n==0)return 0;
    return c+ f(n-1, c/2);

    //0 = 2*x - c -> x=c/2
    //x = x+c - c -> y
    //


}

int main(){
    int n,c;
    cin>>n>>c;

    cout<<fixed<<setprecision(2)<<f(n,c/2)<<"\n";

    //5 20 -20 = 0
    //4 30 - 20 = 10;
    //3 35 - 20 = 15
    //2 37.5 - 20 = 17,5
    //1 38,75 - 20 = 18,75
    //0 19.375
}