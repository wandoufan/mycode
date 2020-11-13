# 条件编译

## 预处理命令
为了提高编程效率，C/C++在编译之前增加了预处理步骤，主要包括：  
1. 宏定义命令
2. 文件包含命令
3. 条件编译命令
为了和一般的C/C++语句区别，预处理命令都以符号'#'开头  


## 基本概念
有时候我们需要程序按照一定条件去编译源文件的不同部分，这就是条件编译  
可以使同一个源程序在不同的编译条件下得到不同的目标代码  


## 常用命令
1. #if			编译预处理中的条件命令，相当于C语法中的if语句
2. #ifdef		判断某个宏是否被定义，若已定义，执行随后的语句
3. #ifndef		与#ifdef相反，判断某个宏是否未被定义
4. #elif	若#if,#ifdef,#ifndef或前面的#elif条件不满足，则执行#elif之后的语句，相当于C语法中的else-if
5. #else	与#if,#ifdef,#ifndef对应,若这些条件不满足，则执行#else之后的语句，相当于C语法中的else
6. #endif		#if, #ifdef, #ifndef这些条件命令的结束标志
7. defined		与#if, #elif配合使用，判断某个宏是否被定义
8. #define 定义一个预处理宏
9. #undef 取消宏的定义


## 常用形式
1. ifdef
```
#ifdef 标识符
    程序段1
#else
    程序段2
#endif
```
2. ifndef
```
#ifndef 标识符
　　程序段1
#else
　　程序段2
#endif
```
3. elif
```
#if 条件表达式1
    程序段 1
#elif 条件表达式2
    程序段 2
#else
    程序段3
#endif
```


## pragma once
1. 只要在头文件的最开始加入'#pragma once'这条预处理指令，就能够保证头文件只被编译一次  
2. 由于编译器每次都需要打开头文件才能判定是否有重复定义，因此在编译大型项目时，ifndef会使得编译时间相对较长，因此一些编译器逐渐开始支持'#pragma once'的方式  
3. pragma once方式却不受一些较老版本的编译器支持，所以它的兼容性可能不够好  
备注：一般尽量选择ifdef的方式  


