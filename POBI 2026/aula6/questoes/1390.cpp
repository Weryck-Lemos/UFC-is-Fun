#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    queue<int> q;
    stack<int> s;

    for(int i=0; i<n; i++) {
        int x;
        cin>>x;

        q.push(x);
        s.push(x);
    }

    while(!q.empty()) {
        cout << q.front();

        q.pop();

        if(!q.empty())
            cout<< " ";
    }

    cout<<"\n";

    while(!s.empty()) {
        cout << s.top();

        s.pop();

        if(!s.empty())
            cout << " ";
    }

    cout <<"\n";
}