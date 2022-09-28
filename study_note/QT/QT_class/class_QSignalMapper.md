# QSignalMapper

## 基本功能
QSignalMapper用来在信号与槽机制中对信号函数进行二次转发，协助信号函数传递更多的参数给槽函数
QSignalMapper可以管理一组无参数的信号函数，然后在重新发出这些信号函数时，带上一个int、string、widget、object等类型的参数
父类：QObject  
子类：无  


## 注意事项
1. 在之前lambda表达式不能被当做槽函数时，QSignalMapper类被广泛使用，但现在整个QSignalMapper类目前都已经过时，不建议在高版本Qt中使用，推荐使用lambda表达式代替  

2. QSignalMapper一次也最多只能传递一个参数

3. 使用QSignalMapper进行转发的信号函数本身不能带有任何参数，即使带了也用不了

4. 使用QSignalMapper机制之后，在槽函数中就无法获取到真正的sender对象，这里的objectName()输出为空
```
qDebug() << sender() -> objectName();
```


## 应用场景
例如：多个checkBox控件的clicked()信号都关联到了同一个槽函数上，需要在槽函数内部知道到底是哪个checkBox控件被触发了  


## 构造函数
1. QSignalMapper::QSignalMapper(QObject \*parent = nullptr)


## 常用公共函数：获取map映射关系
1. QObject \*QSignalMapper::mapping(int id) const
用整型数字的形式返回sender对象  

2. QObject \*QSignalMapper::mapping(const QString &id) const
用字符串的形式返回sender对象 

3. QObject \*QSignalMapper::mapping(QWidget \*widget) const
用widget的形式返回sender对象 

4. QObject \*QSignalMapper::mapping(QObject \*object) const
用QObject的形式返回sender对象 


## 常用公共函数：设置map映射关系
1. void QSignalMapper::setMapping(QObject \*sender, int id)
添加一个映射关系：当sender对象发出信号，然后触发了map()槽函数时，就会发出mapped(id)信号

2. void QSignalMapper::setMapping(QObject \*sender, const QString &text)

3. void QSignalMapper::setMapping(QObject \*sender, QWidget \*widget)

4. void QSignalMapper::setMapping(QObject \*sender, QObject \*object)


## 常用公共函数：删除map映射关系
1. void QSignalMapper::removeMappings(QObject \*sender)
删除sender对象上所有的映射关系  
备注：当映射对象被销毁时会自动执行这一操作  
注意：这一操作不会断开任何信号的connect()关联关系  


## 公共槽函数
1. [slot] void QSignalMapper::map()
当sender对象发送信号函数触发了map()槽函数之后，map()槽函数就会发出mapped()信号  

2. [slot] void QSignalMapper::map(QObject \*sender)


## 信号函数
1. [signal] void QSignalMapper::mapped(int i)

2. [signal] void QSignalMapper::mapped(const QString &text)

3. [signal] void QSignalMapper::mapped(QWidget \*widget)

4. [signal] void QSignalMapper::mapped(QObject \*object)


## 代码示例
```
QSignalMapper *signalmapper;
signalmapper = new QSignalMapper(this);
//把每个按钮的clicked()信号都绑定到QSignalMapper的map()槽函数上
connect(ui -> pushButton, SIGNAL(clicked()), signalmapper, SLOT(map()));
connect(ui -> pushButton_2, SIGNAL(clicked()), signalmapper, SLOT(map()));
connect(ui -> pushButton_3, SIGNAL(clicked()), signalmapper, SLOT(map()));
connect(ui -> pushButton_4, SIGNAL(clicked()), signalmapper, SLOT(map()));
//设置每个按钮对象要传递给槽函数的参数
signalmapper -> setMapping(ui -> pushButton, "this is button_1");
signalmapper -> setMapping(ui -> pushButton_2, "this is button_2");
signalmapper -> setMapping(ui -> pushButton_3, "this is button_3");
signalmapper -> setMapping(ui -> pushButton_4, "this is button_4");
//把QSignalMapper的mapped()信号绑定到真正的槽函数click_test1()上
connect(signalmapper, SIGNAL(mapped(QString)), this, SLOT(click_test1(QString)));

//槽函数定义
void MainWindow::click_test1(QString info)
{
    qDebug() << info;
}
```






