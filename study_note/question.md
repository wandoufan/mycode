# 问题

## C/C++
1. 怎么查看变量类型，不能用type()
2. .h类型的头文件作用
3. public和private关键字用的很频繁，在c和C++中怎么定义的
4. 
```
public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();
这里面的~是什么意思
```
5. 在类中嵌套定义一个类



## QT
1. SIGNAL和SLOT是QT的宏,在使用信号与槽的类中，必须在类的定义中加入宏 Q_OBJECT
宏是个什么概念？

2. ischecked是什么（一个布尔值）  
```
void QWDialog::setTextFontColor()
{
    QPalette plet=ui->txtEdit->palette();
    if (ui->rBtnBlue->isChecked())
        plet.setColor(QPalette::Text,Qt::blue);
    else if (ui->rBtnRed->isChecked())
       plet.setColor(QPalette::Text,Qt::red);
    else if (ui->rBtnBlack->isChecked())
        plet.setColor(QPalette::Text,Qt::black);
    else
       plet.setColor(QPalette::Text,Qt::black);
    ui->txtEdit->setPalette(plet);
}
```
注意：是Qt，不是QT
报错'rBtnBlue'无法识别，是不是教程里作者把radioButton改名了

3. clicked(bool)之后，checked是什么
```
void Dialog::on_checkBox_clicked(bool checked)
{
    QFont font = ui -> textEdit -> font();
    font.setUnderline(checked);
    ui -> textEdit -> setFont(font);
}
```
4. ui下到底有多少个类


## 待总结
1. 实际使用中发现：
如果选择plainTextEdit组件，则设置文本的下划线、斜体、粗体都正常
但如果选择了TextEdit组件，只有设置文本下划线是正常的
文本的斜体和粗体只能在程序运行之后再写入文字才能生效，且生效仅限一次
在编译之前就写好的文字则无法生效

2. checkBox(方块勾选)和radioButton(圆圈勾选)两种组件之间的区别：
多个checkBox可以同时选择，多个radioButton只能选择其中一个

3. 注意变量名的大小写，否则经常会报错变量名未定义

