# QXlsx

## 基本功能
QXlsx是一个强大的开源表格库，可以生成excel表格文件(文件格式为.xlsx)
QXlsx还可以读取或者编辑已有的表格文件中的数据
文件中可以插入图表(直方图、曲线、折线图、饼状图)，也可以插入图片
QXlsx的核心类是Document


## 特点
QXlsx库可以不依赖于Microsoft Excel，也不用调用windows的COM组件
QXlsx库可以应用在任何Qt5支持的平台上


## 官方文档
> http://qtxlsx.debao.me/


## 源代码下载地址
> https://github.com/dbzhang800/QtXlsxWriter


---------------QXlsx使用方式一：调用动态库---------------

生成动态链接库，将动态库放到Qt下，调库使用
备注：编译时需要工具Perl


---------------QXlsx使用方式二：调用源码---------------

1. 从github上下载QXlsx，解压解压QtXlsxWriter-master.zip
2. 将QtXlsxWriter-master\src目录中的xlsx文件夹拷贝到自己的Qt项目中
3. 在自己Qt项目的.pro文件中添加
```
include(xlsx/qtxlsx.pri)
```
4. 在自己的Qt项目代码中添加
```
#include "xlsxdocument.h"
using namespace QXlsx;
```
--------------------------------------

## 命名空间QXlsx中的类
```
CAbstractSheetPrivate
CXlsxSeries
CXlsxAxis
CChartPrivate
CChartsheetPrivate
CXlsxColor
CContentTypes
CDocPropsApp
CDocPropsCore
CDocumentPrivate
CDrawing
CXlsxMarker
CDrawingAnchor
CDrawingAbsoluteAnchor
CDrawingOneCellAnchor
CDrawingTwoCellAnchor
CFormatPrivate
CMediaFile
CNumFormatParser
CXlsxRelationship
CRelationships
CXlsxSharedStringInfo
CSharedStrings
CSimpleOOXmlFile
CXlsxFormatNumberData
CStyles
CTheme
CXlsxDefineNameData
CWorkbookPrivate
CXlsxHyperlinkData
CXlsxSheetFormatProps
CXlsxRowInfo
CXlsxColumnInfo
CWorksheetPrivate
CZipReader
CZipWriter
```