# QPainter

## 基本功能
QPainter可以在widgets和其他绘图设备上进行绘画  
所有支持QPainter绘图的设备详见QPaintDevice  
父类：无  
子类：QStylePainter  
使用时在.pro文件中要添加  
```
QT += gui
```


## 详细功能
如果需要绘画出复杂的形状，先自己定义一个QPainterPath，然后使用drawPath()方法  


## 注意事项
1. 一个绘画对象device一次只能被一个painter来绘图
```
painter->begin(myWidget);
painter2->begin(myWidget); // impossible - only one painter at a time
```

2. 不支持在QImage对象上用QImage::Format_Indexed8格式来进行绘图

3. 画笔QPen和画刷QBrush可以同时设置

4. 如果绘图设备是一个widget，QPainter只能被用在paintEvent()方法内部  


## 关于在QLabel上绘图的问题
1. 问题描述
由于QLabel等控件的绘图事件会被Qt默认过滤掉，因此一般不能直接在QLabel等控件上进行绘图  
如果在代码中直接对QLabel绘图会产生如下报错：  
```
QWidget::paintEngine: Should no longer be called
QPainter::begin: Paint device returned engine == 0, type: 1
QPainter::setPen: Painter not active
```
2. 错误示例
示例1：直接在自定义函数中对QLabel绘图  
```
void MainWindow::test1()
{
    QPainter painter(ui -> label);
    painter.setPen(QPen(Qt::red, 1));
    painter.drawRect(QRect(20, 20, 30, 60));
}
```
示例2：对继承的paintEvent()方法进行重定义，在方法中对QLabel绘图  
备注：网上有使用这种方法的，但实际测试，还是有同样的报错  
```
void MainWindow::paintEvent(QPaintEvent *event)
{
    QPainter painter(ui -> label);
    painter.setPen(QPen(Qt::red, 1));
    painter.drawRect(QRect(20, 20, 30, 60));
}
```
3. 解决方法一
定义一个继承于QLable的控件，对QWidget::paintEvent()方法进行重写  
```
void MyLabel::paintEvent(QPaintEvent *event)
{
    QLabel::paintEvent(event);//先调用父类的paintEvent为了显示'背景'!!!
    QPainter painter(this);
    painter.setPen(QPen(Qt::red,2));
    painter.drawRect(QRect(x,y,w,h));
}
```
4. 解决方法二
通过事件过滤器eventFilter或者事件函数event来对QLabel控件的绘图事件进行捕获，并在捕获到绘图事件QEvent::Paint后进行绘图操作  
```
//在头文件中定义函数
public:
    //eventFilter()是从QObject继承过来的虚函数
    bool eventFilter(QObject *watched, QEvent *event) override;
    void drawTest();

//构造函数
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    //在需要过滤事件的控件上安装eventFilter
    ui -> label -> installEventFilter(this);
}

//对eventFilter()重定义
bool MainWindow::eventFilter(QObject *watched, QEvent *event)
{
    if(watched == ui -> label && event -> type() == QEvent::Paint)
    {
        drawTest();
        return true;
    }
    else
    {
        return QWidget::eventFilter(watched, event);
    }
}

//对QLabel进行绘图
void MainWindow::drawTest()
{
    QPainter painter(ui -> label);
    painter.setPen(QPen(Qt::red, 2));
    painter.drawRect(QRect(20, 20, 30, 60));
}
```


## 代码示例
1. 在一个QLabe上画出图片
备注：QPainter不能直接在QLable上绘图  
```
QPainter painter(ui -> label);
QImage image("D:/1.png");
painter.drawImage(0, 0, image);
```

2. 在一个QImage上画矩形方框
```
QImage image("D:/1.png");
QPainter painter(&image);
painter.setPen(QPen(Qt::red, 1));
painter.drawRect(QRect(20, 20, 30, 60));
ui -> label -> setPixmap(QPixmap::fromImage(image));
```

3. 画一个文本内容，并设置文本的背景颜色为黄色
```
QBrush brush(Qt::yellow, Qt::SolidPattern);
painter.setBackgroundMode(Qt::OpaqueMode);
painter.setBackground(brush);
painter.drawText(50, 50, "test");
```

4. 使用QPainter将图片/文档转换为pdf
详见class_QPdfWriter.md



--------------------------基本设置---------------------------

## 构造函数
1. QPainter::QPainter(QPaintDevice \*device)
这个构造函数会替你调用begin()方法  
备注：使用这个构造函数，如果初始化失败了，也不会获得反馈  

2. QPainter::QPainter()
构造一个空的QPainter对象，没有指定绘图对象，后面需要自己去调用begin()方法  


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
结束绘画，释放绘画中用到的资源  
备注：析构函数会自动调用end()方法，一般不需要手动调用  

