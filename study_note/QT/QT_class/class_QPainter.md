# QPainter

## 基本功能
QPainter可以在widgets和其他绘图设备上进行绘画  
父类：无  
子类：QStylePainter  
使用时在.pro文件中要添加  
```
QT += gui
```


## 详细功能


## 注意事项
1. 一个绘画对象device一次只能被一个painter来绘图
```
painter->begin(myWidget);
painter2->begin(myWidget); // impossible - only one painter at a time
```

2. 不支持在QImage对象上用QImage::Format_Indexed8格式来进行绘图

3. 画笔QPen和画刷QBrush可以同时设置



## 代码示例
1. 定义一个自定义控件，对QWidget::paintEvent()方法进行重写
```
void myLabel::paintEvent(QPaintEvent *event)
{
    QLabel::paintEvent(event);//先调用父类的paintEvent为了显示'背景'!!!
    QPainter painter(this);
    painter.setPen(QPen(Qt::red,2));
    painter.drawRect(QRect(x,y,w,h));
}
```

2. 在一个QImage上画矩形方框
```
QImage image("D:/1.png");
QPainter painter(&image);
painter.setPen(QPen(Qt::red, 1));
painter.drawRect(QRect(20, 20, 30, 60));
```

3. 画一个文本内容，并设置文本的背景颜色为黄色
```
QBrush brush(Qt::yellow, Qt::SolidPattern);
painter.setBackgroundMode(Qt::OpaqueMode);
painter.setBackground(brush);
painter.drawText(50, 50, "test");
```


## 构造函数
1. QPainter::QPainter(QPaintDevice \*device)
这个构造函数会替你调用begin()方法  
备注：使用这个构造函数，如果初始化失败了，也不会获得反馈  

2. QPainter::QPainter()
构造一个空的QPainter对象，没有指定绘图对象，后面需要自己去调用begin()方法  

--------------------------基本设置---------------------------

## 常用公共函数：初始化
1. bool QPainter::begin(QPaintDevice \*device)
开始在device对象上进行绘图，返回初始化是否成功  
注意：调用begin()之后，前面所有的绘图设置(如setPen()、setBrush())都会被重置为默认值  
在调用begin()方法时的常见错误：  
```
painter->begin(0); // impossible - paint device cannot be 0

QPixmap image(0, 0);
painter->begin(&image); // impossible - image.isNull() == true;

painter->begin(myWidget);
painter2->begin(myWidget); // impossible - only one painter at a time
```

2. bool QPainter::end()
结束绘画，释放资源  
析构函数会自动调用end()方法，一般不需要手动调用  


--------------------------绘图设置---------------------------
## 常用公共函数：设置背景区域
1. void QPainter::setBackground(const QBrush &brush)
背景区域是指文本内容、断点线条、位图等  
备注：这个设置对透明的背景模式无效  
```
painter.setBackgroundMode(Qt::OpaqueMode);
painter.setBackground(brush);
```

2. void QPainter::setBackgroundMode(Qt::BGMode mode)
设置背景模式，默认为透明的背景模式(Qt::TransparentMode)  
如果想要让背景颜色生效，就必须设置为Qt::OpaqueMode模式  


## 常用公共函数：设置画刷(对一个区域进行填充)
1. void QPainter::setBrush(const QBrush &brush)

2. void QPainter::setBrush(Qt::BrushStyle style)
重载函数  
设置画刷的风格，颜色为black  

3. void QPainter::setBrushOrigin(const QPointF &position)
设置画刷的开始位置  
备注：没搞明白这个函数有什么作用，好像不进行设置也不影响  

4. void QPainter::setBrushOrigin(int x, int y)
重载函数  

5. void QPainter::setBrushOrigin(const QPoint &position)
重载函数  


## 常用公共函数：设置画笔(对文字和线条进行设置)
1. void QPainter::setPen(const QPen &pen)
pen参数定义了画图的线条，以及文本的颜色  

2. void QPainter::setPen(const QColor &color)
重载函数  
设置线条的颜色，线条宽度为1，风格为Qt::SolidLine  

3. void QPainter::setPen(Qt::PenStyle style)
重载函数  
设置线条的风格，线条宽度为1，颜色为black  


--------------------------绘图内容---------------------------

## 常用公共函数：画椭圆形
1. void QPainter::drawEllipse(const QRectF &rectangle)

2. void QPainter::drawEllipse(const QRect &rectangle)

3. void QPainter::drawEllipse(int x, int y, int width, int height)

4. void QPainter::drawEllipse(const QPointF &center, qreal rx, qreal ry)

5. void QPainter::drawEllipse(const QPoint &center, int rx, int ry)


## 常用公共函数：画矩形方框
1. void QPainter::drawRect(const QRectF &rectangle)
用当前设置好的pen和brush来画矩形方框

2. void QPainter::drawRect(const QRect &rectangle)
重载函数  

3. void QPainter::drawRect(int x, int y, int width, int height)
重载函数  

4. void QPainter::drawRects(const QRectF \*rectangles, int rectCount)
画多个矩形方框  

5. void QPainter::drawRects(const QVector<QRectF> &rectangles)
重载函数  

6. void QPainter::drawRects(const QRect \*rectangles, int rectCount)
重载函数  


## 常用公共函数：画文本内容
1. void QPainter::drawText(const QPointF &position, const QString &text)
position参数指定文本开始的位置  
注意：这个函数无法处理换行符'\n'，也就没办法画出多行文本  

2. void QPainter::drawText(const QPoint &position, const QString &text)

3. void QPainter::drawText(int x, int y, const QString &text)

4. void QPainter::drawText(const QRectF &rectangle, int flags, const QString &text, QRectF \*boundingRect = nullptr)
rectangle参数指定文本显示的区域  
flag参数指定文本的居中方式和显示方式等  
备注：flag的取值来自于enum Qt::AlignmentFlag和enum Qt::TextFlag，详见帮助文档  
注意：这个函数画出的文本内容可以用'\n'来进行换行  
```
painter.drawText(rect, Qt::AlignCenter, tr("Qt\nProject"));
```

5. void QPainter::drawText(const QRect &rectangle, int flags, const QString &text, QRect \*boundingRect = nullptr)

6. void QPainter::drawText(int x, int y, int width, int height, int flags, const QString &text, QRect \*boundingRect = nullptr)

7. void QPainter::drawText(const QRectF &rectangle, const QString &text, const QTextOption &option = QTextOption())