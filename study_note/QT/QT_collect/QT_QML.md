# Qt中的QML

## QML的概念
QML是Qt推出的Qt Quick技术的核心组件之一，是一种新增的简便易学的语言  
QML是一种陈述性语言，用来描述一个程序的用户界面：无论是什么样子，以及它如何表现  
QML是一种描述性的脚本语言，其文件格式以.qml结尾  
QML的语法格式类似于CSS，但又支持javascript形式的编程控制  


## 创建QML项目的方式
1. 通过与C++的交互进行创建
新建项目 - Application(Qt Quick) - 选择其中一种模板  
这种方式使用C++编程进行实现，更加简单  
2. 使用QML的方式进行创建
新建项目 - 其他项目 - QT Quick UI Prototype  
这种方式的UI界面会更加流畅美观，更适用于触屏的操作，但缺点是逻辑结构复杂  


## QML相关的Qt类
备注：总共大约有20个Qt类，详见Qt手册的目录中Qt QML的部分
1. QQmlNetworkAccessManagerFactory