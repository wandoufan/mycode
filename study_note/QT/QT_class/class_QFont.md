# QFont

## 基本功能
QFont用来定义文本的字体属性，包括：字体、大小、粗细、斜体、下划线等等  
备注：不包括设置文本颜色  
父类：无  
子类：无  


## 关于设置字体大小的说明
在不同的显示设备上，dpi(屏幕分辨率)的值可能不同  
如果想要在不同的dpi下显示同样的实际大小，则使用setPointSize()/setPointSizeF()方法  
如果想要字体显示大小随dpi的值而变化，则使用setPixelSize()方法  
另外，在qss语句中，也区分设置字体大小的方式  
```
font-size:16pt;//相当于setPointSize()/setPointSizeF()方法
font-size:16px;//相当于setPixelSize()方法
```


## 代码示例
1. 构造一个常用字体
```
QFont font = QFont("Calibri", 10, 50);
```


## 构造函数
1. QFont::QFont(const QFont &font)

2. QFont::QFont(const QFont &font, const QPaintDevice \*pd)

3. QFont::QFont(const QString &family, int pointSize = -1, int weight = -1, bool italic = false)

4. QFont::QFont()


## 常用公共函数：设置/读取文本各种属性
1. void QFont::setFamily(const QString &family)
设置字体的名字，字体名字不区分大小写  
最常用的字体是"Calibri"，UI界面中按钮使用的默认字体是'SimSun'  
Qt支持的所有字体在帮助手册中没有看到，但可以通过如下方法进行查询  
```
QFontDatabase fd;
QList<QString> family_list = fd.families();
for(int i = 0; i < family_list.size(); i++)
{
    qDebug() << i << ":" << family_list[i];
}
```

2. QString QFont::family() const

3. void QFont::setPixelSize(int pixelSize)
设置字体像素单位的大小  
使用这个函数设置的字体大小会和实际的显示设备有关  

4. int QFont::pixelSize() const
返回字体的像素单位的大小  
如果字体大小是由setPointSize()/setPointSizeF()方法设置的，则返回-1  

5. void QFont::setPointSize(int pointSize)
设置字体肉眼看到的实际大小，pointSize参数必须大于0  
使用这个函数设置的字体大小和显示设备无关  

6. int QFont::pointSize() const
返回字体的实际大小  
如果字体大小是由setPixelSize()方法设置的，则返回-1  

7. void QFont::setPointSizeF(qreal pointSize)
设置字体肉眼看到的实际大小，pointSize参数必须大于0  
使用这个函数设置的字体大小和显示设备无关  
setPointSizeF()设置比setPointSize()更精准，但有的平台可能无法支持这个精度  

8. qreal QFont::pointSizeF() const
返回字体的实际大小  
如果字体大小是由setPixelSize()方法设置的，则返回-1  

9. void QFont::setBold(bool enable)
设置文字为粗体  
true的效果等于setWeight(QFont::Bold)，false的效果等于setWeight(QFont::Normal)  
备注：如果设置了styleName()，这里的设置可能会无效  

10. bool QFont::bold() const

11. void QFont::setWeight(int weight)
设置文字的粗细，weight范围为0-99，取值详见enum QFont::Weight  
备注：如果设置了styleName()，这里的设置可能会无效  

12. int QFont::weight() const

13. void QFont::setItalic(bool enable)
设置文字为斜体  
备注：如果设置了styleName()，这里的设置可能会无效  

14. bool QFont::italic() const

15. void QFont::setOverline(bool enable)
设置上划线  

16. bool QFont::overline() const

17. void QFont::setUnderline(bool enable)
设置下划线  

18. bool QFont::underline() const

19. void QFont::setStrikeOut(bool enable)
设置删除线  

20. bool QFont::strikeOut() const

21. void QFont::setStyleName(const QString &styleName)
设置文本风格  

22. QString QFont::styleName() const


## enum QFont::Weight
```
Constant 			Value 		Description
QFont::Thin			0			0
QFont::ExtraLight	12			12
QFont::SemiLight 	25			25
QFont::Normal 		50			50
QFont::Medium 		57			57
QFont::DemiBold 	63			63
QFont::Bold 		75			75
QFont::ExtraBold 	81			81
QFont::Black		87			87
```

