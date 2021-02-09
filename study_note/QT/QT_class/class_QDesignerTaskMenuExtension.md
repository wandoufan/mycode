# QDesignerTaskMenuExtension

## 基本功能
这个类允许你向QT designer的任务菜单中添加自定义菜单，提供了接口来创建自定义任务菜单的扩展  
通常用来对QT designer中的某个特定控件创建任务菜单  
使用之前，.pro文件中要添加'QT += designer'  
注意：在程序运行之后的右键菜单和在UI界面设计时的右键菜单，这两个是不一样的  
备注：这个类用的人很少，网上几乎没有资料，官方文档提供了'Task Menu Extension Example'  


## QT designer中的功能扩展
QT designer支持以下四种功能的自定义扩展  
1. QDesignerTaskMenuExtension
选中控件点击右键时显示的菜单  
2. QDesignerPropertySheetExtension
UI界面右下角的属性编辑器  
3. QDesignerMemberSheetExtension
给控件连接信号与槽函数时，显示的相关的信号与槽函数  
4. QDesignerContainerExtension
自定义的多页面容器类型控件  


## 关于任务菜单的说明
在QT designer中，选中一个控件，然后点击右键会出现一个菜单  
通常这个菜单的选项是固定的，一般包括：  
```
change text
change object Name
......
cut
copy
paste
select all
delete
layout
```
但有时候这些选项是不够用的，尤其是对于自定义的控件，这个时候我们可以对任务菜单进行扩展  
扩展任务菜单是一个QActions组成的集合，选项会加入到已有的菜单中  


## 扩展菜单背后的创建过程
在QT designer中，在菜单被调用之前，扩展菜单是不会被创建的  
例如，当你在UI界面上选择并右键一个控件时，它的扩展菜单才会被创建出来  
因此，你必须要构建一个extension factory  
构建方法可以使用'QExtensionFactory'，也可以构建一个子类  
然后，使用QT designer的'QExtensionManager'来进行注册  
当一个菜单被调用时，'QExtensionManager'会通过调用QExtensionFactory::createExtension()来逐个检测所有已经注册的factory，直到其找到一个可以为选择的控件创建扩展任务菜单的factory  
这个factory会为这个扩展创建一个实例  
详见class_QExtensionFactory.md和class_QExtensionManager.md  
备注：QT designer中支持的四种扩展，其背后的处理过程都和上面一样  


## 常用函数
1. [pure virtual] QList<QAction \*> QDesignerTaskMenuExtension::taskActions() const
当选中了一个具有扩展菜单的控件时，以actions列表的形式返回任务菜单的扩展  
注意：这个函数必须被重新实现，才能向列表中添加action  

2. [virtual] QAction \*QDesignerTaskMenuExtension::preferredEditAction() const
当选中了一个具有扩展菜单的控件时，返回被调用的action  
这个action必须是taskActions()函数返回的actions之一  
备注：这个函数也可以进行重新实现，不是必须重写  


## 自定义控件扩展任务菜单的项目目录
仿照官方文档中的'Task Menu Extension Example'写了一个项目  
备注：具体代码参见QT_project\custom_designer_menu  
```
custom_designer_menu
	│  tictactoe.pro 项目管理文件
	│  tictactoe.pro.user
	│      
	├─tictactoe
	│  │  tictactoe.pri 控件项目文件
	│  │  
	│  ├─Headers
	│  │      tictactoe.h 控件头文件
	│  │      
	│  └─Sources
	│         tictactoe.cpp 控件源文件
	│          
	├─Resources
	│      icons.qrc 资源集合文件
	│
	├─Headers
	│      tictactoeplugin.h
	│      tictactoetaskmenu.h
	│      tictactoetaskmenufactory.h
	└─Sources
	       tictactoeplugin.cpp 
	       tictactoetaskmenu.cpp
	       tictactoetaskmenufactory.cpp
```
项目中一共包含四个类：  
1. TicTacToe
实现控件本身的各种定义  

2. TicTacToePlugin
将控件扩展为qt designer插件的类  
这里和一般自定义控件项目的代码基本相同，除了要对initialize()函数进行重写  

3. TicTacToeTaskMenuFactory
生成一个可以在qt designer中创建扩展任务菜单的factory  
在这里对QExtensionFactory类中的createExtension()函数进行重写  

4. TicTacToeTaskMenu
实现任务菜单扩展的选项，定义action以及action关联的槽函数  
在这里对QDesignerTaskMenuExtension类的 preferredEditAction()函数和taskActions()函数进行重写  


## 待研究的问题
1. 示例中只向菜单中添加了一个自定义选项，实际上应该是可以添加多个选项的，
具体的实现方式还没有测试过  
2. 关于在QT designer中读取鼠标位置的问题
经过实际测试，在QT designer中，点击鼠标无法触发mousePressEvent(QMouseEvent \*event)函数  
所以用event -> pos()和event -> globalPos()读到的坐标一直都是(0, 0)  
使用QCursor::pos()可以在QT designer中读取到鼠标的位置，但无法感知什么时候点击了鼠标右键  
如果把QCursor::pos()也写在mousePressEvent()函数里面，那同样无法被触发  
综上，现在没找到办法可以在QT designer中读取鼠标点击右键时的位置  