# C++命名规范
备注：命名规范没有统一的标准  

## 变量
1. 本地变量
变量名一律小写，多个单词间可以以下划线连接  
```
int data_size;
```
2. 类中的成员变量
类中的成员变量一般以'm_'开头，即member  
```
int m_count;
```
另外，也有的写法是在变量名最后再加上一个下划线来表示类中的成员变量
```
int data_size_;
```
3. 全局变量
全局变量一般以'g_'开头，即golbal  
```
int g_count;
```
4. 静态变量
静态变量一般以's_'开头，即static  
```
int s_count;
```

## 函数
1. 普通函数以及Public成员函数
采用驼峰命名法，每个单词的首字母大写，中间不包含下划线  
其中，存取变量的函数名称要和变量名称一致  
```
int GetIndex();
bool SetIndex(int index);
```
另外，也可以采取完全小写的名称，单词中间用下划线隔开  
```
int get_index();
bool set_index(int index);
```
2. protect成员函数
保护成员函数的开头应该加上一个下划线进行区别  
```
bool _SetState();
```
3. private成员函数
私有成员函数的开头应该加上两个下划线进行区别  
```
bool __DestroyImp();
```
4. 虚函数
虚函数一般以'Do'进行开头  
```
bool DoRefresh();
bool _DoEncryption();
```

## 类/结构体
采用驼峰命名法，每个单词的首字母大写，中间不包含下划线  
```
class StudengtInfo {};
```

## 命名空间
命名空间的名字每个字母都用小写  
备注：实际代码中的命名空间也经常使用驼峰命名法  
```
namespace space_name{
	// 各种代码声明
	variables;
	functions;
	classes;
}
```

## 宏
宏的名字中每个字母都要用大写，中间加上下划线  
```
Q_OBJECT
```