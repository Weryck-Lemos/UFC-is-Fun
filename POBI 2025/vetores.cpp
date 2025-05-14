#include <iostream>
#include <vector>
#include <algorithm> //sort, reverse, find, lb, ub, count e remove
using namespace std;

int main(){
    vector<int> a = {5, 3, 9, 2, 2, 11, 3, 1, 3, 5};

/*
    cout<<a.front()<<" "<<a.back()<<"\n";
    a.pop_back();
    a.push_back(6);
    a.insert(a.end()-1, 60);
*/
/*
    a.clear();
    if(a.empty())cout<<"vazio\n";
*/
/*
    sort(a.begin(), a.end());
    sort(a.rbegin(), a.rend());

    reverse(a.begin(), a.end());
*/
/*
    int x=3;
    auto lb = lower_bound(a.begin(), a.end(), x);
    auto ub = upper_bound(a.begin(), a.end(), x);
    
    if(lb != a.end()){
        cout<<"esta no vetor\n";
        cout<<"lb: "<<*lb<<" "<<"ub: "<<*ub<<"\n";
        cout<<x<<" se repete: "<<ub-lb<<" vezes\n";
    }

    else{
        cout<<"nao esta no vetor\n";
    }
*/
/*
    auto it = find(a.begin(), a.end(), 100);
    if(it != a.end())cout<<"achei\n";
    else cout<<"nao achei\n";
*/
/*
    int tot = count(a.begin(), a.end(), 5);
    cout<<"aparece: "<<tot<<" vezes\n";
*/
    


    for(int i=0; i<a.size(); i++){
        cout<<a[i]<<" ";
    }
    cout<<"\n";
}