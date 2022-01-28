# QGridLayout

## 基本功能
实现控件的网格状布局  
父类：QLayout  
子类：无  


## 注意事项
1. 创建gridlayout对象时，如果使用QGridLayout::QGridLayout()构造函数，这个对象没有父类  
采用下面两个方法都可以给它指定一个父类
```
//方法一
widget -> setLayout(gridlayout);
//方法二
layout -> addLayout(gridlayout);
```
在gridlayout对象有父类之前，可以对这个gridlayout对象添加控件或设置布局等，但都不会真正起作用  
这时候调用以下方法的返回值都是-1，等gridlayout对象有父类之后才会有真正的返回值  
```
qDebug() << gridlayout -> spacing();
qDebug() << gridlayout -> horizontalSpacing();
qDebug() << gridlayout -> verticalSpacing();
```
2. 在GridLayout中如果只添加了一个组件，则无论怎么参数设置，该组件都始终显示在GridLayout的中间  


## 关于设置GridLayout中控件的间距
设置控件间距的接口函数有很多  
setContentsMargins()可以设置控件与窗体边框之间的间距  
setSpacing()、setHorizontalSpacing()、setVerticalSpacing()可以设置控件之间的间距  
如果整个窗体处于拉伸状态，则设置间距的效果是看不出来的，控件的显示间距都大于设置的间距值  
只有当整个窗体压缩到最小时，设置的间距才能体现出效果  


## 代码示例
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
this -> setLayout(gridlayout);
```


## 构造函数
1. QGridLayout::QGridLayout()
新建一个空的gridlayout，这个gridlayout之后必须被添加到另一个layout中  
你可以在任意时候向这个gridlayout中添加子widget和子layout，但只有当这个gridlayout被添加到另一个layout的时候，才会真正去执行这个gridlayout布局  

2. QGridLayout::QGridLayout(QWidget \*parent)
新建一个gridlayout并指定一个widget作为父类，只有一行一列，当加入新元素时会自动扩展  
```
QGridLayout * gridlayout = new QGridLayout(widget);
```
这个效果等同于  
```
QGridLayout * gridlayout = new QGridLayout;
widget -> setLayout(gridlayout);
```


## 常用成员变量
1. horizontalSpacing : int
设个属性设置layout中widget和边框的水平间距，默认为7  
如果没有特别设置间距，则间距值一般继承自父类  
1.1 int horizontalSpacing() const  
1.2 void setHorizontalSpacing(int spacing)  

2. verticalSpacing : int
设个属性设置layout中widget和边框的垂直间距，默认为7  
如果没有特别设置间距，则间距值一般继承自父类  
2.1 int verticalSpacing() const
2.2 void setVerticalSpacing(int spacing)


## 常用公共函数：添加子widget
1. void QGridLayout::addWidget(QWidget \*widget, int row, int column, Qt::Alignment alignment = Qt::Alignment())
向QGridLayout中添加一个widget组件  
row参数和column参数分别设置行数和列数，其中，最左上角的位置为(0, 0)  
alignment参数用来设置widget组件在layout中的填充程度，详见namespace中enum Qt::AlignmentFlag  
alignment默认值为0，即控件为充满整个框架  
```
gridlayout -> addWidget(label1, 0, 0, Qt::AlignLeft | Qt::AlignVCenter);
gridlayout -> addWidget(label2, 1, 0, Qt::AlignRight | Qt::AlignVCenter);
gridlayout -> addWidget(label3, 2, 0, Qt::AlignCenter);
```
备注：向layout中添加pushbutton等组件时默认会把组件拉长(充满整个框架)，加上Qt::AlignHCenter参数后，组件就会缩短居中  

2. void QGridLayout::addWidget(QWidget \*widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = Qt::Alignment())
向QGridLayout中添加一个widget组件多次  
rowSpan和columnSpan参数设置添加的范围  


## 常用公共函数：添加子layout
1. void QGridLayout::addLayout(QLayout \*layout, int row, int column, Qt::Alignment alignment = Qt::Alignment())
向GridLayout中添加另外一个layout组件  
row参数和column参数分别设置行数和列数，其中，最左上角的位置为(0, 0)  
alignment参数用来设置子layout在父layout中的填充程度  
alignment默认值为0，即控件为充满整个框架  
任意非零的alignment参数都说明子layout不能充满整个框架，此时子layout的尺寸要由sizeHint()函数来确定  

2. void QGridLayout::addLayout(QLayout \*layout, int row, int column, int rowSpan, int columnSpan, Qt::Alignment alignment = Qt::Alignment())
向GridLayout中添加另外一个layout组件多次  
rowSpan和columnSpan参数设置添加的范围  


## 常用公共函数：设置UI显示效果
1. void QGridLayout::setRowStretch(int row, int stretch)
设置第row行的拉伸因子stretch，行号从0开始  
stretch默认为0，这里实际代表的是每行之间高度的比例系数  
当整个窗体进行拉伸时，每行就会按预设的拉伸因子进行显示  
当整个窗体缩到最小时，每行仍会按1:1显示  
例如，设置1到4行的高度比例为1:2:3:4  
```
gridlayout -> setRowStretch(0, 1);
gridlayout -> setRowStretch(1, 2);
gridlayout -> setRowStretch(2, 3);
gridlayout -> setRowStretch(3, 4);
```
注意：如果要实现上面的拉伸效果，layout中的控件需要进行如下设置  
```
label1 -> setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
label1 -> setMinimumSize(120, 50);
```
如果使用setFixedSize()设置控件尺寸，则每行之间仍是等比例显示，无法实现拉伸效果
```
label1 -> setFixedSize(120, 50);
```

2. void QGridLayout::setColumnStretch(int column, int stretch)
设置第column列的拉伸因子stretch，列号从0开始  
stretch默认为0，这里实际代表的是每列之间宽度的比例系数  

3. void QGridLayout::setRowMinimumHeight(int row, int minSize)
设置第row行的最低高度minSize，行号从0开始  
如果整个窗体处于拉伸状态，则设置最低高度的效果可能看不出来  
只有当整个窗体压缩到最小时，设置的最低高度才能体现出效果  

4. void QGridLayout::setColumnMinimumWidth(int column, int minSize)
设置第column列的最低宽度minSize，列号从0开始    


## 常用公共函数：查询layout信息
1. int QGridLayout::rowCount() const

2. int QGridLayout::columnCount() const

3. int QGridLayout::rowStretch(int row) const

4. int QGridLayout::columnStretch(int column) const

5. int QGridLayout::rowMinimumHeight(int row) const

6. int QGridLayout::columnMinimumWidth(int column) const


