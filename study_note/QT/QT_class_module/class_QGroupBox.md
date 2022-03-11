# QGroupBox

## 基本功能
QGroupBox是一个带有标题的容器类组件  


## 构造函数
1. QGroupBox::QGroupBox(const QString &title, QWidget \*parent = nullptr)
创建一个带有标题的group box  

2. QGroupBox::QGroupBox(QWidget \*parent = nullptr)
创建一个不带标题的group box  


## 常用函数
* void QWidget::setLayout(QLayout \*layout)
设置group box的内部布局，这个虽然是所有QWidget组件都有的，但也很常用  
```
QGridLayout *glayout = new QGridLayout();
glayout -> addwidget(button1, 0, 0);
glayout -> addwidget(button2, 1, 0);
glayout -> addwidget(button3, 2, 0);

mygroupbox -> setLayout(glayout);
```

* QString QGroupBox::title() const
获取标题  

* void QGroupBox::setTitle(const QString &title)
设置标题  