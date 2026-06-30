#include <bits/stdc++.h>
using namespace std;

int conv(string str){
    int ans=0, mult=1, i= 3;
    while(i>=0){
        ans += (str[i]-'0') *mult;
        mult*=10;
        i--;
    }
    return ans;
}

string conv2(int n){
    string ans;

    while(n){
        ans += n%10+'0';
        n/=10;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

string put0(string str){

    reverse(str.begin(), str.end());
    string ans="0000";
    for(int i=0; i<str.size(); i++){
        ans[3-i] = str[i];
    }
    return ans;
}

int main(){
    string num;
    cin>>num;

    cout<<num<<"\n";

    vector<int> vet;
    vet.push_back(conv(num));

    while(1){

        num = put0(num);
        string ord = num;
        sort(ord.begin(), ord.end());

        string rev = ord;
        reverse(rev.begin(), rev.end());

        int ans = conv(rev) - conv(ord);

        if(find(vet.begin(), vet.end(), ans) != vet.end()){
            return 0;
        }
        cout<<ans<<"\n";
        num = conv2(ans);
        vet.push_back(ans);
    }

}