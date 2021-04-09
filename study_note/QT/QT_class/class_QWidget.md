# QWidget

## 基本功能
QWidget是所有用户接口对象(具有可视界面组件)的基类  
QWidget继承于QObject类和QPaintdevice类，也是QMainWindow和QDialog的父类  
QWidget在没有指定父容器时可以作为独立的窗口，指定父容器之后可以作为父容器的内部组件  
选择QWidget创建的界面对各种界面组件都可以支持  
QWidget窗口可以被其父窗口或其他窗口挡住一部分  


## 常用属性
* windowModality : Qt::WindowModality
这个属性用来设置哪个windows窗口会被模态的widget锁住  
这个属性只对windows窗口有意义，默认值为Qt::NonModal.
一个模态的widget会阻止其他窗口的widget获取到输入  
把QWidget::windowModality设置为Qt::ApplicationModal等同于把Qialog::modal属性设置为true  
1. Qt::WindowModality windowModality() const
2. void setWindowModality(Qt::WindowModality windowModality)


## enum Qt::WindowModality
模态窗口的属性取值
```
Qt::NonModal
这个窗口不是模态的，不会封锁其他窗口的输入
Qt::WindowModal
这个窗口对于单个窗口是模态的，并封锁该窗口所有父类的输入
Qt::ApplicationModal
这个窗口对于整个程序是模态的，封锁所有窗口的输入
```
