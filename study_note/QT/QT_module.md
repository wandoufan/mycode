# QT中的组件

----------------------------/*常用的组件*/-------------------------------

## 备注
1. QT中每一个组件都对应一个类，例如SpinBox组件对应QSpinBox类
2. checkBox(方块勾选)和radioButton(圆圈勾选)两种组件之间的区别：
多个checkBox可以同时选择，多个radioButton只能选择其中一个  
3. QSlider、QScrollBar 和 Qdial 3个组件都从QAbstractSlider继承而来，有一些共有的属性  

## ui
ui是QT中的一个指针，通过ui可以访问到UI界面中设置的所有组件  
使用方法为：ui -> objectName -> func();
```
ui -> textBrowser -> setText(str); //将str显示出来
```
注意：ui指针只能在QT类的成员方法中使用，外部函数无法调用ui指针，否则报错ui指针不识别  
其中，QT类指三大基类和继承于三大基类的自定义子类  
```
// 例如，自定义的Widget_cal类继承于QWidget类，其成员方法中可以使用ui指针
class Widget_cal : public QWidget
{
	...
}
```


## Spin Box / Double Spin Box
Spin Box和Double Spin Box是常用的用于数字相关的输入组件  
Spin Box组件用于整数的显示和输入，可以设置进制，对应QSpinBox类  
Double Spin Box组件用于浮点数的显示和输入，可以设置显示小数位数，对应QDoubleSpinBox类  
使用QSpinBox和QDoubleSpinBox读取和设置数值时，无需做字符串和数值之间的转换，也无需做进制转换，其显示效果在设置好后会自动生成，因此非常适合数值的输入输出  
**常用属性**
备注：QSpinBox和QDoubleSpinBox都是QAbstractSpinBox的子类，具有大多数相同的属性，只是参数类型不同  
备注：以下属性可以通过UI界面右下角的属性编辑器设置，也可以在代码中调用类的函数进行设置  
prefix		数字显示的前缀，例如'$'  
suffix		数字显示的后缀，例如'kg'  
minimum		数值范围的最小值，如0  
maximum		数值范围的最大值，如255  
singlestep	单击右侧上下调整按钮时的单步改变值，如设置为1或0.1  
value		当前显示的值  
displaylntegerBase	QSpinBox特有属性，显示整数使用的进制，例如2就表示二进制  
decimals	QDoubleSpinBox特有属性，显示数值的小数位数，例如2就显示两位小数  
**常用函数**
1. int value() 
读取组件中当前的输入值  
```
int number = ui -> spinBox_2 -> value();
```
2. void setValue(int/double val)
向组件中设置数值  
```
ui -> spinBox_2 -> setValue(number);
```
3. int displayIntegerBase()
读取组件当前的进制设置  
```
base = ui -> spinBox_5 -> displayIntegerBase();
```
4. void setDisplayIntegerBase(int base)
对组件的进制进行设置  
```
ui -> spinBox_2 -> setDisplayIntegerBase(base);
```


## Dial
Dial组件是一个表盘式数值输入组件，可以通过转动表针来获得输入值，对应QDial类  
**常用属性**


## Slider
Slider组件提供一个垂直或水平的滑动条，通过滑动来设置数值，可以用于数值输入，对应QSlider类  
**常用属性**


## Scroll Bar
Scroll Bar组件提供一个卷滚条，类似于Slider组件，还可以用于卷滚显示区域，对应QScrollBar类  
**常用属性**


## plainTextEdit

## TextEdit



1. 实际使用中发现：
如果选择plainTextEdit组件，则设置文本的下划线、斜体、粗体都正常
但如果选择了TextEdit组件，只有设置文本下划线是正常的
文本的斜体和粗体只能在程序运行之后再写入文字才能生效，且生效仅限一次
在编译之前就写好的文字则无法生效
2. 
3. textBrowser组件可以通过setText(str)方法把内容显示输出出来  


----------------------------/*组件的属性*/-------------------------------

## objectName属性
对于窗体上创建出的每一个组件，都有一个objectName属性作为组件实例的名称  
具体属性值由系统自动创建，一般按照组件创建顺序来命名，例如checkBox、checkBox_2、checkBox_3  
objectName作为组件的唯一标识，每个组件的objectName都不相同  
objectName需要在设计程序之前设置好，设置好后不要再改动，否则代码也要相应改动  


## checkable属性
1. 基本概念
对于继承于QAbstractButton类的Button组件都有一个checkable属性，用来设置按钮状态  
未勾选checkable时，Button为触发按钮(trigger button)，按下去马上弹起来  
勾选checkable后，Button变成切换按钮(toggle button)，可以有两种状态：按下/弹起  
备注：toggle可以理解为开关，可以勾选为开或关的状态；而trigger可以理解为扳机，只点击一次  
2. 大部分Button的checkable默认是不选中的，包括：  
pushButton、toolButton  
3. 少部分Button的checkable默认是选中的，包括： 
radioButton、checkBox  