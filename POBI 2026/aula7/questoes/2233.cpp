#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;

	cin>>n;

	string eng, ptbr;
	map<string, string> dic;

	for (int i=0; i<n; i++){
		cin>>eng>>ptbr;

		dic[eng] = ptbr;
	}

	cin.ignore();


	string sentence;
	getline(cin, sentence);
    
	istringstream iss(sentence);
	vector<string> words((istream_iterator<string>(iss)), istream_iterator<string>());

	for (string word : words){
		cout<<dic[word]<<" ";
	}

	cout<<endl;
	return 0;
}
