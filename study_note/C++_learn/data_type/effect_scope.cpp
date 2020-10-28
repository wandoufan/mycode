# include <iostream>
using namespace std;

int i = 10;  //最外层A
int main()
{
	int i = 20;  //中间层B
	{
		int i = 5;  //最内侧C
		int j;
		::i = ::i + 1;  //注意这里的::i是A层中的i，不是B层中的i
		j = ::i + i;
		cout << ::i << "   " << j << endl;  //11   16
	}
	cout << ::i << "   " << i << endl;  //11   20
	return 0;
}