3. void QPainter::beginNativePainting()

4. void QPainter::endNativePainting()


--------------------------获取信息---------------------------

## 常用公共函数：获取基本信息
1. QPaintDevice \*QPainter::device() const

2. bool QPainter::isActive() const
判断painter是否处于active状态  
例如，在调用begin()之后，调用end()之前，painter就处于active状态  

3. QPaintEngine \*QPainter::paintEngine() const
当painter处于active状态时，获取绘图引擎，否则返回0  


## 常用公共函数：获取设置信息
1. qreal QPainter::opacity() const
返回painter的透明度，默认值为1  

2. const QBrush &QPainter::background() const

3. Qt::BGMode QPainter::backgroundMode() const

3. const QBrush &QPainter::brush() const

4. QPoint QPainter::brushOrigin() const

5. const QFont &QPainter::font() const

6. QFontInfo QPainter::fontInfo() const
备注：仅当painter处于active状态时，方法有效  

7. QFontMetrics QPainter::fontMetrics() const
备注：仅当painter处于active状态时，方法有效  


## 常用公共函数：获取绘图区域
1. QRectF QPainter::boundingRect(const QRectF &rectangle, int flags, const QString &text)

2. QRect QPainter::boundingRect(const QRect &rectangle, int flags, const QString &text)

3. QRect QPainter::boundingRect(int x, int y, int w, int h, int flags, const QString &text)

4. QRectF QPainter::boundingRect(const QRectF &rectangle, const QString &text, const QTextOption &option = QTextOption())


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


## 常用公共函数：其他设置
1. void QPainter::setOpacity(qreal opacity)
设置透明度，参数范围从0.0到1.0，默认为1.0  

2. void QPainter::setFont(const QFont &font)
设置绘图的字体，这个字体对drawText()等方法生效  


--------------------------绘画不同的内容---------------------------

## 常用公共函数：画单个点(方块形状的点)
1. void QPainter::drawPoint(const QPointF &position)

2. void QPainter::drawPoint(const QPoint &position)

3. void QPainter::drawPoint(int x, int y)


## 常用公共函数：画多个点(方块形状的点)
1. void QPainter::drawPoints(const QPointF \*points, int pointCount)
```
static const QPointF points[4] = {
    QPointF(10.0, 80.0),
    QPointF(20.0, 10.0),
    QPointF(80.0, 30.0),
    QPointF(90.0, 70.0)
};
```

2. void QPainter::drawPoints(const QPolygonF &points)

3. void QPainter::drawPoints(const QPoint \*points, int pointCount)

4. void QPainter::drawPoints(const QPolygon &points)


## 常用公共函数：画单根直线
1. void QPainter::drawLine(const QLineF &line)
```
QLineF line(10.0, 80.0, 90.0, 20.0);
QPainter(this);
painter.drawLine(line);
```

2. void QPainter::drawLine(const QLine &line)

3. void QPainter::drawLine(int x1, int y1, int x2, int y2)

4. void QPainter::drawLine(const QPoint &p1, const QPoint &p2)

5. void QPainter::drawLine(const QPointF &p1, const QPointF &p2)


## 常用公共函数：画多根直线
1. void QPainter::drawLines(const QLineF \*lines, int lineCount)

2. void QPainter::drawLines(const QVector<QLineF> &lines)

3. void QPainter::drawLines(const QPointF \*pointPairs, int lineCount)

4. void QPainter::drawLines(const QVector<QPointF> &pointPairs)

5. void QPainter::drawLines(const QLine \*lines, int lineCount)

6. void QPainter::drawLines(const QVector<QLine> &lines)

7. void QPainter::drawLines(const QPoint \*pointPairs, int lineCount)

8. void QPainter::drawLines(const QVector<QPoint> &pointPairs)


## 常用公共函数：画路径(类似于曲线)
1. void QPainter::drawPath(const QPainterPath &path)


## 常用公共函数：画折线
1. void QPainter::drawPolyline(const QPointF \*points, int pointCount)
备注：与画多边形不同，最后一个点与第一个点之间不会自动连接起来  
```
static const QPointF points[3] = 
{
    QPointF(10.0, 80.0),
    QPointF(20.0, 10.0),
    QPointF(80.0, 30.0),
};

QPainter painter(this);
painter.drawPolyline(points, 3);
```

2. void QPainter::drawPolyline(const QPolygonF &points)

3. void QPainter::drawPolyline(const QPoint \*points, int pointCount)

4. void QPainter::drawPolyline(const QPolygon &points)


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


