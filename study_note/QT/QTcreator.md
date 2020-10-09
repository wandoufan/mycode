# QTcreator

## QTcreator提供的应用程序模板
1. Qt Widgets Application  
这是最常用的模板，支持桌面平台的GUI应用程序  
GUI的设计基于C++语言，采用QT提供的一套C++类库  
2. Qt Console Application  
控制台应用程序，无GUI界面，一般用于学习C/C++语言  
3. Qt Quick Application  
创建可部署的 Qt Quick 2 应用程序，其界面设计采用QML语言，程序架构采用C++语言  
利用 Qt Quick 可以设计非常炫的用户界面，一般用于移动设备或嵌入式设备上无边框的应用程序的设计  
4. Qt Quick Controls 2 Application  
创建基于 Qt Quick Controls 2 组件的可部署的 Qt Quick 2 应用程序  
5. Qt Canvas 3D Application  
创建 Qt Canvas 3D QML 项目，也是基于 QML 语言的界面设计，支持 3D 画布  


## 创建界面的基类(base class)
1. QMainWindow 主窗口类  
主窗口具有主菜单栏、工具栏和状态栏，一般以独立窗口显示  
QMainWindow类中好像不能使用Push Button组件  
2. QWidget 所有具有可视界面类的基类  
QWidget继承于QObject类和QPaintdevice类，也是QMainWindow和QDialog的父类  
QWidget在没有指定父容器时可以作为独立的窗口，指定父容器之后可以作为父容器的内部组件  
选择QWidget创建的界面对各种界面组件都可以支持  
QWidget窗口可以被其父窗口或其他窗口挡住一部分  
3. QDialog 对话框窗口类  
QDialog主要用于短期任务或用户进行短期通讯的顶级窗口  


## 三种对话框类型
1. 模式对话框  
窗口创建后，主窗口其他内容都不能执行，只有等该窗口关闭退出后才能执行  
使用exec()函数来实现阻塞功能  
2. 非模式对话框  
窗口创建后，主窗口其他内容不受影响，可以正常执行  
使用show()函数来显示  
3. 半模式对话框  
窗口创建后，主窗口无法点击，但后台程序可以继续运行  
使用setModal(true)和setWindowModality()函数  


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


## 项目组织结构
注意：QT项目的存放路径一定不能有中文，否则无法编译  
1. QMainWindow 主窗口类
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--mainwindow.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入口)
       |                                    |--mainwindow.cpp(主窗口类的实现文件)
Demo1--|
       |--Forms(项目下所有的界面文件*.ui)--|--mainwindow.ui(主窗口的界面文件，使用XML语言)
```
2. QWidget 具有可视界面类的基类
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--widget.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入口)
       |                                    |--widget.cpp(主窗口类的实现文件)
Demo2--|
       |--Forms(项目下所有的界面文件*.ui)--|--widget.ui(主窗口的界面文件，使用XML语言)
```
3. QDialog 对话框类
```
       |--Demo.pro(项目管理文件，包括一些对项目的设置项)
       |--Headers(项目下所有的头文件*.h)--|--dialog.h(主窗口类的头文件)
       |
       |--Sources(项目下所有的C++文件*.cpp)--|--main.cpp(主函数文件，即程序入口)
       |                                    |--dialog.cpp(主窗口类的实现文件)
Demo2--|
       |--Forms(项目下所有的界面文件*.ui)--|--dialog.ui(主窗口的界面文件，使用XML语言)
```


## 项目中包含的文件
1. .pro文件  
.pro文件是项目的管理文件，文件名就是项目名，相当于配置文件  
主要用于记录项目的一些设置，以及项目包含文件的组织管理  
当项目增删文件时，.pro文件会自动更新，不需要手动修改  
2. main.cpp文件  
main.cpp是实现main()函数的文件，包含创建窗口、显示窗口、运行应用程序等功能  
用QApplication类获得一个实例化对象a，即应用程序对象，a.exec()用来启动应用程序执行  
用Widget类获得一个实例化对象w，即用来设计窗口的对象，w.show()用来显示窗口  


## 与窗体相关的4个文件
1. widget.h
定义窗体类的头文件，定义了一个继承自类QWidget的类Widget  
另外还包含了自己定义出的那些槽函数，和widget.cpp文件中定义出的槽函数一一对应  
2. widget.cpp
Widget类的功能实现的源程序文件  
3. widget.ui
窗体界面文件，由UI设计器自动生成，存储了窗体上各个组件的属性设置和布局  
使用XML语言，一般用UI设计器可视化设计生成  
4. ui_widget.h（对widget.ui编译后才在build目录下生成该文件）
根据用户设置的窗体组件及属性、信号与槽的关联等自动生成一个类的定义文件，类名为Ui_Widget  


## UI设计窗口功能区域划分
双击项目中的.ui文件可以打开UI设计窗口，包括：  
1. 设计组件(左侧)  
分为多个组，如Layouts、Buttons、Display Widgets等  
2. 待设计窗体(中间)  
拖动一个组件到窗体上即可  
3. 编辑器(下方)  
Signals和Slots编辑器用于可视化地进行信号与槽的关联  
Action编辑器用于可视化设计Action  
4. 工具栏(上方)  
工具栏中的按钮主要用于实现布局和界面设计  
5. 对象浏览器(右上方)  
对象浏览器(Object Inspector)用树状显示各组件间的关系  
包含两列，即每个组件的对象名称和所属的类名称  
6. 属性编辑器(右下方)  
属性编辑器(Property Editor)中可以显示或修改某个选中的组件的属性值  
包含两列，即每个组件的属性和属性值  
属性从上到下可以分为多个组，实际表示了类的继承关系  
例如，label组件为：QObject→QWidget→QFrame→QLabel  


