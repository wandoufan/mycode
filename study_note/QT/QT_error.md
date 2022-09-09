# QT程序中的报错


## LNK2019: 无法解析的外部符号
这个是Qt项目中最常见的报错之一，可能的原因有很多  
注意：尝试对报错进行修复之后，要先把产生的debug或release目录删除之后再重新运行  

1. 类内使用了信号与槽，但未包含Q_OBJECT宏，因此需在类内加上Q_OBJECT

2. 添加新的.ui窗体文件时编译器没有为它生成新的.obj文件而报错
先重新执行qmake，再运行项目

3. 项目没有包含需要的QT模块，需要在.pro文件中添加对应的模块

4. 头文件中声明了slot槽函数，但在源文件中没有进行具体的定义实现

5. 项目中引用了lib库，这个lib库是32位的，但项目编译的时候用的是64位的编译配置

6. 项目中引用了库文件，但没有在.pro文件中正确地包含库文件


## LNK1123: 转换到 COFF 期间失败: 文件无效或损坏
1. 环境描述
使用Qt 5.2.1 + VS 2010环境
创建一个最简单的项目，以debug模式运行时就会产生如上报错，以release模型运行则没有问题
2. 解决办法
在C盘的Windows目录中搜索cvtres.exe，可以找到多个结果
```
C:\Windows\Microsoft.NET\Framework\v4.0.30319
...
```
在VS的目录中也有一个cvtres.exe
```
C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin
```
Windows目录中的cvtres.exe时间日期比VS目录中的cvtres.exe更新
用Windows目录中的cvtres.exe替换VS目录中的cvtres.exe即可
