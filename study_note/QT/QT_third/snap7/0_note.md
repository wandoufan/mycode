# snap7

## 基本功能
snap7是一个基于以太网与S7系列的西门子PLC通讯的开源库  
支持包括S7系列的S7-200、S7-200smart、S7-300、S7-400、S7-1200以及S7-1500的以太网通信  


## 自己下载的snap7源码的版本
V 1.4.2


## 关于snap7.h/cpp中的内容
备注：几个版本中snap7.h/cpp的内容并不完全相同
1. 定义了大量的snap7相关的宏、常量、用来存储数据的结构体
2. 定义了大量的S7API函数(以Cli_开头)，这些函数也分别对应下面3个类
建议直接用这些函数
3. 定义了3个类：TS7Client、TS7Server、TS7Partner
这些类实际上就把S7API函数又封装了一层，变成了class的形式


## 在Qt项目中显式调用snap7动态库
把包含snap7.h、snap7.dll、snap7.lib的snap7目录放到项目目录中
在.pro文件中添加库文件
```
INCLUDEPATH += $$PWD/snap7
DEPENDPATH += $$PWD/snap7

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/snap7/ -lsnap7
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/snap7/ -lsnap7
else:unix: LIBS += -L$$PWD/snap7/ -lsnap7
```


## 代码示例
```
#include "snap7/snap7.h"
S7Object plc_client;
plc_client = Cli_Create();
int result = Cli_ConnectTo(plc_client, address, plc_rack, plc_slot);
...
```

-------------使用方式一：调用动态库---------------

备注：目前实际使用的是王工写的ws8module中的32位库文件
注意：库文件分成32位和64位的，必须搞清楚用的是哪一版，并和自己的编译套件一致

## 遇到的问题
1. 编译过程中报错
自己在新环境(Qt5.15 + MSVC2015或Qt 5.11 + MinGW)下单独使用snap7库编译时是正常的
但是在老版edas环境下(Qt 5.2.1 + MSVC2010)下使用snap7库在编译时会有如下报错
```
C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\include\time.inl:36: error: C2664: '_ctime32' : cannot convert parameter 1 from 'const time_t *' to 'const __time32_t *'
Types pointed to are unrelated; conversion requires reinterpret_cast, C-style cast or function-style cast
```
经过排查，报错不是自己写的调用snap7相关的代码，而是来自于snap7.h本身
具体原因未知，可能跟C++版本有关，产生了一些兼容性问题
解决办法：
如果是自己在老版环境中单独使用snap7库，就在代码中添加如下宏定义
```
#define _USE_32BIT_TIME_T
```
如果是在edas中使用snap7库，就在.pro文件中添加如下定义
```
DEFINES += _USE_32BIT_TIME_T
```

-------------使用方式二：调用源代码---------------

## snap7项目中src目录解析
1. sys目录
文件名为snap_xxx.h/cpp，包括：
基类、套接字传输、线程、平台依赖文件等
2. core目录
包含所有snap7相关的文件，执行IsoTCP和S7协议
3. lib目录
包含用来创建库的接口文件
4. 使用说明
如果想要写一个多平台的网络数据包驱动程序，可以只用到sys目录
如果想要把snap7嵌入到自己的源代码中，把sys目录和core目录都包含进去


## 遇到的问题
1. 编译过程中报错
不管是用自己下载库中的snap7.h/cpp，还是用edas中的snap7.h/cpp
编译时有大量如下报错，暂时没找到原因，这种方式没有使用成功
```
QT LNK2019 未找到文件.obj
```


