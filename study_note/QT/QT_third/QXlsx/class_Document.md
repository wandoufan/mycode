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

2. bool write (int row, int col, const QVariant &value, const Format &format=Format())
```
xlsx.write(1, 3, "C1");
xlsx.write(2, 3, "C2");
```


## 向表格中插入图片
1. bool insertImage (int row, int col, const QImage &image)
注意：实际插入的位置是指定单元格的右下角  
```
QImage image1;
image1.load("D:/123.jpg");
xlsx.insertImage(3, 3, image1);
```


## 向表格中插入图表Chart
1. Chart \*insertChart(int row, int col, const QSize &size);
注意：这里的Chart对象不是函数参数，而是函数的返回值  
注意：实际插入的位置是指定单元格的右下角  


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

bool setColumnHidden (const CellRange &range, bool hidden)

bool setColumnFormat (int column, const Format &format)

bool setColumnHidden (int column, bool hidden)

bool setColumnFormat (int colFirst, int colLast, const Format &format)

bool setColumnHidden (int colFirst, int colLast, bool hidden)

bool setRowFormat (int row, const Format &format)

bool setRowHidden (int row, bool hidden)

bool setRowFormat (int rowFirst, int rowLast, const Format &format)

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