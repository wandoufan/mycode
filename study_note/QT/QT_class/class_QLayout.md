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



源文件示例：  
```
#include "customwidget.h"
#include <QVBoxLayout>

CustomWidget::CustomWidget(QWidget *parent) : QWidget(parent)
{
    auto mainLayout = new QVBoxLayout(this);
    button = new CWUIControlsLib::CWButton(this);
    mainLayout->addWidget(button);
}
```