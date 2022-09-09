# Document

## 基本功能
Document是QXlsx中的核心类，提供用来处理xlsx文件内容的API
```
#include "xlsxdocument.h"
using namespace QXlsx;
```


## 注意事项
1. 表格中横向为A、B、C、D...，表格中纵向为1、2、3、4...

2. 行号和列号都是从1开始，不是从0开始


## 关于设置单元格格式的说明
实际测试发现，不管是按行还是按列设置格式，都会设置全部行或者全部列，没办法设置部分区域  
例如，想对单元格中目标区域"A1:F12"中每个单元格加上黑框  
使用setColumnFormat()函数会把第1列到第6列全部单元格加上黑框  
使用setRowFormat()函数会把第1行到第12行全部单元格加上黑框  
```
Format format;
format.setBorderStyle(Format::BorderMedium);
xlsx.setColumnFormat("A1:F12", format);
```
目前想到的办法是使用write()函数，在写的时候可以顺便设置该单元格的格式  
对于空白的单元格可以写入一个空字符串，以后想要继续设置该单元格的格式也不会影响  
```
Format format;
format.setBorderStyle(Format::BorderMedium);
for(int column = 1; column < 7; column++)
{
    for(int row = 1; row < 13; row++)
    {
        xlsx.write(row, column, QString(), format);
    }
}
```
备注：对于合并后的单元格如A1:A3，也要每个单元格A1、A2、A3都进行格式设置，没有办法直接设置整个合并单元格  


## 关于插入图片的问题
1. 图片显示的位置问题
QXlsx这个库的代码写的并不完善，插入的图片默认显示在单元格的左上角，可能会遮挡单元格的边框线  
insertImage()函数中并没有提供设置图片位置偏移的接口  
在QXlsx的源码中找到Worksheet::insertImage()函数，将下面代码进行修改：  
```
anchor->from = XlsxMarker(row, column, 0, 0);
```
后两个参数其实就是偏移量rowoff和coloff，只是代码中默认给写为了0  
可以对源码进行简单修改，也可以修改insertImage函数接口  
```
anchor->from = XlsxMarker(row, column, 5*9525, 5*9525);
```
详细参考：  
> https://blog.csdn.net/qq_27681837/article/details/50408260
2. 在不同电脑上excel中图片显示比例的问题
发现在不同的电脑上，表格中插入的图片大小不一致  
例如：在一台电脑上图片和表格大小相同，但换到另一台电脑上后，图片超出了表格的范围  
这个并不是图片本身的大小发生了变化，而是每行表格的高度变化了  
详见：关于电脑屏幕dpi的说明.md  


## 构造函数
1. Document (QObject \*parent=0)

2. Document (const QString &xlsxName, QObject \*parent=0)

3. Document (QIODevice \*device, QObject \*parent=0)


## 文件保存
1. bool save () const
用默认的文件名'Book1.xlsx'来保存

2. bool saveAs (const QString &xlsXname) const
设置自定义的文件名，要加上文件格式后缀
```
xlsx.saveAs("myexcel.xlsx");
```
也可以用来设置文件的保存路径
```
xlsx.saveAs("D:/myexcel.xlsx");
```

3. bool saveAs (QIODevice \*device) const


## 表格中写入数据
1. bool write (const CellReference &cell, const QVariant &value, const Format &format=Format())
```
xlsx.write("A1", "Hello Qt!");
xlsx.write("A2", 12345);
xlsx.write("A3", "A3");
xlsx.write("A4", true);
xlsx.write("A5", "http://qt-project.org");
xlsx.write("A6", QDate(2013, 12, 27));
xlsx.write("A7", QTime(6, 30));
xlsx.write("B1", "this is B1");
```
如果需要写入的字符串实现换行，需要在字符串指定位置加入'\n'，并设置format.setTextWarp(true)  

2. bool write (int row, int col, const QVariant &value, const Format &format=Format())
```
xlsx.write(1, 3, "C1");
xlsx.write(2, 3, "C2");
```


