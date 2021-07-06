# Qt项目中的xxx_global.h头文件

## 基本功能
在Qt项目中实现共享库文件的功能，可以自己生成一个dll文件  
Qt creator会自动生成一个和项目同名的{projectName}\_global.h文件  
因此当项目中有xxx_global.h文件，就说明这是一个生成dll的项目  


## 产生方法
新建项目 - Library - C++ Library  
其中，Detials步骤的Type选项选择默认的Shared Library  


## 代码示例
library_test_global.h  
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