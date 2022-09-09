# Qt程序中处理Pdf文件

## 参考资料
> https://wiki.qt.io/Handling_PDF


## Qt官方提供的pdf相关的库
目前主要是关于生成pdf相关的库，在打开、预览、解析pdf等方面还有欠缺  
```
QPdfDestination
QPdfDocument
QPdfDocumentRenderOptions
QPdfPageNavigation
QPdfPageRenderer
QPdfSelection
QPdfWriter
```


## 目前项目中实际用到的pdf相关功能
生成pdf、打印之前预览pdf
其他的解析pdf等复杂功能目前暂时没有用到


----------------读写pdf-------------------
## 使用QPrinter
1. manual QPainter painting
把QPrinter对象作为参数传递给QPainter的构造函数  
使用QPainter是创建pdf文档最基本的方法(但不是最简单的方法)  
需要手动的把pdf中的所有图形、文字、表格等都一点一点画出来  
这种方法适合从头开始创建一个pdf，不适合把已有的文件转换为pdf  
2. Scribe抄写
Qt Scribe框架是用来创建结构化富文本文档的更高级别的API  
Scribe框架可以读取和操作富文本文档，然后通过QTextDocument::print()把内容传递给QPrinterQPrinter  
支持的文档格式详见：https://wiki.qt.io/Handling_Document_Formats  
3. Graphics View
Qt Graphics View框架更适合用来针对2D图形画面来创建pdf文档  


## 使用第三方库
1. poppler-qt4
> https://freedesktop.org/wiki/Software/poppler/
2. Hummus
> https://pdfhummus.com/
3. PoDoFo
> http://podofo.sourceforge.net/


## 使用分批转换工具
1. poppler-utils
> https://freedesktop.org/wiki/Software/poppler/
2. Inkscape
> https://inkscape.org/


----------------显示pdf(pdf阅读器)-------------------
## 使用QtPDF


## 使用第三方的库/工具
1. poppler-qt4
> https://freedesktop.org/wiki/Software/poppler/
2. poppler-qt5
> https://freedesktop.org/wiki/Software/poppler/
3. mupdf
https://mupdf.com/
目前项目代码中实际使用的应该是mupdf  


----------------交互式的查看pdf-------------------
## 使用QtPDF
QtPDF模块包含了PDF viewer，可以添加到Qt Quick程序或基于widget的程序中  


## 调用外部的pdf viewer工具


## 使用第三方的Qt widget
1. XpdfWidget/Qt
> http://www.glyphandcog.com/XpdfWidgetQt.html
类名：XpdfWidget


## 嵌入一个第三方的ActiveX
1. Adobe Reader
> http://get.adobe.com/reader/
dll文件：Acropdf.dll


## 嵌入一个第三方的浏览器控件
1. Adobe Reader
> http://get.adobe.com/reader/
控件：nppdf


----------------其他-------------------
## excel转pdf
上面的那么多方法都大概了解了一下，不管是Qt自带的还是第三方的感觉都不太合适  
Qt的Scribe框架侧重于对文本内容进行处理  
Qt的Graphics View框架能获取到画面内容，但不能针对excel文件进行特别处理  
poppler等第三方库都侧重于对pdf进行创建、解析、显示  
上述这些方法都不是专门用来实现excel转pdf的功能  
这些方法有可能能够实现需求，但学习成本太高，暂时没时间细看了  


## 调用OfficeExcel的组件实现文件转换成pdf
调用微软的接口：Workbook.ExportAsFixedFormat方法
代码示例详见QT_ActiveQt.md
备注：这个方法需要依赖OfficeExcel的组件
> https://docs.microsoft.com/zh-cn/office/vba/api/excel.workbook.exportasfixedformat


