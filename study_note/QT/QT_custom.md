# QT中自定义组件

## 基本情况
QT中提供了很多基本的组件，但实际使用中可能还需要其他组件  
我们可以自己定义制作各种组件，用于后续的使用  
组件可能是用QT基本组件组合起来，也可能是来自QT之外  
可以在qt creator中使用组件，也可以在qt desginer中使用组件  
创建自定义组件一般有提升法和插件法两种方法  


## 参考资料
> https://blog.csdn.net/giselite/article/details/12622429
> https://blog.csdn.net/giselite/article/details/12622561
> https://blog.csdn.net/giselite/article/details/12622625
> https://blog.csdn.net/anyuliuxing/article/details/96604213
> https://www.cnblogs.com/feiyangqingyun/p/9694025.html


---------------------------------------------------------------

## 提升法简介

缺点：
提升法用于界面可视化设计时不够直观，不能在界面上立刻显示自定义组件的效果  

## 提升法1. (还没有测试过)
在QT creator的UI中，或QT designer中选中部件，
右键提升，填入提升的类名称(与基类的名称要不相同)，头文件名称  
被提升的组件和原有组件是一个基类
升级方法优点：简单快捷
升级法的缺点：不能在Qt Designer中设置自定义控件自己的特有属性，也不能够绘制自己


---------------------------------------------------------------

## 插件法简介
插件是指为UI设计器设计自定义组件的Widget插件  
可以直接安装到UI设计器的组件面板里，设计使用时就能看到其实际显示效果  
但在编译和运行时需要用到插件的dll文件(windows平台上)  



## 创建QT自定义控件项目的详细步骤
1. QT新建项目，选中'其他项目-QT4设计师自定义控件'
2. Location:填写项目名称和项目路径
3. Kits:选择编译器
4. Custom Widgets:填写自定义控件的类名
注意：自定义控件类的类名首字母要大写，例如'CustomButton'  
右侧'源文件'中的内容会自动生成，默认即可  
可以在这里为自定义控件添加图标文件，添加后会在.qrc文件中显示  
右侧'说明'和'默认属性'可以不填，后面可以通过函数进行填写  
5. Plugin Details:填写插件名称
可以使用默认的自动生成名称，例如'CustomButtonPlugin'  


## 自定义控件项目目录
生成的项目目录文件如下：  
备注：这个目录结构只是在Qt creator里这么显示  
实际上在项目文件夹里所有文件都是放在一起的，项目文件夹里也没有任何子目录  
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


## 制作QT自定义控件的注意事项
1. 自定义控件动态库的位数要和qt creator/designer的位数一致
如果位数不一致，creator/designer无法载入.dll文件，在UI设计界面就看不到自定义控件  
在'帮助'-'关于Qt Creator'中可以查看Creator本身的版本  
例如，这台电脑上的Qt Creator 4.13.1是MSVC 2019 64位的，自定义控件也要用MSVC 2019 64位release出来相应的dll文件  
2. release版本和debug版本不能混用  
如果自定义控件的dll是release模式下产生的，那么使用自定义控件的工程项目也要用release模式进行编译  
如果自定义控件的dll是debug模式下产生的，那么使用自定义控件的工程项目也要用debug模式进行编译  
3. qt designer和qt creator之间是相互独立的
如果把dll拷贝到qt designer路径下，那就只能在qt designer中看到，qt creator里是看不到的  
如果把dll拷贝到qt creator路径下，那就只能在qt creator中看到，qt designer里是看不到的  
4. 自定义控件的类名称的首字母不能用小写
否则UI界面中拖过去的控件自动生成的默认名称和类名一样，会编译通不过  
例如：自定义控件的类名为'CustomButton'，默认生成对象名为'customButton'  
5. 不能在插件源文件的构造函数中对自定义组件进行实例化和属性设置
首先，在构造函数里对CustomButton进行实例化没有作用  
另外，这样产生出来的dll拷贝到对应路径下后，会造成qt designer打不开  


## 插件法1. 用UI界面将QT基本组件组合成复合组件
> https://blog.csdn.net/lmhuanying1012/article/details/78217750
> https://blog.csdn.net/qq_37354286/article/details/79954197
1. 在qt creator中新建一个自定义控件项目
2. 删除项目中的控件头文件、控件源文件、控件项目文件
备注：删除.h文件时，会提示是否将.cpp文件和.pri文件一并删除  
3. 选中项目目录，右键-添加新文件，选择'QT'-'QT设计师界面类'
4. Form Template：选择Widget
5. Class Details：设置自定控件类名
将类名从Form改为新建自定义控件项目时的类名  
6. 选择.ui文件，在UI设计界面任意组合我们需要的自定义控件
备注：可以在UI界面中对自定义控件的位置和大小进行设置  
UI界面中底部的Widget大窗口的大小即为将来自定义控件的大小  
7. 在插件源文件中对自定义控件的名称、描述、所在组名等进行设置
注意：不要通过domXml()函数对组件的大小和位置进行设置  
详见 QDesignerCustomWidgetInterface.md  
8. 在控件头文件的类声明中添加宏'QDESIGNER_WIDGET_EXPORT'
另外，加上'#include <QtDesigner/QDesignerExportWidget>'  
详见 QDesignerCustomWidgetInterface.md  
9. 选择对应版本的编译器，将项目用release模式编译运行
之后在编译运行目录下，会产生对应的dll和lib  
备注：release时会有如下报错，不用管，不影响  
```
error: You need to set an executable in the custom run configuration.
```