## 常用公共函数：画带有圆弧角的矩形方框
1. void QPainter::drawRoundedRect(const QRectF &rect, qreal xRadius, qreal yRadius, Qt::SizeMode mode = Qt::AbsoluteSize)

2. void QPainter::drawRoundedRect(int x, int y, int w, int h, qreal xRadius, qreal yRadius, Qt::SizeMode mode = Qt::AbsoluteSize)

3. void QPainter::drawRoundedRect(const QRect &rect, qreal xRadius, qreal yRadius, Qt::SizeMode mode = Qt::AbsoluteSize)


## 常用公共函数：画弧线(圆圈的一部分)
1. void QPainter::drawArc(const QRectF &rectangle, int startAngle, int spanAngle)
根据给定的矩形区域、起始角度、跨角来画一根弧线(圆圈的一部分)  
备注：起始角度和跨角的1代表16/1度，一个完整的圆圈是16 * 360度 = 5760  
备注：角度数值为正，代表逆时针方向；角度数值为负，代表顺时针方向  
备注：0度在3点钟方向  
```
QRectF rectangle(10.0, 20.0, 80.0, 60.0);
int startAngle = 30 * 16;
int spanAngle = 120 * 16;

QPainter painter(this);
painter.drawArc(rectangle, startAngle, spanAngle);
```

2. void QPainter::drawArc(const QRect &rectangle, int startAngle, int spanAngle)

3. void QPainter::drawArc(int x, int y, int width, int height, int startAngle, int spanAngle)


## 常用公共函数：画弦(弧线加一根直线)
1. void QPainter::drawChord(const QRectF &rectangle, int startAngle, int spanAngle)
根据给定的矩形区域、起始角度、跨角来画一个弦(弧线加一根直线)  
备注：起始角度和跨角的1代表16/1度，一个完整的圆圈是16 * 360度 = 5760  
备注：角度数值为正，代表逆时针方向；角度数值为负，代表顺时针方向  
备注：0度在3点钟方向  
```
QRectF rectangle(10.0, 20.0, 80.0, 60.0);
int startAngle = 30 * 16;
int spanAngle = 120 * 16;

QPainter painter(this);
painter.drawChord(rect, startAngle, spanAngle);
```

2. void QPainter::drawChord(int x, int y, int width, int height, int startAngle, int spanAngle)

3. void QPainter::drawChord(const QRect &rectangle, int startAngle, int spanAngle)


## 常用公共函数：画饼状图
1. void QPainter::drawPie(const QRectF &rectangle, int startAngle, int spanAngle)

2. void QPainter::drawPie(int x, int y, int width, int height, int startAngle, int spanAngle)

3. void QPainter::drawPie(const QRect &rectangle, int startAngle, int spanAngle)


## 常用公共函数：画多边形
1. void QPainter::drawConvexPolygon(const QPointF \*points, int pointCount)
pointCount参数代表多边形的顶点个数  
备注：与画折线不同，最后一个点与第一个点之间会自动连接起来  
```
static const QPointF points[4] = {
    QPointF(10.0, 80.0),
    QPointF(20.0, 10.0),
    QPointF(80.0, 30.0),
    QPointF(90.0, 70.0)
};

QPainter painter(this);
painter.drawConvexPolygon(points, 4);
```

2. void QPainter::drawConvexPolygon(const QPolygonF &polygon)

3. void QPainter::drawConvexPolygon(const QPoint \*points, int pointCount)

4. void QPainter::drawConvexPolygon(const QPolygon &polygon)


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


## 常用公共函数：画静态文本内容
1. void QPainter::drawStaticText(const QPointF &topLeftPosition, const QStaticText &staticText)

2. void QPainter::drawStaticText(const QPoint &topLeftPosition, const QStaticText &staticText)

3. void QPainter::drawStaticText(int left, int top, const QStaticText &staticText)


## 常用公共函数：画图片QImage
1. void QPainter::drawImage(const QRectF &target, const QImage &image, const QRectF &source, Qt::ImageConversionFlags flags = Qt::AutoColor)
备注：QImage的尺寸会被自动调整为target矩形的尺寸  
```
QPainter painter(ui -> label);
QImage image("D:/chart.png");
QRect rect(0, 0, ui -> label -> width(), ui -> label -> height());
painter.setRenderHint(QPainter::LosslessImageRendering);//据说可以提高图像质量
painter.drawImage(rect, image);
```

2. void QPainter::drawImage(const QRect &target, const QImage &image, const QRect &source, Qt::ImageConversionFlags flags = Qt::AutoColor)

3. void QPainter::drawImage(const QPointF &point, const QImage &image, const QRectF &source, Qt::ImageConversionFlags flags = Qt::AutoColor)

