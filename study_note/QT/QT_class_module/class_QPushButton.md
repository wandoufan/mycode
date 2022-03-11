# QPushButton

## 基本功能
QPushButton是一个命令按钮  
父类：QAbstractButton  
子类：QCommandLinkButton  


## 构造函数
1. QPushButton::QPushButton(const QIcon &icon, const QString &text, QWidget \*parent = nullptr)
备注：由于C++的隐式类型转换机制，可以把一个QPixmap对象传递给icon参数  

2. QPushButton::QPushButton(const QString &text, QWidget \*parent = nullptr)

3. QPushButton::QPushButton(QWidget \*parent = nullptr)


## 常用成员变量
1. autoDefault : bool
这个属性设置按钮是否具有autoDefault属性  
autoDefault属性是指用户按下回车键之后就会触发该按钮的click()信号  
只有当按钮的parent是QDialog时，按钮才会具有autoDefault属性，否则一般按钮没有该属性  
1.1 bool autoDefault() const
1.2 void setAutoDefault(bool)

2. default : bool
这个属性设置按钮是否为默认按钮，属性默认为false  
2.1 bool isDefault() const
2.2 void setDefault(bool)

3. flat : bool
这个属性设置按钮的背景和边界能否可见，属性默认为false  
当把这个属性值设置为true之后，按钮的背景不可见，只能看见文本，只有点击按钮时才能看见其背景  
3.1 bool isFlat() const
3.2 void setFlat(bool)


## 常用公共函数
1. void setMenu(QMenu \*menu)
给按钮添加菜单功能，添加之后按钮就会出现下拉菜单和选项  
```
QMenu *menu1 = new QMenu("menu1");
QMenu *menu2 = new QMenu("其他");
menu1 -> addAction("设置");
menu1 -> addAction("版本检测");
menu1 -> addAction("关于我们");
menu2 -> addAction("选项一");
menu2 -> addAction("选项二");
menu1 -> addMenu(menu2);
QPushButton *button = new QPushButton("主菜单", this);
button -> setMenu(menu1);
```

2. QMenu \*menu() const