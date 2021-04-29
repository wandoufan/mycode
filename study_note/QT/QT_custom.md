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
插件可以直接安装到UI设计器的组件面板里，设计使用时就能看到其实际显示效果  
插件法的本质是把自定义组件放到一个Widget里面包起来，然后将Widget导出为dll  
在创建自定义控件项目时就指明了控件的基类为QWidget，即控件类自动继承了QWidget  


## 创建QT自定义控件项目的详细步骤
1. QT新建项目，选中'其他项目-QT4设计师自定义控件'
2. Location:填写项目名称和项目路径
3. Kits:选择编译器
4. Custom Widgets:填写自定义控件的类名
注意：自定义控件类的类名首字母要大写，例如'CustomButton'  
右侧'源文件'中的内容会自动生成，默认即可  
其中，控件的基类默认为QWidget，一般不要改动  
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
6. 返回按钮名称的问题
在插件源文件中有一个返回按钮名称的函数，默认为自定义控件的类名  
这里返回的名称就是将来在左侧组件列表中显示的名称  
注意：这里的名称一定不能随意改写，必须和自定义控件的类名完全一样  
如果随意写一个名字，如'CWButton1'，过程中不会报错，但将来拖入到设计界面中会是一个空白的组件，什么都显示不出来  
```
QString CustomButtonPlugin::name() const
{
    return QLatin1String("CustomButton");
}
```


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
自定义控件在Widget大窗口中的位置即为将来的显示位置，一般要放最左上角  
7. 在插件源文件中对自定义控件的名称、描述、所在组名等进行设置
注意：不要通过domXml()函数对组件的大小和位置进行设置  
注意：不要修改name()函数中默认的控件名称，否则将来显示空白  
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
一般在源文件的构造函数中用setGeometry()函数来设置大小和位置  
其中位置参数一般都要设为0，即控件要出现在Widget的最左上角  
代码实现部分参考：QT_purecode.md  
3. 在插件源文件中对自定义控件的名称、描述、所在组名等进行设置
注意：不要通过domXml()函数对组件的大小和位置进行设置  
注意：不要修改name()函数中默认的控件名称，否则将来显示空白  
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
以引入Labview中的CWButton拨杆按钮为例：  
1. 控件简介
拿到了一个cwui.ocx文件，要求将其中的CWButton提取并封装到qt designer中使用  
其中，CWButton是一个来自于LabView的开关式按钮，具有多种显示形态和属性  
这个控件是完全来自于QT外部的控件，并不是由QT自身控件组合而成的  
2. 分析过程
用dumpcpp工具将cwui.ocx解析，得到一个头文件和对应源文件，均为一万多行的代码  
在自动生成的原始代码中就有很多的报错，只能手动将报错部分注释掉  
后来得知这个ocx文件是32位的，而最开始用了64位的dumpcpp工具去解析，这可能会造成一定的问题  
分析代码文件，包含CWButton类在内，里面包含了很多个组件  
但是CWButton和其他部分相互嵌套，关系很复杂，尝试把CWButton单独取出来失败  
备注：对于自动生成的代码一般不要修改，也不要单独取出一部分，很可能会出错  
决定将整个代码都一起用，先测试直接将CWButton实例化并调用其设置函数  
测试成功，表明这段代码本身没有问题，可以直接使用  
3. 创建过程
针对CWButton创建自定义控件的过程中遇到了很多问题，直接记录最终成功的方案  
自动生成的头文件和源文件保持不动，新建一个自定义组件类CustomButton  
把外部组件CWButton类的实例对象作为CustomButton的一个成员  
在插件源文件返回对象时，返回CustomButton对象，而不是CWButton对象  
```
CWButton
	│  CWButton.pro 项目管理文件
	│  CWButton.pro.user
	│      
	├─custombutton
	│  │  custombutton.pri 控件项目文件
	│  │  
	│  ├─Headers
	│  │      custombutton.h 控件头文件
	│  │      cwuicontrolslib.h 自动生成的头文件
	│  └─Sources
	│         custombutton.cpp 控件源文件
	│         cwuicontrolslib.cpp 自动生成源文件
	├─Resources
	│      icons.qrc 资源集合文件
	│
	├─Headers
	│      custombuttonplugin.h 插件头文件
	│      
	└─Sources
	       custombuttonplugin.cpp 插件源文件
```
4. 部分代码示例
custombutton.h示例：
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
custombutton.cpp示例：
```
#include "custombutton.h"

CustomButton::CustomButton(QWidget *parent) :
    QWidget(parent)
{
    qt_button = new CWButton(licenseKey, this);
    qt_button -> setGeometry(0, 0, 300, 300);
    this -> setFixedSize(300, 300);
}
```
custombuttonplugin.cpp示例：
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
如果拷贝了32位的dll文件，则在creator的UI界面里就找不到这个控件  
2. 在项目目录下新建一个include文件夹和一个lib文件夹
将自定义控件的控件头文件拷贝到include文件夹中  
将自定义控件release时生成的lib文件拷贝到lib文件夹中  
3. 在项目的.pro文件中添加
```
INCLUDEPATH += $$PWD/include
LIBS += $$PWD/lib/custombuttonplugin.lib
备注：这里的lib文件要写出文件名，不能只写一个文件路径
```
4. 在项目的UI界面中添加自定义控件，用对应版本的编译器以release模式运行
此时由于缺少动态库，运行既不会报错，也不会成功弹出窗口  
在生成的项目运行目录下，将自定义控件dll拷贝到exe文件的同目录下  
5. 再次用对应版本的编译器以release模式运行，如果成功此时就会弹出带有自定义控件的窗口


