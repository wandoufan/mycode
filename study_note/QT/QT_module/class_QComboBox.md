# QComboBox

## 基本功能
QComboBox组件是一个下拉式菜单，结合了按钮和弹出式列表  


## 构造函数
1. QComboBox::QComboBox(QWidget \*parent = nullptr)


## 常用函数
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

5. int QComboBox::currentIndex() const
返回当前选择选项对应的index，index从0开始  

6. QString QComboBox::currentText() const
返回当前选择选项对应的text  

7. QVariant QComboBox::currentData(int role = Qt::UserRole) const
返回当前选择选项关联是数据  

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