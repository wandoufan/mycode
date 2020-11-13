# QT中的组件

----------------------------/*常用的组件*/-------------------------------

## 备注
1. QT中每一个组件都对应一个类，例如SpinBox组件对应QSpinBox类
2. checkBox(方块勾选)和radioButton(圆圈勾选)两种组件之间的区别：
多个checkBox可以同时选择，多个radioButton只能选择其中一个  
3. 组件的各种属性可以通过UI界面右下角的属性编辑器设置，也可以在代码中调用类的函数进行设置
一般用来设置属性的函数都以set开头，例如setValue()  
4. 可以用'object_name-> metaObject()->className();'来查看当前对象的类型  

## 使用中发现
1. 如果选择plainTextEdit组件，则设置文本的下划线、斜体、粗体都正常
但如果选择了TextEdit组件，只有设置文本下划线是正常的
文本的斜体和粗体只能在程序运行之后再写入文字才能生效，且生效仅限一次
在编译之前就写好的文字则无法生效
2. ui -> lineEdit -> text();方法可以把文本框的内容读取出来，返回一个QString
3. textBrowser组件可以通过setText(str)方法把内容显示输出出来  
4. 代码中经常报错找不到组件，实际有这个组件，可能是系统没有及时认出来，可以对项目进行'清除'操作


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


## QAbstractButton
QAbstractButton类是所有widgets按钮的抽象基类，给按钮提供公用的函数功能  
QAbstractButton是QWidget类的子类  
QAbstractButton是QCheckBox, QPushButton, QRadioButton, QToolButton的父类  
1. isDown()
表示按钮button是否是pressed down按下的  
2. isChecked()
表示按钮是否被检查或者标记切换的  
只有可检查和切换（标记）的按钮可以标记或者取消标记checked or unchecked  
3. isEnabled()
表示按钮是否可以被用户点按  
4. setAutoRepeat()
设置按钮是否当用户长按按钮可以auto-repeat（自动重复执行）  
属性autoRepeatDelay和autoRepeatInterval定义了如何重复响应执行  
5. setCheckable()
设置按钮是否可切换或者标记的  


## Spin Box / Double Spin Box
Spin Box和Double Spin Box是常用的用于数字相关的输入组件  
Spin Box组件用于整数的显示和输入，可以设置进制，对应QSpinBox类  
Double Spin Box组件用于浮点数的显示和输入，可以设置显示小数位数，对应QDoubleSpinBox类  
使用QSpinBox和QDoubleSpinBox读取和设置数值时，无需做字符串和数值之间的转换，也无需做进制转换，其显示效果在设置好后会自动生成，因此非常适合数值的输入输出  
**常用属性**
备注：QSpinBox和QDoubleSpinBox都是QAbstractSpinBox的子类，具有大多数相同的属性，只是参数类型不同  
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


## AbstractSlider
AbstractSlider本身不是一个组件，QAbstractSlider是QSlider、QScrollBar和Qdial 3个的父类，提供了共有的基础属性  
**常用属性**
minimum			设置输入范围的最小值，默认为0  
maximum			设置输入范围的最大值，默认为99  
singleStep		设置单步长，拖动标尺上的滑块或按下左/右光标键时的最小变化数值，默认为1  
pageStep		在Slider上输入焦点，按PgUp或PgDn键时变化的数值，默认为10  
value			设置组件的当前值(minimum和maximum之内)，默认为0  
sliderPosition		设置滑块的位置，默认为0  
tracking		设置sliderPosition是否等同于value，默认为true  
orientation		设置Slider的方向，取值包括Qt::Horizontal(水平方向)和Qt::Vertical(垂直方向)，默认为水平方向  
invertedAppearance		设置显示方式是否反向，取值false时，水平的Slider 由左向右数值增大，默认为false  
invertedControls		设置反向按键控制，取值true时，按下PgUp或PgDn 按键时调整数值的反向相反，默认为false  


## Dial
Dial组件是一个表盘式数值输入组件，可以通过转动表针来获得输入值，对应QDial类  
**常用属性**
备注：QDial是QAbstractSlider的子类，具备QAbstractSlider提供的基础属性  
1. notches Visible		设置表盘的刻度是否可见，默认false  
2. notchTarget			表盘刻度间的间隔像素值，默认3.7  
3. warpping				设置表盘更细小的刻度是否可见，默认为false  