4. void QPainter::drawImage(const QPoint &point, const QImage &image, const QRect &source, Qt::ImageConversionFlags flags = Qt::AutoColor)

5. void QPainter::drawImage(const QRectF &rectangle, const QImage &image)

6. void QPainter::drawImage(const QRect &rectangle, const QImage &image)

7. void QPainter::drawImage(const QPointF &point, const QImage &image)

8. void QPainter::drawImage(const QPoint &point, const QImage &image)

9. void QPainter::drawImage(int x, int y, const QImage &image, int sx = 0, int sy = 0, int sw = -1, int sh = -1, Qt::ImageConversionFlags flags = Qt::AutoColor)


## 常用公共函数：画图片QPixmap(尺寸自动缩放)
1. void QPainter::drawPixmap(const QRectF &target, const QPixmap &pixmap, const QRectF &source)
备注：QPixmap的尺寸会被自动调整为target矩形的尺寸  

2. void QPainter::drawPixmap(const QRect &target, const QPixmap &pixmap, const QRect &source)

3. void QPainter::drawPixmap(int x, int y, int w, int h, const QPixmap &pixmap, int sx, int sy, int sw, int sh)

4. void QPainter::drawPixmap(int x, int y, const QPixmap &pixmap, int sx, int sy, int sw, int sh)

5. void QPainter::drawPixmap(const QPointF &point, const QPixmap &pixmap, const QRectF &source)

6. void QPainter::drawPixmap(const QPoint &point, const QPixmap &pixmap, const QRect &source)

7. void QPainter::drawPixmap(const QPointF &point, const QPixmap &pixmap)

8. void QPainter::drawPixmap(const QPoint &point, const QPixmap &pixmap)

9. void QPainter::drawPixmap(int x, int y, const QPixmap &pixmap)

10. void QPainter::drawPixmap(const QRect &rectangle, const QPixmap &pixmap)

11. void QPainter::drawPixmap(int x, int y, int width, int height, const QPixmap &pixmap)


## 常用公共函数：画图片QPixmap(尺寸不变)
1. void QPainter::drawTiledPixmap(const QRectF &rectangle, const QPixmap &pixmap, const QPointF &position = QPointF())
备注：QPixmap的尺寸保持不变，多出矩形方框的部分不予显示  

2. void QPainter::drawTiledPixmap(int x, int y, int width, int height, const QPixmap &pixmap, int sx = 0, int sy = 0)

3. void QPainter::drawTiledPixmap(const QRect &rectangle, const QPixmap &pixmap, const QPoint &position = QPoint())


## 常用公共函数：画图片QPicture
1. void QPainter::drawPicture(const QPointF &point, const QPicture &picture)

2. void QPainter::drawPicture(int x, int y, const QPicture &picture)

3. void QPainter::drawPicture(const QPoint &point, const QPicture &picture)


--------------------------对指定区域进行填充/擦除---------------------------

## 常用公共函数：对路径填充颜色
1. void QPainter::fillPath(const QPainterPath &path, const QBrush &brush)


## 常用公共函数：对区域填充颜色
1. void QPainter::fillRect(const QRectF &rectangle, const QBrush &brush)

2. void QPainter::fillRect(int x, int y, int width, int height, const QBrush &brush)

3. void QPainter::fillRect(const QRect &rectangle, const QBrush &brush)

4. void QPainter::fillRect(const QRectF &rectangle, const QColor &color)

5. void QPainter::fillRect(int x, int y, int width, int height, const QColor &color)

6. void QPainter::fillRect(const QRect &rectangle, const QColor &color)

7. void QPainter::fillRect(int x, int y, int width, int height, Qt::GlobalColor color)

8. void QPainter::fillRect(const QRect &rectangle, Qt::GlobalColor color)

9. void QPainter::fillRect(const QRectF &rectangle, Qt::GlobalColor color)

10. void QPainter::fillRect(int x, int y, int width, int height, Qt::BrushStyle style)

11. void QPainter::fillRect(const QRect &rectangle, Qt::BrushStyle style)

12. void QPainter::fillRect(const QRectF &rectangle, Qt::BrushStyle style)

13. void QPainter::fillRect(int x, int y, int width, int height, QGradient::Preset preset)

14. void QPainter::fillRect(const QRect &rectangle, QGradient::Preset preset)

15. void QPainter::fillRect(const QRectF &rectangle, QGradient::Preset preset)


## 常用公共函数：对区域进行擦除
1. void QPainter::eraseRect(const QRectF &rectangle)
相当于把指定区域设置为背景颜色  
```
fillRect(rectangle, background());
```

2. void QPainter::eraseRect(int x, int y, int width, int height)

3. void QPainter::eraseRect(const QRect &rectangle)
