# QCursor

## 基本功能
QCursor主要用来创建鼠标光标对象，将光标和特定的widget关联起来，然后获取或设置鼠标光标的位置参数  
关于光标的形状，详细参见帮助手册中的"enum Qt::CursorShape"  
备注：QT提供了一系列标准的光标形状，也可以自定义光标的形状  
备注：使用前在.pro文件中加入'QT += gui'  


## 使用说明
要将一个光标和一个widget关联起来，使用QWidget::setCursor()函数
```
void QWidget::setCursor(const QCursor &)
```
要将一个光标和所有widget关联起来(一般是临时性的)，使用QGuiApplication::setOverrideCursor()函数  
```
[static] void QGuiApplication::setOverrideCursor(const QCursor &cursor)
```


## 公共静态函数
1. [static] QPoint QCursor::pos()
用全局坐标返回光标在主屏幕的位置  
可以调用'QWidget::mapFromGlobal()'函数把全局坐标映射为widget中的坐标  
注意：位置坐标是从windows窗口系统中查询的，如果mouse事件是由其他途径产生的，那么这些虚假的mouse move事件不会被反映到返回的坐标值中  
备注：如果一个平台没有window窗口系统或不支持光标，则返回的位置是基于QWindowSystemInterface产生的mouse move事件  

2. [static] QPoint QCursor::pos(const QScreen \*screen)
用全局坐标返回光标在指定屏幕的位置  
可以调用'QWidget::mapFromGlobal()'函数把全局坐标映射为widget中的坐标  

3. [static] void QCursor::setPos(int x, int y)
用全局坐标将光标移动到主屏幕的指定位置  
可以调用'QWidget::mapToGlobal()'函数把widget中的坐标映射为全局坐标  

4. [static] void QCursor::setPos(const QPoint &p)
这是一个重载函数，用QPoint来传递坐标位置  

5. [static] void QCursor::setPos(QScreen \*screen, int x, int y)
用全局坐标将光标移动到指定屏幕的指定位置  
可以调用'QWidget::mapToGlobal()'函数把widget中的坐标映射为全局坐标  

6. [static] void QCursor::setPos(QScreen \*screen, const QPoint &p)
这是一个重载函数，用QPoint来传递坐标位置  


## 构造函数
```
QCursor(QCursor &&other)

QCursor(const QCursor &c)

QCursor(const QPixmap &pixmap, int hotX = -1, int hotY = -1)

QCursor(const QBitmap &bitmap, const QBitmap &mask, int hotX = -1, int hotY = -1)

QCursor(Qt::CursorShape shape)

QCursor()
```

## 常用函数
* void setShape(Qt::CursorShape shape)
设置光标的形状  

* Qt::CursorShape shape() const
返回当前光标的形状  
