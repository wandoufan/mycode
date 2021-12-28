# 基于python实现的Qt

## 基本情况
Qt框架支持两种编程语言：C++和Python


## 使用Python版的Qt
使用同一个版本的Qt creator，不用专门下载
创建项目时，选择Application(Qt for Python)即可

除了需要安装Python编译器外，还需要安装Python language server(PyLS)
PyLS不需要自己下载，在运行python版的Qt项目时，Qt creator会给出提示，并请求下载




## C++和Python实现Qt的比较
1. 一个最简单的带有UI界面的Qt项目
C++需要四个文件：main.cpp、mainwindow.h、mainwindow.cpp、mainwindow.ui
python只需要两个个文件：main.py、form.ui



## C++与python混合编程
在Qt中使用C++来调用Python接口
