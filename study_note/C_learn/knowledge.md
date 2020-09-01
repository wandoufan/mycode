# 主要记录C语言的基础知识

## C程序的运行过程
编辑：用C语言编写一个源程序(.c文件)
编译：把源程序翻译成二进制形式的目标程序(.obj文件)
链接：将该目标程序与函数库以及其他目标程序链接为可执行文件(.exe)


## C语言中的数据类型
1. 基础类型：  
整型、字符型、实型  
2. 构造类型/导出类型：  
数组类型、结构体类型、共用体类型  


## 命名规则
C语言中的标识符(包含变量名)只能由字母、数字、下划线组成，且首个字符必须是字母或下划线  
C语言的编译系统都区分大小写，一般默认常量用名大写字母表示，变量名用小写字母表示  
C语言本身对标识符长度没有规定，但各个C编译系统都有自己的长度限制  


## C语言中双引号和单引号的区别
一般单引号表示单个字符，双引号表示字符串  
C语言中的字符常量是用单引号括起来的一个字符，如'a'，'D'，'?'，'$'等  
字符串常量用双引号括起来，如"I am happy"  


## 声明变量
不能在一个函数中声明两个名字相同的变量，即使不同类型的变量也不行，这一点与python不同  
因为在C语言中一个函数内属于同一作用域，只有不同作用域才可以使用相同名字的变量  
C语言中的变量使用前必须先声明，而且变量在声明后如果没有初始化，则变量的值是不可预料的  


## 输出数据
C语言中不能直接输出数组元素：printf(array[1])，必须用格式符来引用：printf("%d", array[1])  
这一点与python不同，python可以直接输出列表元素：print(list[1])  
C语言中不能直接输出一个变量：printf(i)，不管变量是int、char或其他类型，必须用格式符来引用：printf("%d", i)  
这一点与python不同，python可以直接通过变量名来输出一个变量：print(i)  


## 赋值表达式
由赋值运算符将一个变量和一个表达式连接起来的式子称为赋值表达式  
赋值表达式一般形式为"变量 赋值运算符 表达式"，例如a = 3  
左边只能是变量，不能是常量或其他表达式，右边的表达式应该由一个明确的值  
赋值表达式中的表达式又可以是另一个赋值表达式，例如a = (b = 5)，最后结果是a值为5  


## 逗号表达式


## 条件表达式
条件运算符也称为三元运算符，一般形式为 表达式1 ? 表达式2 : 表达式3  
C语言中的写法： max = (a > b)? a : b;
python中的写法： max = a if a > b else b



## 转移符
\n 换行，将当前位置移到下一行开头
\t 制表符，跳到下一个tab位置
\b 退格，将当前位置移到前一列
\r 回车，将当前位置移到本行开头
\f 换页，将当前位置移到下页开头
\\ 代表一个反斜杠
\' 代表一个单引号
\" 代表一个双引号


## 运算符的优先级
....  


## 表示空的关键字
C中以'NULL'表示空(注意是大写)，类似于python中的'None'  


## Status
'Status'常出现在C语言版的数据结构教材中，'Status'本身不是C语言中的关键字  
可以看做是一个重新声明的变量名，typedef int Status;  