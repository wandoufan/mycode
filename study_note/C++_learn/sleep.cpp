# include <iostream>
# include <windows.h>
using namespace std;


/*
C和C++中可以通过windows中的Sleep()函数实现程序挂起
注意：函数名S是大写
*/

int main()
{
	cout << "begin!" << endl;
	Sleep(5000); //单位是毫秒
	cout << "finish!" << endl;
}