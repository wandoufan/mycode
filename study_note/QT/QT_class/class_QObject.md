# QObject

## 基本功能
QObject类是所有QT对象的基类  
QObject提供了强大的信号与槽机制和元对象系统等各种功能  


## Q_OBJECT宏
1. Q_OBJECT宏一般写在类的最上方，用来声明使用元对象系统的相关功能  
而且这个类必须是继承于QObject的子类才能使用Q_OBJECT宏  
对于不是QObject子类的类，使用Q_GADGET宏可以使元对象系统支持类中的枚举类型  
2. 每个包含了Q_OBJECT宏的类，都会产生一个元对象  
有了元对象以后，这个类才能使用信号与槽函数、属性系统等等  
因此使用信号槽函数、属性系统的类都必须在内部写上Q_OBJECT  
3. Q_OBJECT宏在编译时会被元对象编译器MOC(Meta-Object Compiler)处理  
并生成源代码文件，例如moc_*.cpp，其中包含相应类的元对象代码  


## Q_PROPERTY宏
详见QT_property.md  


## Q_ENUM()宏
详见QT_property.md  


## 属性相关的常用函数
1. QVariant QObject::property(const char \*name) const
返回对象的指定属性的值，参数为一个属性名称的字符串  
如果没有这样属性存在，那么返回一个非法的variant变量  
```
qDebug() << ui -> label -> property("text");
// return QVariant(QString, "demo2")
```
2. bool setProperty(const char \*name, const QVariant &value)
设置对象属性的值，第一个参数为属性名，第二个参数为属性值  
如果属性名已经存在，且属性值兼容，则改变原有属性值，并返回ture  
如果属性名已经存在，但属性值不兼容，则原有属性值不变，并返回false  
如果属性名还不存在，则向类中添加一个新的动态属性，但是仍然返回false  
注意：根据返回false不能够判断是否添加了动态属性  
备注：以前设置属性要调用不同的属性设置函数，现在可以统一用setProperty函数  
```
ui->label->setText("hello"); \\用label本身的函数设置属性
ui->label->setProperty("text", "hello"); \\用统一的函数设置属性
```
另外，还可以用setPorperty()函数删除动态属性  
setPorperty()函数通过传递属性名和一个非法的QVariant值就可以删除该动态属性  
其中，QVariant的默认构造函数就可以构造出一个非法的QVariant值  
3. [virtual] const QMetaObject \*QObject::metaObject() const
返回一个指向该对象的元对象的指针  
元对象包含了一个继承于QObject的类的信息，如类名、超类名、属性、信号、槽  
具体能查看的信息和调用的函数详见'QMetaObject Struct'  
```
qDebug() << mytext -> metaObject() -> className();
qDebug() << mytext -> metaObject() -> superClass();
qDebug() << mytext -> metaObject() -> propertyCount();
```
4. const QMetaObject QObject::staticMetaObject
staticMetaObject和上面的metaObject()功能类似  
如果没有一个指向对象实例的指针，但仍然想要获取元对象类的信息，可以用这个函数  
```
qDebug() << QPushButton::staticMetaObject.className();
```


