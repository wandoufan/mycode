# QT中的.pro文件

## 基本功能
.pro文件是项目的管理文件，文件名就是项目名，相当于配置文件  
主要用于记录项目的一些设置，以及项目包含文件的组织管理  
.pro文件是用qmake语法编写的，会被qmake用于生成包含构建过程中所需的所有命令的MakeFile  
备注：具体内容详见Qt帮助手册'qmake Manual'  


## 在Qt项目中导入其他项目/代码的方法
1. 如果子项目有.pri文件，直接include子项目的.pri文件
```
include(../SkyplotWidget.pri)
include(xlsx/qtxlsx.pri)
```
2. 如果没有.pri文件，就要把头文件和源文件逐个添加进来
```
HEADERS += \
    snap7/snap7.h \
    snap7/s7_client.h \
    ......

SOURCES += \
    snap7/snap7.cpp \
    snap7/s7_client.cpp \
    ......
```


## qmake变量
备注：所有变量详见Qt帮助手册'Variables'  
注意：路径中使用的都是反斜杠/  
* TEMPLATE
TEMPLATE变量指定工程类型  
```
TEMPLATE = lib //编译成library，qmake会在编译目录下生成dll文件
TEMPLATE = app //表示项目使用的模板是app，是一般的应用程序
TEMPLATE = subdirs //生成makefile文件编译subdirs指定的子文件夹，即主项目下包含子项目
```
* SUBDIRS
SUBDIRS变量指定子项目所在的路径  
```
SUBDIRS += src/src.pro        \
           plugin/plugin.pro  \
           example/example.pro
```
* DEFINES
DEFINES变量指定预定义预处理器符号(宏)  
```
DEFINES  = SKYPLOTWIDGET_STATIC
```
* LIBS
LIBS变量指定工程要链接的库  
可以指向库文件，可以指向库文件所在的目录  
```
LIBS += -L.
LIBS += $$PWD/lib/custombuttonplugin.lib
LIBS += -L$$PWD/snap7/ -lsnap7
```
* QT
QT变量指定要使用的QT模块  
```
QT  += core gui //默认变量，对应于QtCore和QtGui，带界面的程序都要用到该模块
QT  += axcontainer //使用QAxContainer模块中相关的类
QT  += widgets //使用各种widget组件
QT += charts //用到Qt的charts模块
```
* CONFIG
CONFIG变量指定指定工程配置和编译变量  
注意：CONFIG变量的值会被qmake内部识别并有特殊的意义  
```
CONFIG += qt //默认变量，指应用程序使用QT
CONFIG += c++11 //使用c++11
CONFIG += debug //编译出具有调试信息的可执行程序
CONFIG += release //编译不带调试信息的可执行程序，与debug同时存在时，release失效
CONFIG += no_debug_release //不会生成debug和release目录
CONFIG += dll //动态编译库文件
CONFIG += staticlib //静态编译库文件
CONFIG += console //指应用程序需要写控制台
CONFIG += plugin //编译一个插件
CONFIG += no_keywords //禁用关键字的宏
```
* INCLUDEPATH
INCLUDEPATH变量指定C++编译器搜索头文件路径  
```
INCLUDEPATH = ../include
INCLUDEPATH += $$PWD/dll
```
* DEPENDPATH
DEPENDPATH变量指定依赖文件路径  
```
DEPENDPATH = ../include ../src
```
* HEADERS
HEADERS添加头文件  
```
HEADERS = custombuttonplugin.h
```
* SOURCES
SOURCES添加源文件  
```
SOURCES = custombuttonplugin.cpp
```
* RESOURCES
RESOURCES添加需要rcc处理的.qrc文件  
```
RESOURCES = icons.qrc
```
* FORMS
FORMS添加.ui文件  
```
FORMS = cardreader.ui
```
* VERSION
VERSION指定目标库版本号  
```
VERSION = 2.0.1
```
* TARGET
TARGET指定可执行程序的名字，如果不设置，程序名默认设为项目名  
备注：这里设置的是将来生成的exe文件的名字  
```
TARGET = skyplotwidgetdesigner
```
* DLLDESTDIR
DLLDESTDIR指定去哪个路径下拷贝dll文件  
备注：这个变量只有在windows系统下有效  
* RC_ICONS
项目编译后会生成exe文件，可以通过RC_ICONS变量为程序设置自定义的图标  
备注：图标文件必须先转换为.ico格式  
```
RC_ICONS = spinbox.ico
```
* 自定义变量
除了上述变量外，还可以根据需要去自定义变量  
```
MY_VARIABLE = value
```


