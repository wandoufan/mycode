# QLabel

## 基本功能
QLabel用来显示一个文本或者图片  
父类：QFrame  
子类：无  


## 构造函数
1. QLabel::QLabel(const QString &text, QWidget \*parent = nullptr, Qt::WindowFlags f = Qt::WindowFlags())
```
QLabel * label1 = new QLabel("输入：");
```

2. QLabel::QLabel(QWidget \*parent = nullptr, Qt::WindowFlags f = Qt::WindowFlags())


## 常用成员变量
1. alignment : Qt::Alignment
这个属性设置标签中内容的摆放位置，默认位置为：水平方向靠左，垂直方向居中  
属性取值详见namespace中enum Qt::AlignmentFlag  
1.1 Qt::Alignment alignment() const
1.2 void setAlignment(Qt::Alignment)

2. hasSelectedText : const bool
这个属性保存是否有任何文本内容被选中，默认为false  
备注：实测发现标签中的文本无法被鼠标选中  
2.1  bool hasSelectedText() const

3. indent : int

4. margin : int
这个属性设置标签中内容和边框的间距，默认为0  
4.1 int margin() const
4.2 void setMargin(int)

5. openExternalLinks : bool

6. pixmap : QPixmap
这个属性设置标签中的图片  
备注：老版的pixmap()函数返回的是一个指针，新版的pixmap()函数返回的是一个对象，用函数参数Qt::ReturnByValue作为区分  
```
const QPixmap *pixmapPtr = label->pixmap();
QPixmap pixmapVal = label->pixmap(Qt::ReturnByValue);
```
6.1 QPixmap pixmap(Qt::ReturnByValueConstant) const
6.2 void setPixmap(const QPixmap &)

7. scaledContents : bool

8. selectedText : const QString
这个属性保存被选中的文本内容，如果没有选中任何文本，则返回一个空字符串  
备注：实测发现标签中的文本无法被鼠标选中  
8.1 QString selectedText() const

9. text : QString
这个属性设置标签中的文本内容  
9.1 QString text() const
9.2 void setText(const QString &)

10. textFormat : Qt::TextFormat
这个属性设置标签中文本的格式，默认格式为Qt::AutoText  
10.1 Qt::TextFormat textFormat() const
10.2 void setTextFormat(Qt::TextFormat)

11. textInteractionFlags : Qt::TextInteractionFlag
这个属性设置用户输入时的交互方式  

12. wordWrap : bool
这个属性设置标签中的文本内容是否会自动换行，默认为false  
12.1 bool wordWrap() const
12.2 void setWordWrap(bool on)


## 常用公共函数
1. QPicture QLabel::picture(Qt::ReturnByValueConstant) const
以QPicture的形式返回标签中的图片  
备注：老版的picture()函数返回的是一个指针，新版的picture()函数返回的是一个对象，用函数参数Qt::ReturnByValue作为区分  
```
const QPicture *picPtr = label->picture();
QPicture picVal = label->picture(Qt::ReturnByValue);
```


## 常用公共槽函数
1. [slot] void QLabel::clear()

