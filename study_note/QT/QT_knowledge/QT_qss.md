# Qt中的qss语句

## 基本功能
qss语法可以用来设置UI控件的颜色、字体、边框等各种属性  
备注：控件本身的长宽参数无法通过qss语句来设置  
备注：详见Qt帮助手册中的'The Style Sheet Syntax'  


## 用法示例
1. qss语句可以直接写在代码中，作为setStyleSheet函数的参数
```
label1 -> setStyleSheet("background-color:blue;");
```
2. 在UI设计时，可以直接点击StyleSheet属性，在弹窗中写入qss语句  
```
background-color:blue;
```


## 注意事项
1. 全局属性设置和控件的局部属性设置要注意先后顺序
错误示例：全局属性设置写在前面，导致后面控件的局部属性设置无效
```
//全局属性设置
font-family: "New Century Schoolbook";
font-size: 20px;
//控件的局部属性设置
QGroupBox
{ 
border: 2px solid #333333; 
margin-top: 2ex; 
}
QPushButton
{
color: blue;
}
```
正确示例：控件的局部属性设置必须都写在全局属性设置的前面
```
//控件的局部属性设置
QGroupBox
{ 
border: 2px solid #333333; 
margin-top: 2ex; 
}
QPushButton
{
color: blue;
}
//全局属性设置
font-family: "New Century Schoolbook";
font-size: 20px;
```


## 1. 基本语法
1. 语句中的属性大小写是不敏感的，例如color, Color, COLOR指的是同一个属性
而类名、对象名、Qt的属性名是大小写敏感的  
2. 语句一般由选择器(QPushButton)和属性规则{color: red}组成
```
QPushButton { color: red }
```
3. 多个选择器可以使用同一套属性规则，多个选择器之间用逗号隔开
```
QPushButton, QLineEdit, QComboBox { color: red }
```
4. 属性规则由多组property: value组成，每组规则之间用分号隔开
```
QPushButton { color: red; background-color: white }
```
5. 注意：对于widget、groupbox等包含了子控件的控件，要写明选择器
对于label等单个控件，不要写选择器，只写规则，否则不会生效  


## 2. 选择器
1. 全局选择器
匹配所有的控件  
```
*
```
2. 类型选择器
匹配所有的QPushButton以及其子类的控件  
```
QPushButton
```
3. 属性选择器
匹配符合指定属性的QPushButton控件  
```
QPushButton[flat="false"]
```
4. 类选择器
匹配所有的QPushButton控件，但是不包括其子类控件  
```
.QPushButton
```
以上等价于  
```
*[class~="QPushButton"]
```
5. ID选择器
匹配符合指定对象名的QPushButton控件  
```
QPushButton#okButton
```
6. 子孙选择器
匹配所有QDialog中的QPushButton，包含直接子类和孙类  
```
QDialog QPushButton
```
7. 子类选择器
匹配所有QDialog中的QPushButton，只选择直接子类  
```
QDialog > QPushButton
```


## 3. 子控制
对于一些如QComboBox、QSpinBox等特殊的控件，可以根据其下拉等不同状态进行详细控制  
备注：所有的特殊控件及其对应状态，详见Qt帮助手册中的'Qt Style Sheets Reference'-'List of Sub-Controls'  
```
QComboBox::down-arrow {
image: url(down_arrow.png);
}
QComboBox::down-arrow:pressed {
position: relative;
top: 1px; 
left: 1px;
}
```


## 4. 伪状态
备注：所有的伪状态，详见Qt帮助手册中的'Qt Style Sheets Reference'-'List of Pseudo-States'  
1. 当鼠标在控件上进行盘旋时
```
QPushButton:hover { color: white }
```
2. 当鼠标不在控件上进行盘旋时
```
QRadioButton:!hover { color: red }
```
3. 一个控件可以存在多个状态，状态之间为逻辑与关系
```
QCheckBox:hover:checked { color: white }
QPushButton:hover:!pressed { color: blue; }
```
4. 一个控件可以存在多个状态，状态之间为逻辑或关系
```
QCheckBox:hover, QCheckBox:checked { color: white }
```
5. 伪状态可以和子类结合出现
```
 QComboBox::drop-down:hover { image: url(dropdown_bright.png) }
```


