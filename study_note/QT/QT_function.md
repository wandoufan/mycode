# QT中的函数

## PluginDetailsView中提供的常用函数
这些函数都是控件对象可以调用的与UI界面相关的函数  
详见QT帮助的'List of All Members for PluginDetailsView'  
备注：这些函数都是Widget的成员函数，因此对象类型必须是继承于QWidget的才能调用  
1. void setWindowTitle(const QString &)
窗口的标题名称默认是自己定义的类名，也可以用setWindowTitle函数进行修改  
一般在cpp文件中类的构造函数里来使用setWindowTitle函数  
```
//注意：直接写函数名，前面没有对象或者指针来调用这个函数
setWindowTitle("汉王手写签字板ESP370");
```
2. void QWidget::setFixedSize(int , int )
设置某个对象对应控件的大小，第一个参数是宽度，第二个参数是高度  
有的窗口在UI设计界面中可能显示不出来，就可以通过这个函数来调整大小  
```
//必须要通过某个对象来调用该函数
m_pHWPenSign->setFixedSize(600, 160);
```
3. void QWidget::setGeometry(int , int , int , int )
设置某个对象对应控件的大小和位置  
其中，x坐标和y坐标的位置是相对于UI窗口的左上角，或显示屏的左上角  
第一个参数为x坐标  
第二个参数为y坐标  
第三个参数为控件的宽度  
第四个参数为控件的高度  
4. void QWidget::show()
显示这个Widget对象及其子对象  
调用show()函数等同于调用showFullScreen()、showMaximized()、或setVisible(true)，具体取决于平台的默认选择  
5. virtual void setVisible(bool)
设置Widget对象是否可见  
6. void QWidget::setHidden(bool)
等同与setVisible(!hidden)  
