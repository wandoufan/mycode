# QT中的.pro文件

## 基本功能
.pro文件是项目的管理文件，文件名就是项目名，相当于配置文件  
主要用于记录项目的一些设置，以及项目包含文件的组织管理  


## 文件内容
* TEMPLATE
TEMPLATE参数指定工程类型  
```
TEMPLATE = lib //编译成library，qmake会在编译目录下生成dll文件
TEMPLATE = app //表示项目使用的模板是app，是一般的应用程序
TEMPLATE = subdirs //生成makefile文件编译subdirs指定的子文件夹，即主项目下包含子项目
```
* SUBDIRS
SUBDIRS参数指定子项目所在的路径  
```
SUBDIRS += src/src.pro        \
           plugin/plugin.pro  \
           example/example.pro
```
* DEFINES
DEFINES参数指定预定义预处理器符号(宏)  
```
DEFINES  = SKYPLOTWIDGET_STATIC
```
* LIBS
LIBS参数指定工程要链接的库  
```
LIBS += -L.
LIBS += $$PWD/lib/custombuttonplugin.lib
```
* QT
QT参数指定要使用的QT模块  
```
QT  += core gui //默认参数，对应于QtCore和QtGui，带界面的程序都要用到该模块
QT  += axcontainer //使用QAxContainer模块中相关的类
```
* CONFIG
CONFIG参数指定指定工程配置和编译参数  
```
CONFIG += qt //默认参数，指应用程序使用QT
CONFIG += c++11 //使用c++11
CONFIG += debug //编译出具有调试信息的可执行程序
CONFIG += release //编译不带调试信息的可执行程序，与debug同时存在时，release失效
CONFIG += dll //动态编译库文件
CONFIG += staticlib //静态编译库文件
CONFIG += console //指应用程序需要写控制台
CONFIG += plugi //编译一个插件
```
* INCLUDEPATH
INCLUDEPATH参数指定C++编译器搜索头文件路径  
```
INCLUDEPATH   = ../include
```
* DEPENDPATH
DEPENDPATH参数指定依赖文件路径  
```
DEPENDPATH   = ../include ../src
```
* HEADERS
HEADERS添加头文件  
```
HEADERS   = custombuttonplugin.h
```
* SOURCES
SOURCES添加源文件  
```
SOURCES   = custombuttonplugin.cpp
```
* RESOURCES
RESOURCES添加需要rcc处理的.qrc文件  
```
RESOURCES   = icons.qrc
```
* FORMS
FORMS添加.ui文件  
```
FORMS  = cardreader.ui
```
* VERSION
VERSION指定目标库版本号  
```
VERSION = 2.0.1
```
* TARGET
TARGET指定可执行文件名，如果不设置，程序名自动设为项目名  
```
TARGET  = skyplotwidgetdesigner
```


## 使用技巧
1. 指定添加文件的路径
如果想要添加当前路径(.pro所在目录)的上一层路径的文件，可以用'..'表示  
```
SOURCES += ../test.cpp
```
可以用'$$PWD'表示当前工作路径  
```
INCLUDEPATH += $$PWD/include
```
2. 添加多个文件时用'+='，多个文件之间用'\'进行分开
```
SOURCES += \
    main.cpp \
    cardreader.cpp \
    user_management.cpp
```
也可以第一个写成'='，后面的写成'+='  
```
SOURCES = main.cpp
SOURCES += cardreader.cpp
SOURCES += user_management.cpp
```
也可以参数后面直接添加多个值，多个值之间用空格分开  
```
QT += designer widgets gui
```
3. 条件执行语句
当Qt主版本大于4时，才加入widgets模块  
```
greaterThan(Qt_MAJOR_VERSION, 4): Qt += widgets
```
4. 删除某个设置
```
CONFIG -= warn_off
```
5. 配置文件之间可以相互包含
包含了另一个配置文件，就相当于添加了这个配置文件中的所有内容  
```
include(../SkyplotWidget.pri)
```