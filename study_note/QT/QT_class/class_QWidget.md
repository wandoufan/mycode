# QWidget

## 基本功能
QWidget是所有用户接口对象(具有可视界面组件)的基类  
QWidget在没有指定父容器时可以作为独立的窗口，指定父容器之后可以作为父容器的内部组件  
选择QWidget创建的界面对各种界面组件都可以支持  
QWidget窗口可以被其父窗口或其他窗口挡住一部分  
父类：QObject、QPaintdevice  
子类：QMainWindow、QDialog、...  


## todo_list
整理QWidget中的函数
尤其是结合PluginDetailsView中记录的函数，如show()


## 常用成员变量
* windowModality : Qt::WindowModality
这个属性用来设置哪个windows窗口会被模态的widget锁住  
这个属性只对windows窗口有意义，默认值为Qt::NonModal  
一个模态的widget会阻止其他窗口的widget获取到输入  
把QWidget::windowModality设置为Qt::ApplicationModal等同于把Qialog::modal属性设置为true  
1. Qt::WindowModality windowModality() const
2. void setWindowModality(Qt::WindowModality windowModality)


## enum Qt::WindowModality
这个集合描述了窗口的模态特性  
```
Constant   Value   Description
Qt::NonModal   0   这个窗口是非模态的，不会封锁其他窗口获得输入
Qt::WindowModal   1   这个窗口是模态的，只会封锁其父类窗口、父类的父类窗口等获得输入
Qt::ApplicationModal   2   这个窗口是模态的，会封锁其他所有窗口获得输入
```