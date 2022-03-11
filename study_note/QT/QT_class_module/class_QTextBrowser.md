# QTextBrowser

## 基本功能
QTextBrowser提供了一个富文本浏览器，可以用来显示各种文本信息  
QTextBrowser控件一般只用来显示，不作为输入窗口，相当于只读版的QTextEdit  
父类：QTextEdit  
备注：.pro文件中要声明'QT += widgets'


## 构造函数
1. QTextBrowser::QTextBrowser(QWidget \*parent = nullptr)


## 常用公共函数
常用的setText()、append()、clear()等方法都来自于父类QTextEdit  