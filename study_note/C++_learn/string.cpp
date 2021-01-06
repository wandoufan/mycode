#include <iostream>
#include <string>
using namespace std;


/*
C语言中用字符数组来实现字符串的功能，需要提前定义数组长度，很不方便  
C++虽然继承了C语言中的字符数组，但一般不再使用，而是用C++标准库中的string类  
注意：这里的string是一个类，每次使用字符串都相当于实例化了一个对象  
在使用string类之前要#include <string>  
*/


void string_init()
{
	/*
	字符串初始化相关的操作
	*/
	string s1(); //空字符串
	string s2("hello, world"); //使用构造函数来初始化赋值
	string s3 = "hello, world";
	string s4 = s3; //字符串可以直接用'='来赋值
	string s5(3, 'a'); //将字符'a'重复3次的字符串"aaa"
	//第一参数表示重复次数，第二个参数必须是字符，不能是字符串
	string s6;
	s6 = 'k'; //字符串对象可以赋值单个字符，但不能在初始化时赋值单个字符
	//错误写法1：string s6 = 'k';
	//错误写法2：string s6('k');
	string s7("12345678", 2, 4); //从第2个下标开始，长度为4的子串，即"3456"
	//第一个参数表示子串的起始索引位置，第二个参数表示子串的长度
	string s8 = s4 + "  " + s5; //字符串之间可以直接相加
	s8 += "bbb"; //字符串之间可以用'+='来实现尾部追加字符串的效果
	cout << s8 << endl;
}


void string_function()
{
	/*
	string类提供的常用成员函数
	*/
	string s1, s2, s3;
	//1. assign函数用来对字符串对象赋值
	s1.assign("12345678");
	s2.assign(s1, 2, 4);
	s3.assign(3, 'a');
	//2. length和size函数返回字符串的长度
	int string_len1 = s1.length();
	int string_len2 = s1.size();
	//3. append函数在字符串尾部添加字符串
	s1.append(s2);
	s1.append(s2, 2, 2);
	s1.append(3, 'b');
	//4. compare函数用来比较字符串的大小，返回-1、0、1分别代表小于、等于、大于
	string s4("abcdef"), s5("abdcef"), s6("abcdef");
	int compare_result;
	compare_result = s4.compare(s5);
	compare_result = s4.compare(s6);
	compare_result = s4.compare("ababef");
	compare_result = s4.compare(1, 3, s5, 1, 3); //s4的子串和s5的子串比较
	compare_result = s4.compare(1, 3, s5); //s4的子串和s5比较
	//5. substr函数用来获取字符串的子串
	//string substr(int n = 0, int m = string::npos) const;
	//第一个参数代表子串的起始索引位置，第二个参数代表子串的长度
	s2 = s1.substr(3, 4);
	s2 = s1.substr(3);//第二个参数可以省略，长度一直到字符串的末尾
	//6. swap函数用来交换两个字符串的内容
	s2.swap(s3);
	// cout << s2 << "   " << s3 << endl;
}

void string_visit()
{
	string s1("123456789");
	for(int i = 0; i < s1.size(); i++)
	{
		cout << s1[i] << endl; //可以根据索引位置逐个访问字符
	}
}

void string_modify()
{
	/*
	string类中与修改相关的成员函数
	*/
	string s1("123456789");
	s1[5] = '5'; //可以修改字符串中的字符
	cout << s1 << endl;
}

void string_find()
{
	/*
	string类中与查找相关的成员函数
	*/
	string s1("123456789"), s2("345"), s3("456");
	int index;
	//1. find函数从前向后查找并返回子串或字符的出现位置
	//如果没有查找到就返回-1
	index = s1.find(s2);
	index = s1.find('3');
	index = s1.find('0');
	cout << index << endl;

}


int main()
{
	// string_init();
	// string_function();
	// string_visit();
	// string_modify();
	string_find();
	return 0;
}