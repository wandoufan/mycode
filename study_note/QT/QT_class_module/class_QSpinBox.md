# QSpinBox/QDoubleSpinBox

## 基本功能
Spin Box和Double Spin Box是常用的用于数字相关的输入组件  
Spin Box组件用于整数的显示和输入，可以设置进制，对应QSpinBox类  
Double Spin Box组件用于浮点数的显示和输入，可以设置显示小数位数，对应QDoubleSpinBox类  
使用QSpinBox和QDoubleSpinBox读取和设置数值时，无需做字符串和数值之间的转换，也无需做进制转换，其显示效果在设置好后会自动生成，因此非常适合数值的输入输出  


## 常用属性
备注：QSpinBox和QDoubleSpinBox都是QAbstractSpinBox的子类，具有大多数相同的属性，只是参数类型不同  
```
prefix		数字显示的前缀，例如'$'  
suffix		数字显示的后缀，例如'kg'  
minimum		数值范围的最小值，如0  
maximum		数值范围的最大值，如255  
singlestep	单击右侧上下调整按钮时的单步改变值，如设置为1或0.1  
value		当前显示的值  
displaylntegerBase	QSpinBox特有属性，显示整数使用的进制，例如2就表示二进制  
decimals	QDoubleSpinBox特有属性，显示数值的小数位数，例如2就显示两位小数  
```


## 常用函数
* int value()
读取组件中当前的输入值  
```
int number = ui -> spinBox_2 -> value();
```
* void setValue(int/double val)
向组件中设置数值  
```
ui -> spinBox_2 -> setValue(number);
```
* int displayIntegerBase()
读取组件当前的进制设置  
```
base = ui -> spinBox_5 -> displayIntegerBase();
```
* void setDisplayIntegerBase(int base)
对组件的进制进行设置  
```
ui -> spinBox_2 -> setDisplayIntegerBase(base);
```

* int maximum() const
读取最大范围

* void setMaximum(int max)
设置最大范围

*  int minimum() const
读取最小范围

* void setMinimum(int min)
设置最小范围

* void QSpinBox::setRange(int minimum, int maximum)
设置最大和最小范围

* int singleStep() const
读取步长

* void setSingleStep(int val)
设置步长