## 组件的属性
1. objectName
对于窗体上创建出的每一个组件，都有一个objectName属性作为组件实例的名称  
具体属性值由系统自动创建，一般按照组件创建顺序来命名，例如checkBox、checkBox_2、checkBox_3  
objectName作为组件的唯一标识，一般不要对其进行修改  


## 界面设计布局
1. 组件之间的层次关系  
设计组件中包含一类containers组件，用来实现层次关系，将各个组件的分布设计更加美观  
例如，可以将三个checkBox放在一个groupBox中，移动groupBox时三个checkBox会随之移动  
另外，在每个containers组件内部可以单独设置不同的排版布局  
组件之间具体的层次关系可以在右上方的对象浏览器中查看  
2. 组件的排版布局  
设计组件中包含Layouts组件和Spacers组件，具体包括：  
Vertical Layout 垂直方向布局，组件自动在垂直方向上分布  
Horizontal Layout 水平方向布局，组件自动在水平方向上分布  
Grid Layout 网格状布局，网状布局大小改变时，每个网格的大小都改变  
Form Layout 窗体布局，与网格状布局类似，但是只有最右侧的一列网格会改变大小  
Horizontal Spacer 一个用于水平分隔的空格  
Vertical Spacer 一个用于垂直分隔的空格  
3. 伙伴关系(Buddy)  
伙伴关系是指将一个Label和一个组件相关联，在程序运行时即可用快捷键将输入光标切换到某个组件上  
点击上方工具栏中的"Edit Buddies"即可进入伙伴关系编辑模式  
编辑完成后点击工具栏的"Edit Widget"即可退回到组件编辑模式  
伙伴关系设置完成后可以在label组件的buddy属性中进行查看
4. Tab顺序  
Tab顺序是指程序在运行时，按下Tab键时输入光标的移动顺序  
点击上方工具栏中的"Edit Tab Order"即可进入Tab顺序编辑模式  
编辑完成后点击工具栏的"Edit Widget"即可退回到组件编辑模式  
注意：没有输入光标的组件是没有Tab顺序的，例如Label组件  


## 信号与槽(signal & slot)机制
1. 信号(signal)就是在特定情况下被触发的事件  
例如，PushButton最常见的信号就是鼠标单击时发射的clicked()信号  
2. 槽(slot)就是对信号响应的函数  
一个槽就是一个函数，与一般的C++函数是一样的，可以具有任何参数，也可以被直接调用  
也可以定义在类的任何部分(private、public或protected)  
槽函数与一般函数的不同的是：槽函数可以与一个信号关联，信号发射时槽函数自动执行  
3. 信号与槽关联是用QObject::connect()函数实现的  
函数基本格式为QObject::connect(sender, SIGNAL(signal()), receiver, SLOT(slot()));  
connect()是QObject类的一个静态函数，而QObject是所有QT类的基类，故实际调用时可以忽略  
直接写为connect(sender, SIGNAL(signal()), receiver, SLOT(slot()));  
sender是发射信号的对象的名称  
signal()是信号名称，相当特殊的函数，需要带括号，有参数时需要指明参数  
receiver是接收信号的对象的名称  
slot()是槽函数的名称，需要带括号，有参数时需要指明参数  
4. SIGNAL和SLOT  
SIGNAL和SLOT是QT的宏，用于指明信号和槽，并将它们的参数转换为相应的字符串  


## 信号与槽的使用规则  
1. 一个信号可以与多个槽关联，槽函数按建立连接时的顺序依次执行  
例如：当spinNum对象的数值变化时，addFun()和updateStatus()会依次响应  
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(addFun(int));  
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(updateStatus(int));  
2. 一个槽可以被多个信号关联  
例如：下面三个信号都可以触发槽函数setTextFontColor()  
connect(ui->rBtnBlue,SIGNAL(clicked()),this,SLOT(setTextFontColor()));  
connect(ui->rBtnRed,SIGNAL(clicked()),this,SLOT(setTextFontColor()));  
connect(ui->rBtnBlack,SIGNAL(clicked()),this,SLOT(setTextFontColor()));  
3. 一个信号可以连接另一个信号，一个信号发射时也会发射另一个信号  
例如：valueChanged()函数会触发refreshInfo()函数  
connect(spinNum, SIGNAL(valueChanged(int)), this, SIGNAL(refreshInfo(int));  
4. 信号的参数与槽的参数个数和类型都要一致  
至少信号的参数不能少于槽的参数，否则会编译报错  
5. 在使用信号与槽的函数的类中，必须在类的定义中加入宏Q_OBJECT  
6. 当一个信号发射时，与其关联的槽函数都会立即执行  
只有在信号关联的槽函数都执行完毕之后才会执行信号后面的代码  


## 常用信号
1. clicked()
2. clicked(bool)
信号 clicked(bool) 会将 CheckBox 组件当前的选择状态作为一个参数传递，
在响应代码里可以直接利用这个传递的参数。
而如果用信号 clicked()，则需要在代码里读取 CheckBox 组件的选中状态。
3. pressed()
4. released()
5. toggled(bool)
6. stateChanged(int)


## QFont的相关方法属性
```
    QFont font = ui -> textEdit -> font();
    font.setUnderline(checked);
    ui -> textEdit -> setFont(font);
```
1. 常用函数：  
setFamily() 设置字体  
setBold() 字体加粗  
setItalic() 斜体  
setOverline() 上划线  
setUnderline() 下划线  
setStrikeOut() 删除线  
setPointSize() 设置字体肉眼看到的实际大小，在不同设备上显示大小相同  
setPixelSize() 设置字体像素单位的大小，在不同设备上显示大小可能不同  