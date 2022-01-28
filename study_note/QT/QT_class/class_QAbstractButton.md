# QAbstractButton

## 基本功能
QAbstractButton是所有widgets按钮的抽象基类，给按钮提供公用的函数功能  
父类：QWidget
子类：QCheckBox, QPushButton, QRadioButton, QToolButton


## 常用成员变量
1. autoExclusive : bool

2. autoRepeat : bool
这个属性设置当用户长按按钮时是否可以auto-repeat（自动重复执行）  
2.1 bool autoRepeat() const
2.2 void setAutoRepeat(bool)

3. autoRepeatDelay : int

4. autoRepeatInterval : int

5. checkable : bool
这个属性用来设置按钮的弹起模式，默认为false  
属性为false，Button为触发按钮(trigger button)，按下去马上弹起来  
属性为true时，Button变成切换按钮(toggle button)，可以有两种状态：按下/弹起  
备注：toggle可以理解为开关，可以勾选为开或关的状态；而trigger可以理解为扳机，只点击一次  
大部分Button的checkable属性默认为false，包括：pushButton、toolButton  
少部分Button的checkable属性默认为true，包括：radioButton、checkBox  
5.1 bool isCheckable() const
5.2 void setCheckable(bool)

6. checked : bool
这个属性用来设置按钮是否为选中状态，默认为false  
备注：只有checkable属性为true的按钮的checked属性才可能为true  
6.1 bool isChecked() const
6.2 void setChecked(bool)

7. down : bool
这个属性用来设置按钮是否被按下，默认为false  
如果是在代码中把这个属性设置为true，则pressed()和clicked()信号不会被发出来  
7.1 bool isDown() const
7.2 void setDown(bool)

8. icon : QIcon
这个属性用来设置按钮图标  
8.1 QIcon icon() const
8.2 void setIcon(const QIcon &icon)

9. iconSize : QSize
这个属性用来设置按钮图标的尺寸  
9.1 QSize iconSize() const
9.2 void setIconSize(const QSize &size)

10. shortcut : QKeySequence

11. text : QString
这个属性用来设置图表的文本内容，没有默认文本  
11.1 QString text() const
11.2 void setText(const QString &text)


## 常用公共函数
无


## 信号函数
1. [signal] void QAbstractButton::clicked(bool checked = false)

2. [signal] void QAbstractButton::pressed()

3. [signal] void QAbstractButton::released()

4. [signal] void QAbstractButton::toggled(bool checked)
当一个checkable属性为true的按钮的选中状态发生改变时会发出toggled()信号  