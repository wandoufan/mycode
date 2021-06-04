# Qt项目中的.h.in文件

## 描述
在对Qt项目直接release编译时，报错：error: C1083: Cannot open include file: 'app/app_version.h'  
在对应目录下没有找到该头文件，只有一个同名的.h.in文件，即'app_version.h.in'  

## 基本功能
.h.in文件是一个模板文件，它是在cmake或者automake的过程中产生的一个用于输入设置信息等功能的中间文件  
它会在你调用confing、automake等.sh文件之后，自动生成一个相应的.h文件，然后就可以在源码中调用  
一般情况下，如果遇到这个问题，只要把源码下载，并按照官方的automake/autoconf规范执行一次，就可以得到该文件对应的.h文件了，就可以拷贝给QT载入用了  
备注：实际上还是不知道怎么去运行项目  

