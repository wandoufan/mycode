# QInputDialog

## 基本功能
QInputDialog提供了一个简单便利的对话框来获得用户输入的值  
QInputDialog的父类是QDialog  
注意：QInputDialog的对话框一次都只能输入一个数值  


## 输入多个信息
有时候我们需要在一个界面上让用户输入多组信息，如姓名、年龄、学号等  
使用QInputDialog输入多个数值时，需要弹出多个对话框，比较麻烦  
没有找到使用QInputDialog输入复杂信息的办法  
目前的办法是自己定义一个信息填写窗口，然后自己从窗口中获取输入值  


## 公共静态成员方法
备注：以下方法都可以直接使用，不需要实例化对象  
1. 输入一个浮点型数字
```
double 
QInputDialog::getDouble(QWidget *parent, const QString &title, const QString &label, double value = 0, double min = -2147483647, double max = 2147483647, int decimals = 1, bool *ok = nullptr, Qt::WindowFlags flags = Qt::WindowFlags(), double step = 1)
```
2. 输入一个整型数字
```
int 
QInputDialog::getInt(QWidget *parent, const QString &title, const QString &label, int value = 0, int min = -2147483647, int max = 2147483647, int step = 1, bool *ok = nullptr, Qt::WindowFlags flags = Qt::WindowFlags())
```
3. 选择Item中的一项，输入一行字符串
其中Item由QStringList &items进行定义，显示为下拉菜单的形式  
```
QString 
QInputDialog::getItem(QWidget *parent, const QString &title, const QString &label, const QStringList &items, int current = 0, bool editable = true, bool *ok = nullptr, Qt::WindowFlags flags = Qt::WindowFlags(), Qt::InputMethodHints inputMethodHints = Qt::ImhNone)
```
4. 弹出一个文本框，框内可以一次输入多行字符串
```
QString 
QInputDialog::getMultiLineText(QWidget *parent, const QString &title, const QString &label, const QString &text = QString(), bool *ok = nullptr, Qt::WindowFlags flags = Qt::WindowFlags(), Qt::InputMethodHints inputMethodHints = Qt::ImhNone)
```
5. 输入一行字符串
```
QString 
QInputDialog::getText(QWidget *parent, const QString &title, const QString &label, QLineEdit::EchoMode mode = QLineEdit::Normal, const QString &text = QString(), bool *ok = nullptr, Qt::WindowFlags flags = Qt::WindowFlags(), Qt::InputMethodHints inputMethodHints = Qt::ImhNone)
```