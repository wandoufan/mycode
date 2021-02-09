# QMouseEvent

## 基本功能
QMouseEvent提供了用来描述鼠标事件的参数，包括当前鼠标的位置  
QMouseEvent的父类是QInputEvent  
备注：使用前在.pro文件中加入'QT += gui'  


## 使用说明
鼠标事件相关的函数，详见QT_function.md  
```
void QWidget::mousePressEvent(QMouseEvent \*event)
void QWidget::mouseReleaseEvent(QMouseEvent \*event)
void QWidget::mouseMoveEvent(QMouseEvent \*event)
void QWidget::mouseDoubleClickEvent(QMouseEvent \*event)
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


## QCursor和QMouseEvent获取的鼠标位置之间的区别
1. 使用位置
QMouseEvent::globalPos()一般用在mousePressEvent()等函数中，等到触发相应的mouse event后才会读取此时的鼠标位置坐标  
QCursor::pos()可以用在代码的任意位置，每次读的都是此刻鼠标所在的位置  
因此在代码的不同地方调用QCursor::pos()，读到的坐标可能不一样  
2. 读取数值
只有在代码的同一位置调用这两个函数，二者读到的坐标值才是一样的  
即QCursor::pos() == QMouseEvent::globalPos()  
```
void SkyplotWidget::mousePressEvent(QMouseEvent *event)
{
    if(event -> button() ==  Qt::RightButton)
    {
        //此时二者读到的坐标值相同
        mouse_pos = event -> pos();
        mouse_global_pos = event -> globalPos();
        global_point = QCursor::pos();
        widget_point = this -> mapFromGlobal(global_point);
        menu -> exec(mouse_global_pos);
    }
}
```
3. 在QT designer中使用
经过实际测试，在QT designer中，点击鼠标无法触发mousePressEvent(QMouseEvent \*event)函数  
所以用event -> pos()和event -> globalPos()读到的坐标一直都是(0, 0)  
使用QCursor::pos()可以在QT designer中读取到鼠标的位置，但无法感知什么时候点击了鼠标右键  
如果把QCursor::pos()也写在mousePressEvent()函数里面，那同样无法被触发  
综上，现在没找到办法可以在QT designer中读取鼠标点击右键时的位置  