## 5. 冲突解决
当同一个控件匹配到多个属性规则，且规则之间相互冲突，则遵循如下解决方案：  
1. 当有多个规则时，优先匹配更特殊的规则
```
QPushButton#okButton { color: gray }//匹配
QPushButton { color: red }
```
2. 当有伪状态时，优先匹配伪状态
```
//当鼠标在控件上进行盘旋时，文本为白色，否则文本为红
QPushButton:hover { color: white }
QPushButton { color: red }
```
3. 对于类型选择器，按照先后顺序匹配，即优先匹配最后一条规则
注意：所有控件类型的特殊性是相同的  
例如，虽然QPushButton是QAbstractButton的子类，但QPushButton并不比QAbstractButton更特殊  
```
QPushButton { color: red }
QAbstractButton { color: gray }//匹配
```
4. 对于更复杂的规则冲突，详见文档中的规则特殊性计算公式'a-b-c'


## 6. 常用属性规则
备注：所有的属性规则，详见Qt帮助手册中的'Qt Style Sheets Reference'-'List of Properties'  
1. background-color
设置控件的背景颜色  
```
QLabel { background-color: yellow }
QLineEdit { background-color: rgb(255, 0, 0) }
```
2. color
```
QPushButton { color: red }
```
3. border
设置边界的宽度、风格、颜色  
```
QLineEdit { border: 1px solid white }
```
边界还可以细分为上下左右  
```
border-top
border-right
border-bottom
border-left
```
单独设置边界的颜色，同样可以细分为上下左右  
```
border-color: white;
border-top-color
...
```
单独设置边界的风格，同样可以细分为上下左右  
```
border-style: solid;
border-top-style
...
//常用的边界风格包括：
dashed 短线虚线
dot-dash 短线+断点虚线
dot-dot-dash 短线+断点虚线
dotted 断点虚线
double 双层线
solid 实线
none 没有边界线
```
单独设置边界的宽度，同样可以细分为上下左右  
```
border-width: 5px;
border-top-width
...
```
单独设置边界的曲率半径，可以细分为四个边角  
备注：如果不进行设置，控件一般都是矩形，设置后可以有圆滑的边角  
```
border-radius: 10px;
border-top-left-radius
border-top-right-radius
border-bottom-right-radius
border-bottom-left-radius
```
4. font
设置文本的大小、字体等属性  
```
QCheckBox { font: bold italic large "Times New Roman" }
```
单独设置文本的字体  
备注：Qt手册中并没有列出支持的字体，以下供参考
```
font-family: "New Century Schoolbook";(推荐)
font-family: "Microsoft YaHei";
font-family: "Segoe UI"; 
font-family: "FangSong";(字体亮度不够，看不清)
```
单独设置文本的字体大小  
```
font-size: 12px;
```
单独设置文本的字体风格  
```
font-style: italic;
```
单独设置文本的笔画粗细  
```
font-weight: 300;
//参数取值包括：
normal
bold(加粗)
100
200
...
900
```
5. text-align
设置文本在控件中的位置  
备注：实测这条规则对于QLabel、QTextBrowser控件无效  
```
QPushButton { text-align: left; }
//参数取值包括：
top
bottom
left
right
center
```


## StyleSheet属性设置参考示例
```
QPushButton {
    font-family: "Microsoft YaHei";
    font-size: 16px;
    color: #BDC8E2;
    font-style: italic;
    font-weight: bold;

    text-align: center;
    padding-left: 10px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: aqua;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
}
QPushButton:hover{
	color: red;
	border-color: green;
    background-color: aqua;
}
QPushButton:pressed{
	color: green;
	border-color: blueviolet;
    background-color: black;
}

QLabel{
    font-family: "FangSong";
    font-size: 15px;
    color: #BDC8E2;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #808080;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}

QLineEdit, QFrame { 
border-width: 1px; 
padding: 1px; 
border-style: solid; 
border-color: darkkhaki; 
border-radius: 5px; 
}

Numeric {
    font-family: "FangSong";
    font-size: 28px;
    color: green;

    font-weight: bold;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #696969;
    border-radius: 20px;

    background-color: black;
    background-repeat: no-repeat;
    background-position: left center;
}
```


