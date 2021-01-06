# QT中的.pro文件

## 基本功能
.pro文件是项目的管理文件，文件名就是项目名，相当于配置文件  
主要用于记录项目的一些设置，以及项目包含文件的组织管理  
当项目中要用到一些非标准库时，要在.pro文件中进行声明，例如：'QT += axcontainer'  
当项目增删文件时，.pro文件会自动更新，不需要手动修改  
注意：实际使用发现删除QT项目中的文件夹没反应，必须到.pro文件中将该文件注释掉  
例如，向QT项目目录中拷贝了一个cpp文件和一个头文件，但QT中打开项目始终显示不出来，需要在.pro文件手动加上这两个文件的声明  

## 文件内容
1. TEMPLATE = lib
如果加上这个，程序运行时可能会报错：
```
error: You need to set an executable in the custom run configuration.
```
但会在编译目录下生成dll文件

The TEMPLATE variable's value makes qmake create the custom widget as a library