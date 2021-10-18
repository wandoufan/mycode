# include <stdio.h>
# include <iostream>
using namespace std;

template <typename T, int size>//声明一个模板
class ClassTemplate //类模板
{
public:
	void SetArray(int index, T value)
	{
		m_array[index] = value;
	}

	void PrintArray()
	{
		for(int i = 0; i < size; i++)
		{
			cout << i << " : " << m_array[i] << endl;
		}
	}

private:
	T m_array[size];
};



int main()
{
	//模板类1

	ClassTemplate<int, 10> Class1;
	for(int i = 0; i < 10; i++)
	{
		
	}


	// const int a = 1;
	// const char b = 'a';
	// ClassTemplate<a, b> Class1(a, b);//模板类实例化
	// Class1.GetName();

	return 0;
}