## QFontDatabase中包含的所有的字体
```
0 : "Arial"
1 : "Arial Black"
2 : "Arial Narrow"
3 : "Bahnschrift"
4 : "Bahnschrift Condensed"
5 : "Bahnschrift Light"
6 : "Bahnschrift Light Condensed"
7 : "Bahnschrift Light SemiCondensed"
8 : "Bahnschrift SemiBold"
9 : "Bahnschrift SemiBold Condensed"
10 : "Bahnschrift SemiBold SemiConden"
11 : "Bahnschrift SemiCondensed"
12 : "Bahnschrift SemiLight"
13 : "Bahnschrift SemiLight Condensed"
14 : "Bahnschrift SemiLight SemiConde"
15 : "Book Antiqua"
16 : "Bookman Old Style"
17 : "Bookshelf Symbol 7"
18 : "Calibri"
19 : "Calibri Light"
20 : "Cambria"
21 : "Cambria Math"
22 : "Candara"
23 : "Candara Light"
24 : "Century"
25 : "Century Gothic"
26 : "Comic Sans MS"
27 : "Consolas"
28 : "Constantia"
29 : "Corbel"
30 : "Corbel Light"
31 : "Courier"
32 : "Courier New"
33 : "DejaVu Sans Mono"
34 : "DengXian"
35 : "Dubai"
36 : "Dubai Light"
37 : "Dubai Medium"
38 : "Ebrima"
39 : "Fixedsys"
40 : "Franklin Gothic Medium"
41 : "Gabriola"
42 : "Gadugi"
43 : "Garamond"
44 : "Georgia"
45 : "HoloLens MDL2 Assets"
46 : "Impact"
47 : "Ink Free"
48 : "Javanese Text"
49 : "Leelawadee"
50 : "Leelawadee UI"
51 : "Leelawadee UI Semilight"
52 : "Lucida Console"
53 : "Lucida Sans Unicode"
54 : "Malgun Gothic"
55 : "Malgun Gothic Semilight"
56 : "Marlett"
57 : "Microsoft Himalaya"
58 : "Microsoft JhengHei"
59 : "Microsoft JhengHei Light"
60 : "Microsoft JhengHei UI"
61 : "Microsoft JhengHei UI Light"
62 : "Microsoft New Tai Lue"
63 : "Microsoft PhagsPa"
64 : "Microsoft Sans Serif"
65 : "Microsoft Tai Le"
66 : "Microsoft Uighur"
67 : "Microsoft YaHei"
68 : "Microsoft YaHei UI"
69 : "Microsoft YaHei UI Light"
70 : "Microsoft Yi Baiti"
71 : "MingLiU-ExtB"
72 : "MingLiU_HKSCS-ExtB"
73 : "Modern"
74 : "Mongolian Baiti"
75 : "Monotype Corsiva"
76 : "MS Gothic"
77 : "MS PGothic"
78 : "MS Reference Sans Serif"
79 : "MS Reference Specialty"
80 : "MS Sans Serif"
81 : "MS Serif"
82 : "MS UI Gothic"
83 : "MT Extra"
84 : "MV Boli"
85 : "Myanmar Text"
86 : "Nirmala UI"
87 : "Nirmala UI Semilight"
88 : "Palatino Linotype"
89 : "PMingLiU-ExtB"
90 : "Roman"
91 : "Script"
92 : "Segoe MDL2 Assets"
93 : "Segoe Print"
94 : "Segoe Script"
95 : "Segoe UI"
96 : "Segoe UI Black"
97 : "Segoe UI Emoji"
98 : "Segoe UI Historic"
99 : "Segoe UI Light"
100 : "Segoe UI Semibold"
101 : "Segoe UI Semilight"
102 : "Segoe UI Symbol"
103 : "SimSun-ExtB"
104 : "Sitka"
105 : "Sitka Banner"
106 : "Sitka Display"
107 : "Sitka Heading"
108 : "Sitka Small"
109 : "Sitka Subheading"
110 : "Sitka Text"
111 : "Small Fonts"
112 : "Sylfaen"
113 : "Symbol"
114 : "System"
115 : "Tahoma"
116 : "TeamViewer15"
117 : "Terminal"
118 : "Times New Roman"
119 : "Trebuchet MS"
120 : "Verdana"
121 : "Webdings"
122 : "Wingdings"
123 : "Wingdings 2"
124 : "Wingdings 3"
125 : "Yu Gothic"
126 : "Yu Gothic Light"
127 : "Yu Gothic Medium"
128 : "Yu Gothic UI"
129 : "Yu Gothic UI Light"
130 : "Yu Gothic UI Semibold"
131 : "Yu Gothic UI Semilight"
132 : "仿宋"
133 : "华文中宋"
134 : "华文仿宋"
135 : "华文宋体"
136 : "华文彩云"
137 : "华文新魏"
138 : "华文楷体"
139 : "华文琥珀"
140 : "华文细黑"
141 : "华文行楷"
142 : "华文隶书"
143 : "宋体"
144 : "小米兰亭"
145 : "幼圆"
146 : "微软雅黑"
147 : "微软雅黑 Light"
148 : "新宋体"
149 : "方正姚体"
150 : "方正舒体"
151 : "楷体"
152 : "等线"
153 : "等线 Light"
154 : "隶书"
155 : "黑体"
```