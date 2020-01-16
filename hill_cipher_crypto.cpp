#include <iostream>
#include <string>

#define N 26

using namespace std;

bool verify(string s)
{
	for(int i=0;i<s.length();++i)
	{
		if(s[i]>122 || s[i]<97)
			return true;
	}
	return false;
}



int main()
{
	int k;
	cout<<"Enter the key size: \n";
	cin>>k;
	cout<<"Enter the key: \n";

	int key[k][k];
	string text;

	for(int i=0;i<k;++i)
		for(int j=0;j<k;++j)
			cin>>key[i][j];

	cout<<"Enter the text\n";
	bool flag = true;
	while(flag)
	{
		cin>>text;
		flag = verify(text); 
	}



}
