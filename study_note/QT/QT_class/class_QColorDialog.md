# QColorDialog

## 基本功能
QColorDialog提供了一个对话窗口来让用户挑选颜色  
QColorDialog的父类是QDialog  
经常有需求是让用户自己设置颜色，如果让用户输入RGB的值，接收后再转换为颜色，就非常麻烦了  
使用QColorDialog可以很方便的让用户选择颜色并返回一个QColor  


## 公共静态成员方法
1. 弹出一个颜色选择对话框(最常用函数)
```
[static] QColor QColorDialog::getColor(const QColor &initial = Qt::white, QWidget *parent = nullptr, const QString &title = QString(), QColorDialog::ColorDialogOptions options = ColorDialogOptions())
```
如果用户点击'ok'，则返回用户选择的QColor  
如果用户点击'Cancel'或关闭对话框，则返回一个invalid color  
备注：返回值是否合法取决于用户点击了哪个按钮，与用户是否选择了颜色无关  
```
button_color = QColorDialog::getColor();
//用isValid()函数判断返回值是否合法
if(button_color.isValid())
{
    qDebug() << "valid color";
    qDebug() << button_color;
}
else
{
    qDebug() << "invalid color";
    qDebug() << button_color;
}
```

2. [static] void QColorDialog::setCustomColor(int index, QColor color)
设置某个自定义颜色对应的index  
备注：这个函数在macOS平台上不能使用  

3. [static] QColor QColorDialog::customColor(int index)
用给定的index作为QColor的值，并返回这个自定义的颜色  
使用该函数之前要先用 函数进行相应的设置  