## 向表格中插入图片
1. bool insertImage(int row, int col, const QImage &image)
注意：实际插入的位置是指定单元格的右下角  
如果想插入左上角第一个单元格，插入位置要设置成(0, 0)  
```
QImage image1;
image1.load("D:/123.jpg");
xlsx.insertImage(3, 3, image1);
```


## 向表格中插入图表Chart
1. Chart \*insertChart(int row, int col, const QSize &size);
注意：这里的Chart对象不是函数参数，而是函数的返回值  
注意：实际插入的位置是指定单元格的右下角  
备注：插入图表也存在图表显示在单元格左上方的问题，解决办法和插入图片一样  


## 从表格中读出数据
1. QVariant read (const CellReference &cell) const

2. QVariant read (int row, int col) const


## 合并/拆分单元格
1. bool mergeCells (const CellRange &range, const Format &format=Format())
```
xlsx.mergeCells("A1:C3");
xlsx.mergeCells("A1:C1");
xlsx.mergeCells("A1:A3");
```

2. bool unmergeCells (const CellRange &range)
```
xlsx.unmergeCells("A1:A3");
```


## 设置单元格宽高
1. bool setColumnWidth (const CellRange &range, double width)
设置若干列的列宽  
```
xlsx.setColumnWidth("B1:F1", 30);
```

2. bool setColumnWidth (int column, double width)
设置某一列的列宽  
```
xlsx.setColumnWidth(4, 30);
```

3. bool setColumnWidth (int colFirst, int colLast, double width)
设置若干列的列宽  
```
xlsx.setColumnWidth(4, 10, 30);
```

4. bool setRowHeight (int row, double height)
设置某一行的高度  
```
xlsx.setRowHeight(2, 50);
```

5. bool setRowHeight (int rowFirst, int rowLast, double height)
设置若干行的高度  
```
xlsx.setRowHeight(2, 5, 50);
```


## 设置单元格格式
bool setColumnFormat (const CellRange &range, const Format &format)

bool setColumnFormat (int column, const Format &format)

bool setColumnFormat (int colFirst, int colLast, const Format &format)

bool setColumnHidden (const CellRange &range, bool hidden)

bool setColumnHidden (int column, bool hidden)

bool setColumnHidden (int colFirst, int colLast, bool hidden)

bool setRowFormat (int row, const Format &format)

bool setRowFormat (int rowFirst, int rowLast, const Format &format)

bool setRowHidden (int row, bool hidden)

bool setRowHidden (int rowFirst, int rowLast, bool hidden)


## 读取单元格格式
double columnWidth (int column)

Format columnFormat (int column)

bool isColumnHidden (int column)

double rowHeight (int row)

Format rowFormat (int row)

bool isRowHidden (int row)


## 在表格中创建新的工作表Sheet
备注：QXlsx创建的表格中默认只有一张工作表  
1. QStringList sheetNames() const;
获取当前所有的工作表  

2. bool addSheet(const QString &name = QString(), AbstractSheet::SheetType type = AbstractSheet::ST_WorkSheet);
添加一个新的工作表  
备注：当前工作表会自动切换为新插入的工作表  
```
xlsx.addSheet("mysheet");
```

3. bool insertSheet(int index, const QString &name = QString(), AbstractSheet::SheetType type = AbstractSheet::ST_WorkSheet);
在指定位置插入一个新的工作表  

4. bool selectSheet(const QString &name);
设置当前工作表  
```
xlsx.selectSheet("Sheet1");
```

5. bool renameSheet(const QString &oldName, const QString &newName);
重命名工作表  

6. bool copySheet(const QString &srcName, const QString &distName = QString());
复制工作表  

7. bool moveSheet(const QString &srcName, int distIndex);
移动工作表  

8. bool deleteSheet(const QString &name);
删除工作表  

9. AbstractSheet \*sheet(const QString &sheetName) const;
获取指定工作表对象  
```
xlsx.addSheet("sheet_data");
AbstractSheet *sheet_data;
sheet_data = xlsx.sheet("sheet_data");
```

10. AbstractSheet \*currentSheet() const;
获取当前工作表对象  
```
AbstractSheet *sheet_data;
sheet_data = xlsx.currentSheet();
```