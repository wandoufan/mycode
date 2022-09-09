# QPdfWriter

## 基本功能
QPdfWriter可以通过绘图设备来生成pdf文件，基于QPainter实现  
父类：QObject and QPagedPaintDevice  
子类：无  


## QPdfWriter与QPrinter的对比
二者都是QPagedPaintDevice的子类，都可以用来生成pdf文件，区别在于：  
1. QPrinter是Qt4中的，QPdfWriter是Qt5中的，QPdfWriter使用更简单
2. QPdfWriter专门用来生成pdf文件，而QPrinter的功能更加强大，还可以操作打印机等


## 代码示例
1. 将图片转换为pdf文件
注意：图片放入pdf之后，尺寸会自动变小，原因未知，需要用scale()方法进行放大
```
QString file_path = "D:/image.pdf";
QFile pdf_file(file_path);
if(pdf_file.open(QIODevice::WriteOnly))
{
    QPdfWriter *pdf_writer = new QPdfWriter(&pdf_file);
    pdf_writer -> setPageMargins(QMarginsF(10, 10, 10, 10));
    QPainter *painter = new QPainter(pdf_writer);
    QImage image("D:/chart.png");
    //图片写入Pdf之后默认会被缩小，需要进行放大
    QRect rect = painter -> viewport();
    int multiple = rect.width() / image.width();//放大倍数
    painter -> scale(multiple, multiple);
    painter -> setRenderHint(QPainter::LosslessImageRendering);//据说可以提高图像质量
    painter -> drawImage(50, 50, image);
    //注意：最后一定要有清理内存的处理，否则生成的pdf文件打开报错
    delete painter;
    delete pdf_writer;
    pdf_file.close();
}
```

2. 从头开始生成一个pdf文件
文件中所有的内容(图形、文字、表格)都需要自己一点一点画出来  
另外，还需要调整坐标系等等一系列设置，如果文件内容比较多，用起来就会很麻烦  
```
QString file_path = "D:/test.pdf";
QFile pdf_file(file_path);
if(pdf_file.open(QIODevice::WriteOnly))
{
    QPdfWriter *pdf_writer = new QPdfWriter(&pdf_file);
    pdf_writer -> setResolution(300);
    pdf_writer -> setPageMargins(QMarginsF(10, 10, 10, 10));
    pdf_writer -> setTitle("this is a title");
    QPainter *painter = new QPainter(pdf_writer);
    painter -> setFont(QFont("Calibri", 10, 50));
    painter -> setPen(QPen(Qt::red, 3));
    painter -> drawText(100, 100, "this is pdf test page1");
    painter -> drawRect(300, 300, 400, 300);
    pdf_writer -> newPage();
    painter -> drawText(100, 100, "this is pdf test page2");
    //注意：最后一定要有清理内存的处理，否则生成的pdf文件打开报错
    delete painter;
    delete pdf_writer;
    pdf_file.close();
}
```


3. 将一个已有的文件转换为pdf文件
目前没有发现QPdfWriter能够实现这个功能  


-------------------------------------

## 构造函数
1. QPdfWriter::QPdfWriter(QIODevice \*device)

2. QPdfWriter::QPdfWriter(const QString &filename)


## 常用公共函数：