# 关于C++的基础知识


## 基本概念
1. C++是由C语言发展而来，几乎完全兼容C语言，C代码几乎可以不加修改的用于C++  
2. C++编译器可以运行大部分C的代码，但C编译器不能运行C++的代码  
3. C++的标识符(包含变量名)只能由字母、数字、下划线组成，且首个字符必须是字母或下划线  
4. C++的编译系统都区分大小写，一般默认常量用名大写字母表示，变量名用小写字母表示   
5. 封装、继承和多态是面向对象的三大特征，这些特征都是通过类来实现的，因此类是C++中的核心  

## C++由3个部分组成
1. 核心语言，提供了所有构件块，包括变量、数据类型、常量等  
2. C++标准库，提供了很多类，每个类又包含很多函数，用于操作文件、字符串等  
> http://www.cplusplus.com
3. 标准模板库(STL)，提供了大量的方法，用于操作数据结构等

## C++源文件的后缀 
C语言源文件的后缀在不同的编译器下都是\*.c，而C++源文件在不同的编译器下支持不同的后缀  
1. Visual Studio(VS)：cpp、cxx、cc
2. GCC(GUN c++):cpp、cxx、cc、c++、C
3. Borland C++:cpp
一般推荐使用cpp作为c++文件的后缀  

## ANSI标准
ANSI标准是为了确保C++的跨平台性，编写的C++代码在Mac、UNIX、Windows计算机上都能通过编译  
由于ANSI标准已稳定使用了很长的时间，所有主要的C++编译器的制造商都支持ANSI标准  

## 两个类之间相互调用的问题
两个类不能互相包含头文件，否则会造成编译错误
在QT中可以用信号&槽机制实现两个类之间相互传输数据
在单纯的C++代码中可以使用信号量或消息队列来实现，具体实现方式待研究
