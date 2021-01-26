# QLayout

## 参考资料
https://blog.csdn.net/li162001/article/details/88126928

## 基本功能
QLayout是QT中所有控件几何属性设置相关类的基类，提供界面布局管理功能  
QLayout是一个抽象类，不能直接实例化，一般都是获取其子类的对象  
备注：使用前要在.pro文件中添加'QT += widgets'  
继承关系如下：  
```
QLayout
	├─QBoxLayout
	│  ├─QHBoxLayout 将所有Widget组件水平排列
	│  └─QVBoxLayout 将所有Widget组件垂直排列
	├─QFormLayout 管理Input Widget组件和与它们关联的labels
	├─QGridLayout 将所有Widget组件以网格状排列
	└─QStackedLayout 一次显示一个组件(组件堆叠在一起，只显示最上面组件)
```


## 注意事项
1. layout对象不需要调用show()函数即可默认显示(layout也没有这个成员方法)
2. 当代码中出现多个layout对象时
如果都带有this指针(指明了父对象为当前窗口)，则只会显示出现最前面的那个layout  
如果只有一个带有this指针，则只会显示带有this指针的这个layout  
3. 组件在layout中显示顺序、索引序号都是和组件添加到Layout中的顺序是一致的  
4. 在GridLayout中如果只添加了一个组件，则无论怎么参数设置，该组件都始终显示在GridLayout的中间  


## QLayout常用函数
备注：以下都是基类中的函数，子类中都可以使用  
1. void QLayout::setContentsMargins(int left, int top, int right, int bottom)
默认情况下，Layout包含的组件和边框之间有一个缝隙(11个像素的间距)  
可以用setContentsMargins来具体设置间距的大小  
备注：setMargin(int margin)函数有同样的功能，但已经过时，不再使用  
```
vlayout -> setContentsMargins(30, 30, 30, 30);
```
2. void QLayout::addWidget(QWidget \*w)
向当前的Layout中添加一个Widget组件，注意参数必须是指针类型  
```
vlayout -> addWidget(button1);
```
3. virtual int indexOf(QWidget \*widget) const
查询Layout中某个控件的索引，索引号从0开始计算  
索引序号与控件添加到Layout中的顺序是一致的  
```
int index = vlayout -> indexOf(button1);
```
4. virtual int count() const = 0
查询Layout中包含控件的个数
```
int count = vlayout -> count();
```


## QGridLayout常用函数
1. void QGridLayout::addLayout(QLayout \*layout, int row, int column, Qt::Alignment alignment = Qt::Alignment())
向一个QGridLayout类型的layout中添加一个layout组件  
row参数和column参数分别设置行数和列数  
其中，最左上角的位置为(0, 0)  
alignment参数用来设置子layout在父layout中的填充程度  
alignment默认值为0，即控件为充满整个框架  
任意非零的alignment参数都说明子layout不能充满整个框架，此时子layout的尺寸要由sizeHint()函数来确定  
```
glayout -> addLayout(vlayout, 1, 1);
```
2. void QGridLayout::addWidget(QWidget \*widget, int row, int column, Qt::Alignment alignment = Qt::Alignment())
向一个QGridLayout类型的layout中添加一个widget组件  
row参数和column参数分别设置行数和列数  
其中，最左上角的位置为(0, 0)  
alignment参数用来设置widget组件在layout中的填充程度  
alignment默认值为0，即控件为充满整个框架  
```
glayout -> addWidget(box1, 0, 0);
glayout -> addWidget(box2, 0, 1);
glayout -> addWidget(box3, 1, 0);
```

