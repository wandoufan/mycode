# 头文件(header file)

## 基本概念
在代码的开头一般都有如'#include <stdio.h>'这样的文件，称为头文件(header file)  
头文件都使用#include命令包含在代码的最开头，一般都以.h作为文件后缀  
头文件不仅可以使用编译器自带的头文件，还可以自己进行编写定义  

## 语法
引用头文件的语法有两种：  
1. #include <stdio.h>
2. #include "stdio.h"

## 头文件的作用
头文件中包含了很多的函数声明和宏定义，可以被源文件们引用共享，在源文件中实现相应的功能  
例如，printf函数其实并不是C/C++内置的库函数  如果没有声明stdio.h文件，编译时虽然能够通过但会警告printf函数未定义  
备注：直接把头文件的内容拷贝到源文件中就相当于在源文件中引用头文件，但不建议这么操作  

## 编程语言
注意：不是所有编程语言都支持使用头文件  
1. 使用头文件的编程语言：
C、C++、object C  
2. 不使用头文件的编程语言：
python、ruby、C#、Java  
备注：python中的import库有点类似于头文件  

## 常用头文件的功能
每个头文件都支持一组特定的功能，常用的头文件包括：  
1. stdio.h
提供标准的输入输出功能，例如printf函数  
2. math.h
提供数学运算等功能，例如pow函数  
3. string.h
提供字符串运算等功能，例如strcmp函数  