# Qt项目中的xxx_global.h头文件

## 基本功能
在Qt项目中实现共享库文件的功能，可以自己生成一个dll文件  
Qt creator会自动生成一个和项目同名的{projectName}\_global.h文件  
因此当项目中有xxx_global.h文件，就说明这是一个生成dll的项目  
备注：这里并不需要去继承某个Qt的类，只需要在定义类时加上一个宏声明  


## 产生方法
新建项目 - Library - C++ Library  
其中，Detials步骤的Type选项选择默认的Shared Library  
对项目编译时，会有如下报错，不用管，不影响  
编译之后，在运行目录下会产生对应的dll文件和lib文件  
```
error: You need to set an executable in the custom run configuration.
```


## 代码示例
1. library_test.pro文件  
```
QT -= gui

TEMPLATE = lib
DEFINES += LIBRARY_TEST_LIBRARY

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    library_test.cpp

HEADERS += \
    library_test_global.h \
    library_test.h

# Default rules for deployment.
unix {
    target.path = /usr/lib
}
!isEmpty(target.path): INSTALLS += target
```
2. library_test_global.h文件  
```
#ifndef LIBRARY_TEST_GLOBAL_H
#define LIBRARY_TEST_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(LIBRARY_TEST_LIBRARY)
#  define LIBRARY_TEST_EXPORT Q_DECL_EXPORT //当编译共享库时，必须将其添加到使用的符号声明
#else
#  define LIBRARY_TEST_EXPORT Q_DECL_IMPORT //当编译一个使用了该共享库的项目时，必须将其添加到使用的符号声明
#endif

#endif // LIBRARY_TEST_GLOBAL_H
```
3. library_test.h文件  
```
#ifndef LIBRARY_TEST_H
#define LIBRARY_TEST_H

#include "library_test_global.h"

class LIBRARY_TEST_EXPORT Library_test //必须在class和类名之间加上宏声明
{
public:
    Library_test();
};

#endif // LIBRARY_TEST_H

```
4. library_test.cpp文件  
```
#include "library_test.h"

Library_test::Library_test()
{

}
```