```

https://blog.csdn.net/u010525694/article/details/78452786

/* === Shared === */

QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, 
QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog { 
background-color: #222222; 
color: #BBBBBB; 
font-family: “Segoe UI”; 
}

/* === QWidget === */

QWidget:window { 
background: #222222; 
color: #BBBBBB; 
font-family: “Segoe UI”; 
}

/* === QToolTip === */

QToolTip { 
background-color: #000000; 
border: 2px solid #333333; 
color: yellow; 
}

/* === QPushButton === */

QPushButton { 
border: 1px solid #333333; 
padding: 4px; 
min-width: 65px; 
min-height: 12px; 
}

QPushButton:hover { 
background-color: #333333; 
border-color: #444444; 
}

QPushButton:pressed { 
background-color: #111111; 
border-color: #333333; 
color: yellow; 
}

QPushButton:disabled { 
color: #333333; 
}

/* === Checkable items === */

QCheckBox::indicator, QRadioButton::indicator, QTreeView::indicator { 
width: 16px; 
height: 16px; 
background-color: #111111; 
border: 1px solid #333333; 
}

QRadioButton::indicator { 
border-radius: 8px; 
}

QCheckBox::indicator::checked, QRadioButton::indicator::checked, QTreeView::indicator::checked { 
background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #BBBBBB, stop:1 #111111); 
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled, QTreeView::indicator:disabled { 
background-color: #444444; 
}

QCheckBox::indicator::checked:disabled, QRadioButton::indicator::checked:disabled, QTreeView::indicator::checked:disabled { 
background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #BBBBBB, stop:1 #444444); 
}

/* === QComboBox === */

QComboBox { 
background-color: black; 
border: 1px solid #333333; 
color: white; 
padding:1px 2em 1px 3px; 
}

QComboBox::drop-down { 
subcontrol-origin: padding; 
subcontrol-position: top right; 
border-left: 1px solid #333333; 
}

QComboBox::down-arrow { 
border: 2px solid #333333; 
width: 6px; 
height: 6px; 
background: #5f5f5f; 
}

/* === QGroupBox === */

QGroupBox { 
border: 2px solid #333333; 
margin-top: 2ex; 
}

QGroupBox::title { 
color: yellow; 
subcontrol-origin: margin; 
subcontrol-position: top left; 
margin-left: 5px; 
}

/* === QTabWidget === */

QTabWidget::pane { 
background: #222222; 
border: 2px solid #333333; 
}

/* === QTabBar === */

QTabBar::tab { 
background: transparent; 
border: 1px solid #333333; 
border-bottom: none; 
color: #BBBBBB; 
padding-left: 5px; 
padding-right: 10px; 
padding-top: 3px; 
padding-bottom: 3px; 
}

QTabBar::tab:hover { 
background-color: #333333; 
border: 1px solid #444444; 
border-bottom: none; 
}

QTabBar::tab:selected { 
background-color: #111111; 
border: 1px solid #333333; 
border-top: 1px solid yellow; 
border-bottom: none; 
color: yellow 
}

/* === QToolBar === */

QToolBar { 
background-color: #222222; 
border: none; 
padding: 1px; 
}

QToolBar:handle { 
background: #222222; 
border-left: 1px dotted yellow; 
color: #BBBBBB; 
}

QToolBar::separator { 
width: 6px; 
background-color: #222222; 
}

/* === QToolButton === */

QToolButton { 
border: 1px solid #333333; 
margin: 1px; 
}

QToolButton:hover { 
background-color: #333333; 
border: 1px solid #444444; 
}

QToolButton[popupMode=”1”] { /* only for MenuButtonPopup */ 
padding-right: 20px; /* make way for the popup button */ 
}

QToolButton::menu-button { 
border-left: 1px solid #333333; 
background: transparent; 
width: 16px; 
}

QToolButton::menu-button:hover { 
border-left: 1px solid #444444; 
background: transparent; 
width: 16px; 
}

QToolButton:checked, QToolButton:pressed { 
background-color: #111111; 
color: yellow; 
}

/* === QMenu === */

QMenu { 
background-color: black; 
border: 1px solid gray; 
color: white; 
padding: 1px; 
}

QMenu::item { 
padding: 2px 25px 2px 20px; 
border: 1px solid transparent; 
}

QMenu::item:disabled { 
color: #666666; 
}

QMenu::item:selected { 
border-color: gray; 
background: #222222; 
}

QMenu::icon:checked {

}

QMenu::separator { 
height: 1px; 
background: #222222; 
margin-left: 10px; 
margin-right: 10px; 
margin-top: 1px; 
margin-bottom: 1px; 
}

QMenu::indicator { 
width: 13px; 
height: 13px; 
}

/* === QMenuBar === */

QMenuBar { 
background-color: black; 
color: white; 
}

QMenuBar::item { 
background: transparent; 
}

QMenuBar::item:disabled { 
color: gray; 
}

QMenuBar::item:selected { 
background: #222222; 
}

QMenuBar::item:pressed { 
background: #444444; 
}

/* === QScrollBar:vertical === */

QScrollBar:vertical { 
background: #111111; 
width: 16px; 
margin: 16px 0 16px 0; 
}

QScrollBar::handle:vertical { 
background: #555555; 
min-height: 16px; 
}

QScrollBar::add-line:vertical { 
background: #444444; 
height: 16px; 
subcontrol-position: bottom; 
subcontrol-origin: margin; 
}

QScrollBar::sub-line:vertical { 
background: #444444; 
height: 16px; 
subcontrol-position: top; 
subcontrol-origin: margin; 
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { 
background: none; 
}

QScrollBar:up-arrow:vertical, QScrollBar:down-arrow:vertical { 
border: 2px solid #333333; 
width: 6px; 
height: 6px; 
background: #5f5f5f; 
}

/* === QScrollBar:horizontal === */

QScrollBar:horizontal { 
background: #111111; 
height: 16px; 
margin: 0 16px 0 16px; 
}

QScrollBar::handle:horizontal { 
background: #555555; 
min-width: 16px; 
}

QScrollBar::add-line:horizontal { 
background: #444444; 
width: 16px; 
subcontrol-position: right; 
subcontrol-origin: margin; 
}

QScrollBar::sub-line:horizontal { 
background: #444444; 
width: 16px; 
subcontrol-position: left; 
subcontrol-origin: margin; 
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { 
background: none; 
}

QScrollBar:left-arrow:horizontal, QScrollBar:right-arrow:horizontal { 
border: 2px solid #333333; 
width: 6px; 
height: 6px; 
background: #5f5f5f; 
}

/* =================== */

QLineEdit, QListView, QTreeView, QTableView, QAbstractSpinBox { 
background-color: black; 
color: #BBBBBB; 
border: 1px solid #333333; 
}

QAbstractScrollArea, QLineEdit, QTextEdit, QAbstractSpinBox, QComboBox { 
border-color: #333333; 
border: 1px solid #333333;

}

/* === QHeaderView === */

QHeaderView::section { 
background: #222222; 
border: 0; 
color: #BBBBBB; 
padding: 3px 0 3px 4px; 
}

/* === QListView === */ 
QListView::item:hover { 
background: #333333; 
}

QListView::item:selected { 
background: #111111; 
color: yellow; 
}

/* === QTableView === */ 
QTableView::item:hover { 
background: #333333; 
}

QTableView::item:hover { 
background: #111111; 
color: yellow; 
}

/* === QTreeView === */

QTreeView::item { 
background: black; 
}

QTreeView::item:hover { 
background: #333333; 
}

QTreeView::item:selected { 
background: #111111; 
color: yellow; 
}

QTreeView::branch {

}

QTreeView::branch:has-siblings:adjoins-item {

}

QTreeView::branch:has-siblings:!adjoins-item {

}

QTreeView::branch:closed:has-children:has-siblings {

}

QTreeView::branch:has-children:!has-siblings:closed {

}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {

}

QTreeView::branch:open:has-children:has-siblings {

}

QTreeView::branch:open:has-children:!has-siblings {

}

/* === Customizations === */

QFrame#infoLabel { 
border: 1px inset #333333; 
} 
2.

.QWidget { 
background-color: beige; 
}

QToolBar { 
background-color: beige; 
}

QDialog, QFileDialog { 
background-color: beige; 
}

QTabWidget::pane { /* The tab widget frame */ 
border-top: 2px solid #C2C7CB; 
}

QTabWidget::tab-bar { 
left: 5px; /* move to the right by 5px */ 
}

QTabBar, QTabWidget { 
background-color: beige; 
} 
QTabBar::tab { 
background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, 
stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, 
stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3); 
border: 1px solid darkkhaki; 
border-bottom-color: #C2C7CB; /* same as the pane color */ 
border-top-left-radius: 4px; 
border-top-right-radius: 4px; 
min-width: 8ex; 
padding: 2px; 
} 
QTabBar::tab:selected, QTabBar::tab:hover { 
background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, 
stop: 0 #fafafa, stop: 0.4 #f4f4f4, 
stop: 0.5 #e7e7e7, stop: 1.0 #fafafa); 
}

QTabBar::tab:selected { 
border-color: #9B9B9B; 
border-bottom-color: #C2C7CB; /* same as pane color */ 
}

QTabBar::tab:!selected { 
margin-top: 2px; /* make non-selected tabs look smaller */ 
}

/* Nice Windows-XP-style password character. */

QLineEdit[echoMode=”2”] { 
lineedit-password-character: 9679; 
}

QHeaderView::section { 
background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
stop:0 #616161, stop: 0.5 #505050, 
stop: 0.6 #434343, stop:1 #656565); 
color: white; 
padding-left: 4px; 
border: 1px solid #6c6c6c; 
}

QHeaderView::section:checked 
{ 
background-color: red; 
}

/* We provide a min-width and min-height for push buttons

so that they look elegant regardless of the width of the text. */ 
QPushButton { 
background-color: palegoldenrod; 
border-width: 2px; 
border-color: darkkhaki; 
border-style: solid; 
border-radius: 5; 
padding: 3px; 
min-width: 9ex; 
min-height: 2.5ex; 
}

QPushButton:hover { 
background-color: khaki; 
}

/* Increase the padding, so the text is shifted when the button is

pressed. */ 
QPushButton:pressed { 
padding-left: 5px; 
padding-top: 5px; 
background-color: #d0d67c; 
}

QLabel, QAbstractButton { 
font: bold; 
}

/* Mark mandatory fields with a brownish color. */

.mandatory { 
color: brown; 
}

/* Bold text on status bar looks awful. */

QStatusBar QLabel { 
font: normal; 
}

QStatusBar::item { 
border-width: 1; 
border-color: darkkhaki; 
border-style: solid; 
border-radius: 2; 
}

QStackedWidget, QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView, QWebView, QTreeView, QHeaderView { 
background-color: cornsilk; 
selection-color: #0a214c; 
selection-background-color: #C19A6B; 
}

QListView { 
show-decoration-selected: 1; 
}

QListView::item:hover { 
background-color: wheat; 
}

---- OK
/* We reserve 1 pixel space in padding. When we get the focus,
we kill the padding and enlarge the border. This makes the items glow. */ 
QLineEdit, QFrame { 
border-width: 1px; 
padding: 1px; 
border-style: solid; 
border-color: darkkhaki; 
border-radius: 5px; 
}

/* As mentioned above, eliminate the padding and increase the border. */

QLineEdit:focus, QFrame:focus { 
border-width: 3px; 
padding: 0px; 
}

/* A QLabel is a QFrame */

QLabel { 
border: none; 
padding: 0; 
background: none; 
}

/* A QToolTip is a QLabel */

QToolTip { 
border: 2px solid darkkhaki; 
padding: 5px; 
border-radius: 3px; 
opacity: 200; 
}

/* Nice to have the background color change when hovered. */

QRadioButton:hover, QCheckBox:hover { 
background-color: wheat; 
}

/* Force the dialog’s buttons to follow the Windows guidelines. */

QDialogButtonBox { 
button-layout: 0; 
}

3. 
/* 
Style by evilworks, 2012-2013. pollux@lavabit.com 
This file is Public Domain. 
*/

/* === Shared === */

QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, 
QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog, QTabBar { 
font-family: “Segoe UI”; 
background-color: #888; 
color: #000; 
}

/* === QWidget === */ 
QWidget:window { 
font-family: ‘Segoe UI’; 
background-color: #888; 
}

/* === QPushButton === */ 
QPushButton { 
border: 1px solid #555; 
padding: 4px; 
min-width: 65px; 
min-height: 12px; 
}

QPushButton:hover { 
background-color: #999; 
}

QPushButton:pressed { 
background-color: #333; 
border-color: #555; 
color: #AAA; 
}

QPushButton:disabled { 
color: #333333; 
}

/* === QComboBox === */ 
QComboBox { 
background-color: #AAA; 
border: 1px solid #555; 
color: black; 
}

QComboBox::drop-down { 
subcontrol-origin: padding; 
subcontrol-position: top right; 
border-left: 1px solid #333333; 
}

/* === QGroupBox === */ 
QGroupBox { 
border: 1px solid #555; 
margin-top: 2ex; 
}

QGroupBox::title { 
color: black; 
subcontrol-origin: margin; 
subcontrol-position: top left; 
border: 1px solid #555; 
}

/* === QTabBar === */ 
QTabBar::tab { 
border-bottom: none; 
color: #000; 
padding: 4px; 
background-color: #888; 
border: 1px solid #555; 
}

QTabBar::tab:hover { 
background-color: #AAA; 
}

QTabBar::tab:selected { 
background-color: #000; 
color: white; 
}

/* === QTabWidget === */ 
QTabWidget::pane { 
background: #888; 
border: 1px solid #555; 
}

/* === QToolBar === */ 
QToolBar { 
background: #949494; 
border: none; 
padding-left: 0px; 
padding-right: 0px; 
margin: 2px; 
}

QToolBar::separator { 
width: 1px; 
margin-left: 3px; 
margin-right: 3px; 
background-color: #555; 
}

/* === QToolButton === */ 
QToolButton { 
border: 1px solid #666; 
margin: 1px; 
}

QToolButton:hover { 
background-color: #AAA; 
}

QToolButton[popupMode=”1”] { /* only for MenuButtonPopup */ 
padding-right: 20px; /* make way for the popup button */ 
}

QToolButton::menu-button { 
border-left: 1px solid #666; 
background: transparent; 
width: 16px; 
}

QToolButton::menu-button:hover { 
border-left: 1px solid #666; 
background: transparent; 
width: 16px; 
}

QToolButton:checked, QToolButton:pressed { 
background-color: #000; 
border: 1px solid #555; 
color: white; 
}

/* === QScrollBar:vertical === */ 
QScrollBar:vertical { 
width: 16px; 
margin: 16px 0 16px 0; 
background: #333; 
}

QScrollBar::handle:vertical { 
background: #888; 
min-height: 16px; 
border-top: 1px solid #666; 
border-bottom: 1px solid #666; 
}

QScrollBar::add-line:vertical { 
background: #888; 
height: 16px; 
subcontrol-position: bottom; 
subcontrol-origin: margin; 
}

QScrollBar::sub-line:vertical { 
background: #888; 
height: 16px; 
subcontrol-position: top; 
subcontrol-origin: margin; 
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { 
background: none; 
}

/* === QScrollBar:horizontal === */ 
QScrollBar:horizontal { 
height: 16px; 
margin: 0 16px 0 16px; 
background: #333; 
}

QScrollBar::handle:horizontal { 
background: #888; 
min-width: 16px; 
border-left: 1px solid #666; 
border-right: 1px solid #666; 
}

QScrollBar::add-line:horizontal { 
background: #888; 
width: 16px; 
subcontrol-position: right; 
subcontrol-origin: margin; 
}

QScrollBar::sub-line:horizontal { 
background: #888; 
width: 16px; 
subcontrol-position: left; 
subcontrol-origin: margin; 
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { 
background: none; 
}

/* === QMenu === */ 
QMenu { 
background-color: black; 
border: 1px solid gray; 
color: white; 
padding: 1px; 
}

QMenu::item { 
padding: 2px 25px 2px 20px; 
border: 1px solid transparent; 
}

QMenu::item:disabled { 
color: #666666; 
}

QMenu::item:selected { 
border-color: gray; 
background: #222222; 
}

QMenu::icon:checked {

}

QMenu::separator { 
height: 1px; 
background: #222222; 
margin-left: 10px; 
margin-right: 10px; 
margin-top: 1px; 
margin-bottom: 1px; 
}

QMenu::indicator { 
width: 13px; 
height: 13px; 
}

/* === QMenuBar === */ 
QMenuBar { 
background-color: black; 
color: white; 
}

QMenuBar::item { 
background: transparent; 
}

QMenuBar::item:disabled { 
color: gray; 
}

QMenuBar::item:selected { 
background: #222222; 
}

QMenuBar::item:pressed { 
background: #444444; 
} 
/* =================== */ 
QLineEdit, QListView, QTreeView, QTableView, QAbstractSpinBox { 
background-color: #AAA; 
color: #000; 
border: 1px solid #555; 
}

QAbstractScrollArea, QLineEdit, QTextEdit, QAbstractSpinBox, QComboBox { 
border: 1px solid #555; 
}

/* === QHeaderView === */ 
QHeaderView::section { 
height: 20px; 
}

QHeaderView::section { 
background: #666; 
border: 0; 
color: #000; 
padding-left: 4px; 
}

/* === QListView === */ 
QListView::item:hover { 
background: #AAA; 
}

QListView::item:selected { 
background: #333; 
color: #AAA; 
}

/* === QTableView === */ 
QTableView::item:hover { 
background: #333333; 
}

QTableView::item:hover { 
background: #111111; 
color: yellow; 
}

/* === QTreeView === */ 
QTreeView::item { 
background: #AAA; 
}

QTreeView::item:hover { 
background: #CCC; 
}

QTreeView::item:selected { 
background: #333; 
color: #AAA; 
}

QTreeView::branch {

}

QTreeView::branch:has-siblings:adjoins-item {

}

QTreeView::branch:has-siblings:!adjoins-item {

}

QTreeView::branch:closed:has-children:has-siblings {

}

QTreeView::branch:has-children:!has-siblings:closed {

}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {

}

QTreeView::branch:open:has-children:has-siblings {

}

QTreeView::branch:open:has-children:!has-siblings {

}

--------------------------------------------------------------------------
-- ok
QPushButton {
    font-family: "Microsoft YaHei";
    font-size: 16px;
    color: #BDC8E2;
    font-style: italic;
    font-weight: bold;

    text-align: left center;
    padding-left: 25px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: aqua;
    border-radius: 20px;

    background-color: #2E3648;
    background-image: url("./image.png");
    background-repeat: no-repeat;
    background-position: left center;
}
QPushButton:hover{
    color: red;
    border-color: green;
    background-color: aqua;
}
QPushButton:pressed{
    color: green;
    border-color: blueviolet;
    background-color: black;
}

QLabel{
    font-family: "FangSong";
    font-size: 15px;
    color: #BDC8E2;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #808080;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}
Numeric {
    font-family: "FangSong";
    font-size: 28px;
    color: #FAEBD7;

    font-weight: bold;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #696969;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}
————————————————

-- ok
QLabel{
    font-family: "FangSong";
    font-size: 15px;
    color: white;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #808080;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}
Numeric {
    font-family: "FangSong";
    font-size: 28px;
    color: white;

    font-weight: bold;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #696969;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}

----ok
QPushButton {
    font-family: "Microsoft YaHei";
    font-size: 16px;
    color: #BDC8E2;
    font-style: italic;
    font-weight: bold;

    text-align: center;
    padding-left: 10px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: aqua;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
}
QPushButton:hover{
    color: red;
    border-color: green;
    background-color: aqua;
}
QPushButton:pressed{
    color: green;
    border-color: blueviolet;
    background-color: black;
}

QLabel{
    font-family: "FangSong";
    font-size: 15px;
    color: #BDC8E2;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #808080;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}

QLineEdit, QFrame { 
border-width: 1px; 
padding: 1px; 
border-style: solid; 
border-color: darkkhaki; 
border-radius: 5px; 
}

Numeric {
    font-family: "FangSong";
    font-size: 28px;
    color: green;

    font-weight: bold;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #696969;
    border-radius: 20px;

    background-color: black;
    background-repeat: no-repeat;
    background-position: left center;
}
//------------------------------------------------------

----ok
QPushButton {
    font-family: "Microsoft YaHei";
    font-size: 16px;
    color: #BDC8E2;
    font-style: italic;
    font-weight: bold;

    text-align: left center;
    padding-left: 25px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: aqua;
    border-radius: 20px;

    background-color: #2E3648;
    background-image: url("./image.png");
    background-repeat: no-repeat;
    background-position: left center;
}
QPushButton:hover{
    color: red;
    border-color: green;
    background-color: aqua;
}
QPushButton:pressed{
    color: green;
    border-color: blueviolet;
    background-color: black;
}

QLabel{
    font-family: "FangSong";
    font-size: 15px;
    color: #BDC8E2;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #808080;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}
Numeric {
    font-family: "FangSong";
    font-size: 28px;
    color: #FAEBD7;

    font-weight: bold;

    text-align: left;
    padding-left: 5px;
    padding-top: 0px;

    border-style: solid;
    border-width: 2px;
    border-color: #696969;
    border-radius: 20px;

    background-color: #2E3648;
    background-repeat: no-repeat;
    background-position: left center;
}

QFrame { 
   border-width: 1px; 
   padding: 1px; 
   border-style: solid; 
   border-color: darkkhaki; 
   border-radius: 5px; 
}
```