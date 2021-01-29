# QMouseEvent

## 基本功能
QMouseEvent提供了用来描述鼠标事件的参数，包括当前鼠标的位置  
有一个常用函数mousePressEvent，详见QT_function.md  
```
void QWidget::mousePressEvent(QMouseEvent \*event)
```


## 构造函数


## 常用函数
* QPoint QMouseEvent::pos() const
返回光标的位置坐标，这个坐标是相对于当前窗口的位置  
即窗口的左上角为(0, 0)，坐标值与窗口本身的位置无关  

* int QMouseEvent::x() const
位置的x坐标  

* int QMouseEvent::y() const
位置的y坐标  

* QPoint QMouseEvent::globalPos() const
返回光标的位置坐标，这个坐标是相对于显示屏的位置  
即显示屏的左上角为(0, 0)  

* int QMouseEvent::globalX() const
位置的x坐标  

* int QMouseEvent::globalY() const
位置的y坐标  

* Qt::MouseButton QMouseEvent::button() const
返回触发此次鼠标事件的按钮  
注意：对于鼠标移动事件，返回的总是Qt::NoButton  
```
//判断当前的操作是点击了鼠标右键
if(event -> button() ==  Qt::RightButton)
```



