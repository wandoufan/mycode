# 编译器

## 编译器的主要工作流程
```
源程序（source code）→ 
预处理器（preprocessor）→ 
编译器（compiler）→ 
汇编程序（assembler）→ 
目标程序（object code）→ 
连接器（链接器，Linker）→ 
可执行程序（executables）
```

## gcc
gcc(GUN compiler collection)，即GUN编译套件，用来进行C/C++的编译  
gcc编译器是Linux系统下最常用的C/C++编译器，大部分Linux发行版都会默认安装  
gcc编译器在shell中通过'gcc'命令来调用，命令包括很多选项  
参考资料：
> http://c.biancheng.net/gcc/


## GUN
GUN是运行在Liunx/Unix系统下的工具包，一般位于/usr/bin/目录下，常见包括：  
1. gcc GUN提供的C语言编译器  
2. g++ GUN提供的C++语言编译器  
3. ld GUN链接器，将目标文件和库文件链接起来，创建可执行程序和动态链接库  
4. ar 用来生成静态库文件.a，可以编辑和管理静态链接库  
5. make 生成器，根据makefile文件自动编译链接生成可执行程序或库文件  
6. gdb 调试器，用于调试可执行程序  
7. ldd 查看可执行文件依赖的动态链接库  


## MinGW
为了在Windows系统下也可以使用GUN工具，就产生了MinGW(Minimalist GUN for Windows)  
利用MinGW就可以生成Windows里面的exe程序和dll链接库  
MinGW本身主要就是编译链接等工具和头文件、库文件，并不包含系统管理、文件操作之类的Shell环境  
MinGW原本是用于生成32位程序的，随着64位系统流行起来，从MinGW分离出来了MinGW-w64  
MinGW-w64项目同时支持生成64位和32位程序  


## GUN和MinGW的区别
1. MinGW 里面工具带有扩展名 .exe， Linux/Unix 系统里工具通常都是没有扩展名的
2. MinGW 里面的生成器文件名为 mingw32-make.exe，Linux/Unix 系统里就叫 make
3. MinGW 在链接时是链接到 *.a 库引用文件，生成的可执行程序运行时依赖 *.dll  
而 Linux/Unix 系统里链接时和运行时都是使用 /*.so  


## MSYS(Minimal SYStem)
为了解决MinGW在windows环境下不能提供shell环境的问题， MinGW官方又推出了MSYS  
MSYS相当于是一个部署在Windows系统里面的小型Unix系统环境  
通过MSYS，我们可以直接在Windows系统下运行很多Linux命令行，有点类似git-bash  
对于MinGW-w64项目，它对应的小型系统环境叫MSYS2（Minimal SYStem 2）  


## Makefile文件
1. 文件作用
一个工程中的源文件不计其数，其按类型、功能、模块分别放在若干个目录中  
makefile就像一个Shell脚本一样，指定了具体的编译过程，实现整个项目的自动化编译，极大提高了效率  
2. 文件内容
Makefile文件描述了整个工程的编译、连接等规则，包括：  
指定哪些文件需要先编译，哪些文件需要后编译，哪些文件需要重新编译  
需要创建哪些库文件以及如何创建这些库文件  
如何最后产生我们想要的可执行文件等等  
3. make工具
make工具是用来执行Makefile文件的命令工具，主流的IDE都提供该命令  
比如：Delphi的make，Visual C++的nmake，Linux下GNU的make  
4. 具体说明
Makefile有自己的书写格式、关键字、函数  
备注：在Qt中，Makefile文件是由qmake工具根据.pro文件自动生成的，用户只需要编写.pro文件即可  