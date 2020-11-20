# QT中的函数

## PluginDetailsView中提供的常用函数
备注：详见QT帮助的'List of All Members for PluginDetailsView'
1. setWindowTitle(const QString &)
窗口的标题名称默认是自己定义的类名，也可以用setWindowTitle函数进行修改  
一般在cpp文件中类的构造函数里来使用setWindowTitle函数  
```
//注意：直接写函数名，前面没有对象或者指针来调用这个函数
setWindowTitle("汉王手写签字板ESP370");
```
2. setFixedSize(int , int )
设置某个对象对应UI窗口的大小，第一个参数是宽度，第二个参数是高度  
有的窗口在UI设计界面中可能显示不出来，就可以通过这个函数来调整大小  
```
//必须要通过某个对象来调用该函数
m_pHWPenSign->setFixedSize(600, 160);
```