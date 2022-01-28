# Qt中的界面布局

## 基本信息
使用layout相关的类需要在.pro文件中添加：  
```
QT += widgets
```
备注：Qt中没有layout模块，只是一些相关的类  


## Layout相关类的继承关系
1. Vertical Layout：垂直方向布局，组件自动在垂直方向上分布  
2. Horizontal Layout：水平方向布局，组件自动在水平方向上分布  
3. Grid Layout：网格状布局，网状布局大小改变时，每个网格的大小都改变  
4. Form Layout：窗体布局，与网格状布局类似，但是只有最右侧的一列网格会改变大小  
```
QLayout
	├─QBoxLayout
	│  ├─QHBoxLayout 将所有Widget组件水平排列
	│  └─QVBoxLayout 将所有Widget组件垂直排列
	├─QFormLayout 管理Input Widget组件和与它们关联的labels
	├─QGridLayout 将所有Widget组件以网格状排列
	└─QStackedLayout 一次显示一个组件(组件堆叠在一起，只显示最上面组件)
```
其中，QGridLayout是最常用的，优先使用这个  


## 关于layout的显示问题
正常情况下，在QWidget，QDialog里面使用setLayout()方法之后就可以直接显示出布局  
但实际测试发现，如果是在QMainWindow里面使用setLayout()方法后没有任何反应  
虽然QMainWindow也是QWidget的子类，但主窗口有自己的界面布局，因此不支持设置自定义的layout  
解决办法：  
在QMainWindow中添加一个QWidget，然后对这个QWidget设置布局  
```
QGridLayout * gridlayout = new QGridLayout;
QLabel * label1 = new QLabel("label1");
QLabel * label2 = new QLabel("label2");
QLabel * label3 = new QLabel("label3");
QLabel * label4 = new QLabel("label4");
gridlayout -> addWidget(label1, 0, 0);
gridlayout -> addWidget(label2, 0, 1);
gridlayout -> addWidget(label3, 1, 0);
gridlayout -> addWidget(label4, 1, 1);
QWidget * widget = new QWidget;
widget -> setLayout(gridlayout);
this -> setCentralWidget(widget);//this是一个QMainWindow
```


## 注意事项
1. 当代码中出现多个layout对象时
如果都带有this指针(指明了父对象为当前窗口)，则只会显示出现最前面的那个layout  
如果只有一个带有this指针，则只会显示带有this指针的这个layout  