## 关于测试CWButton拨杆按钮时的位数问题
1. 问题描述
在自定义控件创建完成之后，想对信号函数等功能进行测试  
CWButton是32位的，而这台电脑上的QT creator是64位的  
把64位dll拷贝进creator的路径下，然后把控件拖到到UI界面中  
如果用32位编译，则会产生报错；如果用64位编译，则控件显示为空白  
2. 解决方案
换个思路，不用dll，也不把控件拖到UI界面上  
用纯代码的方式，把控件的源文件和头文件拷贝到项目目录下  
然后直接将类对象实例化，用32位编译运行即可  
3. 总结
关于在64位的QT creator中去使用32位的dll，没有找到合适的解决方法  


## 关于自定义控件默认大小的问题
1. 问题描述
dll添加到designer或creator中之后，自定义控件拖到UI界面上默认是个很小的方块  
这个方块就是Widget窗口，需要手动拉大之后才能把里面包含的自定义控件显示出来  
窗口默认大小为16x16，一般需要在控件的源文件中对窗口的大小进行扩大设置  
2. 解决方案
以自定义控件CWButton中的custombutton.cpp示例：  
```
#include "custombutton.h"

CustomButton::CustomButton(QWidget *parent) :
    QWidget(parent)
{
    qt_button = new CWButton(licenseKey, this);
    qt_button -> setGeometry(0, 0, 300, 300);
    this -> setFixedSize(300, 300);
}
```
其中，qt_button是需要包进Widget里面的自定义控件CWButton  
自定义控件的大小可以用setGeometry函数设置  
窗口显示的默认大小必须用setFixedSize函数设置  
备注：以前误以为这个控件必须放进一个layout里才能调整大小，其实不用的  
备注：这样设置相当于在代码中把大小写死了，在UI界面上就无法再调整大小  
3. 进一步的解决
目前没有找到办法，既能设置合适的默认大小，又能在UI界面调整大小  
系统的默认大小实在太小了，因此可以用setMinimumSize函数设置控件的最小尺寸  
设置之后控件拖到UI界面上就以最小尺寸显示，在UI界面上可以调大，不可以调小  
```
this -> setMinimumSize(300, 300);
```
4. 关于this指针调用setFixedSize函数的进一步说明
this指针就是这个Widget窗口本身，可以调用一些函数来设置其大小和位置  
如果是一个直接运行的窗口程序，使用setGeometry函数和setFixedSize函数都可以  
如果是用来生成自定义控件dll的程序(非直接运行)，就必须使用setFixedSize函数  
使用setGeometry函数不会报错，但控件还是会显示成一个很小的方块，即设置无效  

-----------------------------------------------------

## 给自定义组件添加属性、信号与槽函数
详见QT_property.md  