## 一些指定生成文件路径的qmake变量
* DESTDIR
DESTDIR指定可执行文件或库文件最终的生成路径  
```
DESTDIR = ../../lib
```
* OBJECTS_DIR
OBJECTS_DIR指定.obj文件和.res文件的生成路径  
```
OBJECTS_DIR = $$PWD/./temp/obj
```
* MOC_DIR
MOC_DIR指定.h文件和.cpp文件的生成路径  
```
MOC_DIR = $$PWD/./temp/moc
```
* RCC_DIR
RCC_DIR指定rcc资源文件的生成路径  
```
RCC_DIR = $$PWD/./temp/rcc
```
* UI_DIR
UI_DIR指定ui_xxx.h文件的生成路径  
```
UI_DIR = $$PWD/./temp/ui
```


## qmake语法
备注：所有语法详见Qt帮助手册'qmake Language'  
1. +=
添加多个文件时用'+='，多个文件之间用'\'进行分开  
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
也可以变量后面直接添加多个值，多个值之间用空格分开  
```
QT += designer widgets gui
```
2. -=
变量列表中删除某个值  
```
CONFIG -= warn_off
```
3. \*=
只有当变量列表中不存在该值时，才向变量列表中添加该值  
相比于+=，可以避免重复添加变量值  
```
DEFINES *= USE_MY_STUFF
```
4. \~=
替换变量列表中符合正则表达式的某个值  
```
//将变量列表中所有以QT_D和QT_T开头的值都用QT替换掉
DEFINES ~= s/QT_[DT].+/QT
```
5. $$
$$操作符可以用来抽取出变量中的值，然后将值传递给其他变量  
```
//把SOURCES变量和HEADERS变量的值都抽取出来，并一起赋值给EVERYTHING变量
EVERYTHING = $$SOURCES $$HEADERS
message("The project contains the following files:")
message($$EVERYTHING)
```
如果要输出变量中的值，要在变量名前加上$$，否则输出的是字符串格式的变量名  
```
NAME = "zhang"
message(NAME) //输出NAME
message($$NAME) //输出zhang
```
也可以使用$${}操作符读取变量的值，以下两行效果相同  
```
MY_DEFINES = $$DEFINES
MY_DEFINES = $${DEFINES}
```
还可以把抽取出来的值作为参数传递给某个函数  
```
min = $$2
greaterThan(QT_MINOR_VERSION, $$min)
{
	return(true)
}
```
如果要在qmake运行时获取到一个环境变量的值，使用$$()操作符  
```
//当处理项目文件时可以立刻读到PWD的值
DESTDIR = $$(PWD)
message(The project will be installed in $$DESTDIR)
```
如果要在生成makefile文件后获取到一个环境变量的值，使用$()操作符  
```
//当产生makefile文件时可以读到PWD的值
DESTDIR = $(PWD)
message(The project will be installed in the value of PWD)
message(when the Makefile is processed.)
```
如果要访问qmake的各种属性，使用$$[]操作符  
```
message(Qt version: $$[QT_VERSION])
message(Qt is installed in $$[QT_INSTALL_PREFIX])
message(Qt resources can be found in the following locations:)
message(Documentation: $$[QT_INSTALL_DOCS])
message(Header files: $$[QT_INSTALL_HEADERS])
message(Libraries: $$[QT_INSTALL_LIBS])
message(Binary files (executables): $$[QT_INSTALL_BINS])
message(Plugins: $$[QT_INSTALL_PLUGINS])
message(Data files: $$[QT_INSTALL_DATA])
message(Translation files: $$[QT_INSTALL_TRANSLATIONS])
message(Settings: $$[QT_INSTALL_CONFIGURATION])
message(Examples: $$[QT_INSTALL_EXAMPLES])
```
6. #
句子前面加#表示注释掉  
```
#TEMPLATE = app
```
7. 作用域和条件
当条件为真时，执行下面的作用域  
常用来进行构建跨平台的项目，在不同的平台上执行不同的操作  
```
win32
{
	SOURCES += paintwidget_win.cpp
}
unix
{
	SOURCES += paintwidget_unix.cpp
}
macx
{
	SOURCES += paintwidget_macx.cpp
}
```
当执行的操作语句比较少时，也可以写成以下格式  
```
win32:SOURCES += paintwidget_win.cpp
unix:SOURCES += paintwidget_unix.cpp
macx:SOURCES += paintwidget_macx.cpp
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
2. 条件执行语句
当Qt主版本大于4时，才加入widgets模块  
```
greaterThan(Qt_MAJOR_VERSION, 4): Qt += widgets
```
3. include()函数可以实现配置文件之间的包含
包含了另一个配置文件，就相当于添加了这个配置文件中的所有内容  
```
include(../SkyplotWidget.pri)
include(xlsx/qtxlsx.pri)
```
4. message()函数中的信息可以输出在'编译输出'和'概要信息'的窗口中  
```
message("this is a message test")
```
如果要输出变量中的值，要在变量名前加上$$，否则输出的是字符串格式的变量名  
```
NAME = "zhang"
message(NAME) //输出NAME
message($$NAME) //输出zhang
```
