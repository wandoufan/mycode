# QT中的.pri文件

## 基本功能
.pri文件和.pro文件一样，都是用来做项目的管理文件  
但.pri文件一般用在自定义控件项目中，用来做内层控件部分的配置文件


## 示例
自定义控件项目目录示例
```
demo11_custom
	│  demo11_custom.pro 项目管理文件
	│  demo11_custom.pro.user
	│      
	├─qtcwbutton
	│  │  qtcwbutton.pri 控件项目文件
	│  │  
	│  ├─Headers
	│  │      qtcwbutton.h 控件头文件
	│  │      
	│  └─Sources
	│          qtcwbutton.cpp 控件源文件
	│          
	├─Resources
	│      icons.qrc 资源集合文件
	│
	├─Headers
	│      qtcwbuttonplugin.h 插件头文件
	│      
	└─Sources
	        qtcwbuttonplugin.cpp 插件源文件
```
文件内容示例
```
HEADERS += custombutton.h
HEADERS += cwuicontrolslib.h

SOURCES += custombutton.cpp
SOURCES += cwuicontrolslib.cpp

```