## 插件法2. 用纯代码将QT基本组件设计成自定义组件
1. 在qt creator中新建一个自定义控件项目
2. 在自动生成的控件头文件和控件源文件中插入组件相关的代码
备注：可以在这部分代码中用函数对自定义控件的位置和大小进行设置  
代码实现部分参考：QT_purecode.md  
3. 在插件源文件中对自定义控件的名称、描述、所在组名等进行设置
注意：不要通过domXml()函数对组件的大小和位置进行设置  
详见 QDesignerCustomWidgetInterface.md  
4. 在控件头文件的类声明中添加宏'QDESIGNER_WIDGET_EXPORT'
另外，加上'#include <QtDesigner/QDesignerExportWidget>'  
详见 QDesignerCustomWidgetInterface.md  
5. 选择对应版本的编译器，将项目用release模式编译运行
之后在编译运行目录下，会产生对应的dll和lib  
备注：release时会有如下报错，不用管，不影响  
```
error: You need to set an executable in the custom run configuration.
```


## 插件法3. 插件法用外部的组件转换封装成QT可用的组件
备注：测试失败，dll导出后在designer里显示是一个空白  
仿照纯代码创建自定义控件的过程，将外部组件包进一个Widget里面，然后把整个Widget封装出来  
以引入Labview中的CWButton拨杆按钮为例：  
其中，CustomButton是我们新建的自定义组件类，继承于QWidget  
把外部组件CWButton类的实例对象作为CustomButton的一个成员  
至于CWButton本身的源文件和头文件放入到同目录下即可，不需要对其改动  
在插件源文件返回对象时，返回CustomButton对象，而不是CWButton对象  
1. custombutton.h示例：
```
#ifndef CUSTOMBUTTON_H
#define CUSTOMBUTTON_H

#include <QWidget>
#include <QtDesigner/QDesignerExportWidget>
#include "cwuicontrolslib.h"
using namespace CWUIControlsLib;

class QDESIGNER_WIDGET_EXPORT CustomButton : public QWidget
{
    Q_OBJECT

public:
    CustomButton(QWidget *parent = 0);

public:
    CWButton *qt_button;
    QString licenseKey;
};

#endif // CUSTOMBUTTON_H
```
2. custombutton.cpp示例：
```
#include "custombutton.h"
#include <QVBoxLayout>

CustomButton::CustomButton(QWidget *parent) :
    QWidget(parent)
{
    qt_button = new CWButton(licenseKey, this);
    qt_button -> setGeometry(0, 0, 100, 100);
    qt_button -> show();

    auto mainLayout = new QVBoxLayout(this);
    mainLayout -> addWidget(qt_button);
}
```
3. custombuttonplugin.cpp示例
```
QWidget *CustomButtonPlugin::createWidget(QWidget *parent)
{
    return new CustomButton(parent);
}
```

--------------------------------------------------------

## 1. 在qt designer里使用自定义控件
如果要在qt designer中使用，只需要把dll拷贝到对应的designer路径下  
qt designer根据不同编译器有多个版本，参考路径如下：  
```
C:\Qt\5.15.1\msvc2019_64\plugins\designer
```
如果dll是32位的，则必须放到32位的路径下，在32位的qt designer中查看  
如果dll是64位的，则必须放到64位的路径下，在64位的qt designer中查看  


## 2. 在qt creator里使用自定义控件
如果要在qt creator中使用，即在QT项目中使用自定义控件，则过程很复杂  
说明：这个操作过程是根据网上教程看到的，虽然能用，但非常繁琐，不知道是否有其他简单方法  
1. 将自定义控件dll拷贝到qt creator路径下
QT creator的正确路径如下：  
```
C:\Qt\Tools\QtCreator\bin\plugins\designer
```
QT creator的错误路径为：  
```
C:\Qt\Tools\QtCreator\lib\qtcreator\plugins
```
注意：qt creator只有一个，位数版本是固定的，必须使用对应的dll  
例如，这台电脑上的QT是MSVC 2019 64位的，自定义控件也要用MSVC 2019 64位release出来相应的dll文件  
2. 在项目目录下新建一个include文件夹和一个lib文件夹
将自定义控件的控件头文件拷贝到include文件夹中  
将自定义控件release时生成的lib文件拷贝到lib文件夹中  
3. 在项目的.pro文件中添加
```
INCLUDEPATH += $$PWD/include
LIBS += $$PWD/lib/custombuttonplugin.lib
```
4. 在项目的UI界面中添加自定义控件，用对应版本的编译器以release模式运行
此时由于缺少动态库，运行既不会报错，也不会成功弹出窗口  
在生成的项目运行目录下，将自定义控件dll拷贝到exe文件的同目录下  
5. 再次用对应版本的编译器以release模式运行，如果成功此时就会弹出带有自定义控件的窗口


-----------------------------------------------------

## 给自定义组件添加属性
QT提供的各种基本组件都可以通过UI界面右下角的属性编辑器进行设置  
自定义的组件可以添加属性以及属性值
1. 方法一：
通过Q_PROPERTY宏定义自定义控件的相关属性，比如：
Q_PROPERTY(double minValue READ getMinValue WRITE setMinValue)
上述语句会添加属性minValue，数据类型为double
READ后的函数用于读取关联的变量值并在designer中显示
WRITE后的函数用于将designer中的输入值设置为关联的变量值
数据类型不同，在使用自定义控件过程中设置属性时会自动弹出不同类型的Dialog，
比如QColor类型对应QColorDialog，QFont类型对应QFontDialog等。
备注：这些语句在定义时写在自定义控件类的内部（控件头文件中）
2. 方法二：
在QT Designer中可以选择我们的自定义组件，然后通过UI界面进行属性功能的添加



