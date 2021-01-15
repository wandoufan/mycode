# QLayout

## 参考资料
https://blog.csdn.net/li162001/article/details/88126928

## 基本功能
QLayout是QT中所有控件几何属性设置相关类的基类，提供界面布局管理功能  
备注：使用前要在.pro文件中添加'QT += widgets'  
继承关系如下：
```
QLayout
	├─QBoxLayout
	│  ├─QHBoxLayout 将所有Widget组件水平排列
	│  └─QVBoxLayout 将所有Widget组件垂直排列
	├─QFormLayout 管理Input Widget组件和与它们关联的labels
	├─QGridLayout 将所有Widget组件以网格状排列
	└─QStackedLayout 一次显示一个组件(组件堆叠在一起，只显示最上面组件)
```


## 源文件示例
以引入Labview中的CWButton拨杆按钮为例：  
CWButton可以在CustomButton的构造函数中用setGeometry函数设置大小
但在UI界面中，自定义控件拖过去之后默认是一个很小的方块，需要手动拉大之后才能看到完整的控件  
可以将控件添加到Layout中，这样默认就能显示完整的大小  
```
#include "customwidget.h"
#include <QVBoxLayout>

CustomButton::CustomButton(QWidget *parent) :
    QWidget(parent)
{
    qt_button = new CWButton(licenseKey, this);
    qt_button -> setGeometry(0, 0, 300, 300);
    auto mainLayout = new QVBoxLayout(this);
    mainLayout -> addWidget(qt_button);
    mainLayout -> setContentsMargins(0, 0, 0, 0);
}
```


## 常用函数
1. void QLayout::setContentsMargins(int left, int top, int right, int bottom)
默认情况下，Layout控件和Widget边框之间有一个缝隙(11个像素的间距)  
可以用setContentsMargins来具体设置间距的大小，一般都改为0  
备注：setMargin(int margin)函数有同样的功能，但已经过时，不再使用  

