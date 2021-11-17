# QComboBox

## 基本功能
QComboBox组件是一个下拉式菜单，结合了按钮和弹出式列表  


## 使用技巧
1. 一般在用addItem添加菜单选项时，要把选项对应的关联数据(枚举变量值)也添加上  
这样以后可以直接使用currentData()方法获取关联数据，不必再用if-else结构逐个判断当前选项并设置对应变量值  
备注：currentData()方法获得的是QVariant类型数据，要转换成需要的类型  
```
serialport -> setBaudRate(ui -> comboBox_1 -> currentData().value<qint32>());
serialport -> setDataBits(ui -> comboBox_2 -> currentData().value<QSerialPort::DataBits>());
```
2. 如果想通过designer界面去添加菜单选项，需要对currentText、currentIndex等属性进行设置  


## 构造函数
1. QComboBox::QComboBox(QWidget \*parent = nullptr)


## 常用成员变量
1. currentIndex : int
currentIndex属性表示当前菜单选项对应的索引，索引值从0开始  
对于一个空的QComboBox对象，其currentIndex属性值为-1  
1.1 读函数  
int QComboBox::currentIndex() const
1.2 写函数  
void QComboBox::setCurrentIndex(int index)
1.3 信号函数  
[signal] void QComboBox::currentIndexChanged(int index)

2. currentText : QString
currentIndex属性表示当前菜单选项对应的内容  
2.1 读函数  
QString QComboBox::currentText() const
2.2 写函数  
void QComboBox::setCurrentText(const QString &text)
2.3 信号函数  
[signal] void QComboBox::currentTextChanged(const QString &text)


## 常用公共函数
1. void QComboBox::addItem(const QString &text, const QVariant &userData = QVariant())
向下拉菜单中以'append'方式添加选项，选项显示顺序与添加的先后顺序一致  
第一个参数为选项的文本内容  
第二个参数为选项关联的数据，常用枚举变量的值  
```
public:
   enum SVisible {Full, Half, Zero};
   Q_ENUM(SVisible)
QComboBox *choose_visible;

choose_visible = new QComboBox(this);
choose_visible -> addItem("Visible", Full);
choose_visible -> addItem("HalfVisible", Half);
choose_visible -> addItem("Invisible", Zero);
```
备注：当关联数据使用枚举值时，如何获取选择的值还没有搞清楚，currentData()函数返回的是QVariant类型，不知道怎么转换回自定义的enum类型  
另外，添加选项也可以不关联数据，只写一个文本内容
```
choose_visible -> addItem("Visible");
```

2. void QComboBox::addItem(const QIcon &icon, const QString &text, const QVariant &userData = QVariant())
和上面函数的功能一样，区别在于多了一个图标参数  

3. void QComboBox::addItems(const QStringList &texts)
用字符串列表的形式向菜单中一次添加多个选项  

4. void QComboBox::setItemText(int index, const QString &text)
设置指定选项的文本内容，其中index从0开始  

7. QVariant QComboBox::currentData(int role = Qt::UserRole) const
返回当前选择选项关联的数据  

8. int QComboBox::count() const
返回总的选项个数  


## 公共槽函数
1. [slot] void QComboBox::clear()
清除ComboBox，删除所有的选项  

2. [slot] void QComboBox::clearEditText()
清除ComboBox所有行的文本内容  

3. void QComboBox::setCurrentIndex(int index)
通过index来设置下拉菜单显示的默认选项（常用）  

4. void QComboBox::setCurrentText(const QString &text)
设置选项的文本内容  

5. void QComboBox::setEditText(const QString &text)
在ComboBox的文本编辑器中设置文本内容  