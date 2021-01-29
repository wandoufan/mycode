## QPalette

## 基本功能
Qpalette(调色板)类是专门用于管理组件的外观颜色的类  
每个组件都有一个palette属性，可以用来进行颜色相关的设置  
注意：在代码中设置组件的颜色后不会立刻反映在UI设计界面上，必须等程序运行后才能看到效果  


## 使用setStyleSheet函数来设置组件颜色
使用QPalette设置颜色时步骤太多，可以选择使用setStyleSheet，代码更简洁  
setStyleSheet函数的参数是一个qss语法的字符串  
外观类组件的对象都可以调用setStyleSheet函数  
```
//设置字体颜色
label->setStyleSheet("color: blue");
//设置背景颜色
label1 -> setStyleSheet("background-color:blue;");
label->setStyleSheet("QLabel{background:#000000;}");
label->setStyleSheet("QLabel{background-color:rgb(200,101,102);}");
```
备注：如果qss语句写错了，设置不会生效，但程序也不会有报错  


## QPalette使用示例
例1
```
QPalette plet = ui -> plainTextEdit -> palette();
plet.setColor(QPalette::Text, Qt::blue);//设置窗口中文字的颜色
ui -> plainTextEdit -> setPalette(plet);
```
例2
```
Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
	ui->setupUi(this);
	QPalette BackGroundColor = this -> palette();
	BackGroundColor.setColor(QPalette::Background, QColor(10, 100 , 50, 255));//设置Widget窗口的背景颜色
	this -> setPalette(BackGroundColor);
}
```


## 常用参数
1. 设置颜色显示区域的参数包括：  
QPalette::Base 设置文本输入窗口部件的背景色  
QPalette::Text 设置文本输入窗口中文字的颜色  
QPalette:WindowText 通常指窗口看不见的前景色  
QPalette::Button 指按钮窗口部件的背景色  
QPalette::ButtonText 指按钮窗口部件的前景色  
QPalette::Background 背景色  
QPalette::Foreground 前景色  
注意：设置Widget等窗口的背景颜色用QPalette::Background，设置QtextEdit等文本输入框的背景颜色用QPalette::Base  


## enum Qt::GlobalColor
颜色也可以用下面的参数进行赋值  
```
Constant  Value  Description

Qt::white  3  White (#ffffff)
Qt::black  2  Black (#000000)
Qt::red  7  Red (#ff0000)
Qt::darkRed  13  Dark red (#800000)
Qt::green  8  Green (#00ff00) 
Qt::darkGreen  14  Dark green (#008000) 
Qt::blue  9  Blue (#0000ff) 
Qt::darkBlue  15  Dark blue (#000080) 
Qt::cyan  10  Cyan (#00ffff) 
Qt::darkCyan  16  Dark cyan (#008080) 
Qt::magenta  11  Magenta (#ff00ff) 
Qt::darkMagenta  17  Dark magenta (#800080) 
Qt::yellow  12  Yellow (#ffff00) 
Qt::darkYellow  18  Dark yellow (#808000) 
Qt::gray  5  Gray (#a0a0a4) 
Qt::darkGray  4  Dark gray (#808080) 
Qt::lightGray  6  Light gray (#c0c0c0) 
```