## Slider
Slider组件提供一个垂直或水平的滑动条，通过滑动来设置数值，可以用于数值输入，对应QSlider类  
**常用属性**
备注：Slider是QAbstractSlider的子类，具备QAbstractSlider提供的基础属性  
1. tickPosition		标尺刻度的显示位置，取值包括以下6种：  
QSlider::NoTicks：不显示刻度(默认)  
QSlider::TicksBothSides：标尺两侧都显示刻度  
QSlider::TicksAbove：标尺上方显示刻度  
QSlider::TicksBelow：标尺下方显示刻度  
QSlider::TicksLeft：标尺左侧显示刻度  
QSlider::TicksRight：标尺右侧显示刻度  
2. tickInterval		标尺刻度的间隔值，默认为0，此时会在singleStep和pageStep之间自动选择  


## Scroll Bar
Scroll Bar组件提供一个垂直或水平的卷滚条用于卷滚显示区域，类似于Slider组件，对应QScrollBar类  
**常用属性**
QScrollBar是QAbstractSlider的子类，只有基础属性，没有自己特有的属性  


## Progress Bar
Progress Bar组件提供一个进度条，常用于进度显示，对应QProgressBar类  
**常用属性**
minimum		设置最小值，默认为0  
maximum		设置最大值，默认为100  
value		设置当前值(minimum和maximum之内)，默认为24  
textVisible		设置是否显示进度百分百，默认true  
orientation		设置进度的填充方向为水平或垂直方向，默认为水平方向  
format			设置显示文字的格式，取值包括以下三种：  
'%p%'显示百分比(默认)  
'%v'显示当前值  
'%m'显示总步数  


## Date Time Edit
Date Time Edit是用来编辑和显示日期时间的组件，对应QDateTimeEdit类  
QDateTimeEdit是QTimeEdit和QDateEdit的父类，也是QAbstractSpinBox的子类  
**常用属性**
备注： datetime属性和date、time两个属性之间是互相关联的  
datetime			设置日期时间  
date				设置日期  
time				设置时间  
maximumDateTime		设置最大日期时间  
minimumDateTime		设置最小日期时间  
maximumDate			设置最大日期  
minimumDate			设置最小日期  
maximumTime			设置最大时间  
minimumTime			设置最小时间  
currentSection			设置当前输入光标所在的时间日期数据段，默认为YearSection  
例如，当前输入光标在YearSection段，就修改'年'的值  
currentSectionIndex		设置用序号表示的输入光标所在的段，默认为0  
calendarPopup			设置是否允许弹出一个日历选择框，默认为false  
displayFormat			设置日期时间数据的显示格式，默认为yyyy/M/d H:mm  
例如，一个日期时间数据就显示为'2016-11-02 08:23:46'  
```
字符		意义
d	天，不补零显示，1-31
dd	天，补零显示，01-31
M	月，不补零显示，1-12
MM	月，补零显示，01-12
yy	年，两位显示，00-99
yyyy	年，4位数字显示，如 2016
h	小时，不补零，0-23 或 1-12 (如果显示 AM/PM)
hh	小时，补零2位显示，00-23 或 01-12 (如果显示 AM/PM)
H	小时，不补零，0-23 (即使显示 AM/PM)
HH	小时，补零显示，00-23 (即使显示 AM/PM)
m	分钟，不补零，0-59
mm	分钟，补零显示，00-59
z	毫秒，不补零，0-999
zzz	毫秒，补零 3 位显示，000-999
AP或A	使用 AM/pm 显示
ap或a	使用 am/pm 显示
```


## Time Edit
Time Edit是用来编辑和显示时间的组件，对应QTimeEdit类  
QTimeEdit是QDateTimeEdit的子类，只有基础属性，没有自己特有的属性  


## Date Edit
Date Edit是用来编辑和显示日期的组件，对应QDateEdit类  
QDateEdit是QDateTimeEdit的子类，只有基础属性，没有自己特有的属性  



## Calendar Widget
Calendar Widget是用来编辑和显示日历的组件，对应QCalendarWidget类  
用户在日历组件上选择日期时会触发selectionChanged()，可以以此为信号创建槽函数  
```
void Widget_Time::on_calendarWidget_selectionChanged()
{
    //将日历上选择的日期写入到文本框中
    QDate user_date = ui -> calendarWidget -> selectedDate();
    QString date_str = user_date.toString("yyyy-MM-dd");
    ui -> select_date -> setText(date_str);
}
```

## plainTextEdit

## TextEdit






----------------------------/*组件的属性*/-------------------------------

## objectName属性
对于窗体上创建出的每一个组件，都有一个objectName属性作为组件实例的名称  
objectName作为组件的唯一标识，每个组件的objectName都不相同  
具体属性值由系统自动创建，一般按照组件创建顺序来命名，例如checkBox、checkBox_2、checkBox_3  
objectName也可以自定义命名，但需要在设计程序之前设置好，设置好后不要再改动，否则代码也要相应改动  


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