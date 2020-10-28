# include <stdio.h>
# include <iostream>
# include <list>
using namespace std;

/*C++中的list*/

/*
vector、list、三种容器类型的比较
备注：在数据结构中list仅是一种逻辑结构，具体存储方式既可以是顺序存储也可以是链式存储  
此处的list采用链式存储可能是C++中的规定？
1. vector使用顺序存储，即使用一整块存储空间，支持[]操作符
vector可以高效的进行随机存取，但插入和删除的效率较低
2. list使用链式存储，即使用指针来利用零碎的内存空间，不支持[]操作符
list可以高效的进行插入和删除，但随机存取的效率较低
3. deque支持[]操作符
deque可以高效的进行随机存取，并且可以在两端高效的进行插入和删除
*/

/*
1. C语言中有list么，还是只有数组
2. list的元素支持的数据类型有哪些
3. 使用list之前要在开头进行声明'# include <list>'
4. 注意：C++中list和QT中QList的各种函数并不相同，不能直接套用
5. list不能直接用cout输出，只能逐个元素的去输出
6.
*/


void test1()
{
	list<int> list_num;
	int i;
	for (i = 0; i < 10; i++)
	{
	    list_num.push_back(i + 1);
	}
	cout << list_num.size() << endl;
	// for (int j = 0; j < list_num.size(); j++)
	// {
	// 	cout << list_num[j] << endl;
	// }
	// cout << list_num[1] << endl;
}

int main()
{
	test1();
	return 0;
}