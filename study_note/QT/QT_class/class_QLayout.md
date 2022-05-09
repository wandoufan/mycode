# QLayout

## 基本功能
QLayout是Qt中所有界面布局相关类的抽象基类，提供界面布局管理功能  
备注：QLayout是一个抽象基类，一般不直接实例化，主要用来提供公共函数  
父类：QObject、QLayoutItem  
子类：QBoxLayout、QFormLayout、QGridLayout、QStackedLayout  


## 常用成员变量
1. sizeConstraint : SizeConstraint
这个属性设置layout的resize模式，默认模式为SetDefaultConstraint  
1.1 QLayout::SizeConstraint sizeConstraint() const  
1.2 void setSizeConstraint(QLayout::SizeConstraint)  

2. spacing : int
这个属性设置layout中widget之间的间距，默认为7  
如果没有特别设置间距，则间距值一般继承自父类  
对于QGridLayout和QFormLayout可以设置不同的水平间距和垂直间距，这种情况下，spacing()返回-1  
2.1 int spacing() const 
2.2 void setSpacing(int)


## 常用公共函数：边框间隙设置
备注：setMargin(int margin)函数有同样的功能，但已经过时，不再使用  
1. void QLayout::setContentsMargins(const QMargins &margins)
设置边框间隙的大小  
默认情况下，Layout包含的组件和边框之间有一个间隙(11个像素的间距)  

2. void QLayout::setContentsMargins(int left, int top, int right, int bottom)
设置边框间隙的大小  
```
gridlayout -> setContentsMargins(10, 10, 10, 10);
```

3. QMargins QLayout::contentsMargins() const
返回边框间隙，在绝大多数平台上，间隙值都是11  

4. void QLayout::getContentsMargins(int \*left, int \*top, int \*right, int \*bottom) const
返回边框间隙，在绝大多数平台上，间隙值都是11  


## 常用公共函数：管理layout中的子widget
1. void QLayout::addWidget(QWidget \*w)
向当前的Layout中添加一个Widget组件  

2. void QLayout::removeWidget(QWidget \*widget)
从layout中删除一个Widget组件  

3. QWidget \*QLayout::parentWidget() const
返回当前layout的父类  

4. QLayoutItem \*QLayout::replaceWidget(QWidget \*from, QWidget \*to, Qt::FindChildOptions options = Qt::FindChildrenRecursively)
替换layout中的widget  

5. [virtual] int QLayout::indexOf(QWidget \*widget) const
返回layout中widget的序号，序号从0开始，和widget添加到layout中的顺序一致  
如果没有找到widget，则返回-1  

6. [pure virtual] int QLayout::count() const
返回Layout中包含控件的个数  
备注：这是一个纯虚函数，但测试可以调用  


## 常用公共函数：设置layout中的item
这些函数不常用，不用管了  

