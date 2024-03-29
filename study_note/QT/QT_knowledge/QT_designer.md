# QT designer

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
7. 输出面板(最下方)  
输出面板包括了问题、应用程序输出、编译输出等多个部分的程序运行信息  
其中应用程序输出可以查看到程序运行的中间结果，常用来进行代码调试  


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

