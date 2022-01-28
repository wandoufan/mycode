# QDialog

## 基本功能
QDialog是所有对话窗口的基类  
对话窗口一般用作临时任务或与用户之间进行交互，属于最高层级的控件  
如果创建对话框时设置了父类指针，其默认位置是父类控件的中央位置  
有父类控件的对话框还可以共享其父类的任务栏入口  
父类：QWidget  
子类：QColorDialog, QErrorMessage, QFileDialog, QFontDialog, QInputDialog, QMessageBox, QProgressDialog, and QWizard  


## 模态对话框
模态对话窗会封锁同一个程序中其他可见窗口的输入(不只是输入数据，也包括获得点击响应)  
在模态对话窗关闭之前，其他窗口会变的毫无响应  
对话窗可以是WindowModal，也可以是ApplicationModal  
```
QDialog *mydialog = new QDialog(this);
mydialog -> open();
```


## 非模态对话框
非模态对话框与同一个程序中其他窗口之间相互独立，不会影响到其他窗口  
```
QDialog *mydialog = new QDialog(this);
mydialog -> show();
```


## 默认键
对话框的默认键是Enter键，按下默认键表示用户接受对话框的设置，并且想要关闭对话框  
使用QPushButton::setDefault()、QPushButton::isDefault()、QPushButton::autoDefault()可以设置对话框的默认键  


## ESC键
如果用户在一个对话框中按下了ESC键，就会调用QDialog::reject()  
这会将窗口关闭，此时可能需要考虑close event相关的处理  


## 常用QDialog对话框类
QColorDialog（颜色对话框）  
QFileDialog（文件对话框）  
QFontDialog（字体对话框）  
QInputDialog（输入对话框）  
QMessageBox（消息对话框）  
QProgressDialog（进度对话框）  
QErrorMessage（错误信息对话框）  
QPageSetupDialog（页面设置对话框）  
QPrintDialog（打印对话框）  
QPrintPreviewDialog（打印预览对话框）  


## 构造函数
1. QDialog::QDialog(QWidget \*parent = nullptr, Qt::WindowFlags f = Qt::WindowFlags())
f参数可以设置对话窗口的具体样式  


## 常用成员变量
1. modal : bool (模态)
这个属性用来设置show()函数弹出的dialog对话框是模态还非模态  
默认情况下，这个属性为false，即弹出的dialog对话框是非模态的  
把这个属性设置为true等同于把QWidget::windowModality设置为Qt::ApplicationModal  
另外，exec()函数会忽视这个属性，总是以模态来弹出dialog对话框  
1.1 bool isModal() const
1.2 void setModal(bool modal)

2. sizeGripEnabled : bool
这个属性用来设置对话框的右下角是否显示抓痕(可以通过点击拖拽对窗口进行大小调整)  
默认情况下，这个属性为false  
当属性为true时，一个QSizeGrip对象会被放在对话框的右下角  
备注：无论是否显示抓痕，都能拖动右下角调整窗口大小，但有抓痕时拖动点从右下角顶点到有抓痕部分都能拖动，无抓痕时只能拖动右下角顶点附近很少的地方，这意味着该属性是扩展了右下角窗口大小调整的可拖放区域  
2.1 bool isSizeGripEnabled() const
2.2 void setSizeGripEnabled(bool)



## 常用公共函数
1. int QDialog::result() const
在对话框还没被销毁的时候，可以返回模态对话框的返回值：Accepted或Rejected  
如果对话框是用Qt::WA_DeleteOnClose属性创建的，那么不要调用result()函数  
注意：当在一个QMessageBox实例上调用这个函数，函数返回值是enum QMessageBox::StandardButton  

2. void QDialog::setResult(int i)
设置模态对话框的返回值  


## 公共槽函数
1. [virtual slot] int QDialog::exec()
以模态类型显示一个对话框，默认情况下，是Qt::ApplicationModal  
exec()函数的返回值是模态对话框的返回值  
使用exec()函数可能会造成一系列危险的bug，例如：通过exec()打开了一个对话框，然后删除了对话框的父类，这可能会造成程序崩溃  
注意：避免使用exec()函数，推荐使用open()函数，因为open()是异步的，不会制造额外的事件循环  

2. [virtual slot] void QDialog::open()
以模态类型显示一个对话框，然后立刻返回，默认情况下，是Qt::WindowModal  

3. [virtual slot] void QDialog::done(int r)
关闭对话框，并将其返回值设置为r，会发出finished()信号，其参数值为r  
如果r是Accepted或Rejected，同时也会发出accepted()或rejected()信号  
如果这个对话框是用exec()调用出来的，使用done()函数也会导致本地事件循环关闭，exec()返回r  

4. [virtual slot] void QDialog::accept()
隐藏模态对话框，并将模态对话框的返回值设置为Accepted  

5. [virtual slot] void QDialog::reject()
隐藏模态对话框，并将模态对话框的返回值设置为Rejected  


## 信号函数
1. [signal] void QDialog::accepted()
当用户点击'同意'、调用accept()\done()，都会发出该信号  
注意：当调用hide()或setVisible(false)来隐藏对话框，或删除对话框，不会发出该信号  

2. [signal] void QDialog::rejected()
当用户点击'拒绝'、调用reject()\done()，都会发出该信号  
注意：当调用hide()或setVisible(false)来隐藏对话框，或删除对话框，不会发出该信号  

3. [signal] void QDialog::finished(int result)
当用户操作或者调用reject()\accept()\done()来设置对话框的返回值时，都会发出该信号  
注意：当调用hide()或setVisible(false)来隐藏对话框，或删除对话框，不会发出该信号  


## enum QDialog::DialogCode
这个集合描述了模态对话框的返回值
```
Constant   Value
QDialog::Accepted   1
QDialog::Rejected   0
```