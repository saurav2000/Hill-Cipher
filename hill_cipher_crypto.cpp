#include <iostream>
#include <string>

#define N 26

using namespace std;

int k;

bool verify(string s)
{
	for(int i=0;i<s.length();++i)
	{
		if(s[i]>122 || s[i]<97)
			return true;
	}
	return false;
}

int determinant(int **m, )
{
	return 0;
}

// bool inverse()

int extendedEuclid(int a, int b, int &x, int &y)
{
	if(!a)
	{
		x = 0;
		y = 1;
		return b;
	}

	int x_,y_;
	int g = extendedEuclid(b%a, a, x_, y_);

	x = y_ - (b/a)*x_;
	y = x_;

	return g;
}

int main()
{
	cout<<"Enter the key size: \n";
	cin>>k;
	cout<<"Enter the key: \n";

	int **key = (int**)malloc(sizeof(int*) * k);
	for(int i=0;i<k;++i)
		key[i] = (int*)malloc(sizeof(int) * k);
	string text;
	determinant(key);
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

	if(text.length()%k!=0)
	{
		for(int i=0;i<k-(text.length()%k);++i)
			text+= "x";
	}

	string encrypted = "";
	for(int i=0;i*k<text.length();i+=1)
	{
		for(int l=0;l<k;++l)
		{
			int sum = 0;
			for(int m=0;m<k;++m)
				sum+= key[l][m]*(text[i*k+m]-97);
			encrypted+= ((char)((sum%N)+97));
		}
	}

	cout<<text<<"\n\n";
	cout<<encrypted<<"\n";

}
