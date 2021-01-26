# QT中的属性系统

## 参考资料
> https://zhuanlan.zhihu.com/p/43348546


## 元对象系统(Meta-Object System)
备注：详见QT帮助中'QMetaObject Struct'  
1. 基本概念
Qt的元对象系统提供了对象之间通信的信号与槽机制、运行时类型信息和动态属性系统  
2. 元对象系统由以下三个基础组成：
2.1 QObject类是所有使用元对象系统的类的基类  
2.2 在一个类的private部分声明Q_OBJECT宏，然后类就可以使用元对象的信号与槽等各种特性  
2.3 MOC为每个QObject的子类提供必要的代码来实现元对象系统的特性  
Q_OBJECT宏在编译时会被元对象编译器MOC(Meta-Object Compiler)处理  
并生成源代码文件，例如moc_*.cpp，其中包含相应类的元对象代码  
3. 元对象系统提供的其他功能：


## 动态属性系统
1. 动态属性的定义
动态属性是指在运行时向类的实例化对象添加的新属性  
与Q_PROPERTY宏添加的属性不同，动态属性相当于一个临时属性  
动态属性只能添加到QObject实例中的，而不是添加到最核心的QMetaObject中  
2. 用setPorperty()函数添加动态属性
setPorperty()函数传递一个属性名和一个属性值  
如果属性名已经存在，且属性值兼容，则改变原有属性值，并返回ture  
如果属性名已经存在，但属性值不兼容，则原有属性值不变，并返回false  
如果属性名还不存在，则向类中添加一个新的动态属性，但是仍然返回false  
注意：根据返回false不能够判断是否添加了动态属性  
3. 用setPorperty()函数删除动态属性
setPorperty()函数通过传递属性名和一个非法的QVariant值就可以删除该动态属性  
其中，QVariant的默认构造函数就可以构造出一个非法的QVariant值  
4. 在Designer中添加动态属性
在QT Designer中可以选择指定组件，然后通过UI界面进行动态属性的添加  
在属性编辑器中，可以添加动态属性的名称、类型、属性值  



## Q_PROPERTY宏
备注：详见QT帮助中'The Property System'  
1. 基本功能
Q_PROPERTY宏是属于QObject类中的一个宏  
对于一个继承于QObject的类，这个宏用来声明类中的属性并注册到QT的属性系统中  
这些属性看上去就像是类中成员变量，但通过元对象系统，它们可以具有额外的特征  
2. 基本格式
属性的类型、名字和READ函数是必须填写的  
其中，数据类型可以是QVariant支持的任意类型，也可以是用户自定义的类型  
其他所有选项都是选填的，但一般会把WRITE函数也填写上  
所有bool选项的默认值都是true，除了USER选项的默认值为false  
```
 Q_PROPERTY(type name
            (READ getFunction [WRITE setFunction] |
             MEMBER memberName [(READ getFunction | WRITE setFunction)])
            [RESET resetFunction]
            [NOTIFY notifySignal]
            [REVISION int]
            [DESIGNABLE bool]
            [SCRIPTABLE bool]
            [STORED bool]
            [USER bool]
            [CONSTANT]
            [FINAL])
            [REQUIRED]
```
2.1 READ  
如果指定的是一个非MEMBER变量，要求后面有一个读函数用来读取属性值  
一般来说，读函数最好是const类型的  
2.2 WRITE  
写函数是可选的，用来设置属性值  
写函数的返回值必须为void，而且只能带有一个参数  
其中，Read-only类型的属性没有写函数  
2.3 MEMBER  
要想将类中已有的成员变量设置为属性值，需要用MEMBER关键字  
这使得给定的MEMBER变量在不需要创建读写函数的情形下实现可读可写  
如果需要控制变量，也允许对MEMBER变量额外使用读函数或写函数(但不能同时使用)  
2.4 RESET  
RESET函数用来将属性值重置回它的默认值  
RESET函数返回类型必须为void，并且不带任何参数  
2.5 NOTIFY  
无论何时当属性值改变时，就会发射出一个指定的信号函数  
这个信号函数必须是在类中已经存在的函数(信号函数是在同一个类中进行自定义的)  
对于MEMBER变量，信号函数必须带有0个或1个参数  
参数的类型必须和属性的类型相同，参数会变成改变后的新的属性值  
对于MEMBER属性，QT会在需要时自动发出信号函数  
注意：NOTIFY必须是允许QML属性绑定的特定信号函数  
3. READ、WRITE和MEMBER的区别
READ、WRITE和MEMBER两种方法都可以赋予属性值读/写  
注意：READ、WRITE和MEMBER不能同时使用，赋予可读可写特性一次就够了，不能赋予两次  
方法一：用READ、WRITE，那么直接调用指定的函数即可  
这种方法的效率更高、速度更快，而且在编译阶段就可以进行类型检查  
缺点就是还没运行前你就得了解这个类是有setFocus()这个函数  
```
Widget *w = new Widget;
w->setFocus(true);
```
方法二：用MEMBER，那么用QObject的property()和setProperty()两个函数  
采用这种方法，我们不需要知道这个类有啥函数、有啥变量，只需要知道这个类有一个叫'focus'的属性值就可以了  
```
Widget *w = new Widget;
w->property("focus");
w->setProperty("focus", true);
```


## 代码示例
备注：Q_PROPERTY宏的代码都是写在类定义的内部中  
1. 使用MEMBER关键字可以把成员变量扩展为QT的属性
focus是布尔类型的属性，对应类中的成员变量m_focus  
```
Class Widget : public QObject
{
    Q_PROPERTY(bool focus MEMBER m_focus)
    Q_OBJECT
public:
    bool hasFocus() const;
    void setFocus(bool on);
private:
    bool m_focus;
}
```
2. 给某个属性设置关联的信号函数
备注：信号函数在类中声明为signals即可，不需要再写出其具体定义  
```
class QDESIGNER_WIDGET_EXPORT CustomButton : public QWidget
{
    Q_OBJECT
    Q_PROPERTY(bool Value READ Value WRITE SetValue NOTIFY valuechanged) //NOTIFY关键字后面是信号函数

public:
    CustomButton(QWidget *parent = 0);

public:
    bool Value();
    void SetValue(bool value);

signals:
    void valuechanged(); //信号函数声明
}
```
在写函数的具体定义中要加上触发信号函数的语句  
使用emit关键字表示触发信号函数  
```
void CustomButton::SetValue(bool value)
{
    qt_button -> SetValue(value);
    emit valuechanged(); //执行写函数时触发信号函数
}
```
3. 枚举类型的属性
对于枚举类型的变量，只要把定义写在类的内部，在属性编辑器中就会自动显示为下拉菜单的形式  
```
class QDESIGNER_WIDGET_EXPORT CustomButton : public QWidget
{
    Q_OBJECT
    Q_PROPERTY(MyModes Mode READ Mode WRITE SetMode)//注意这里类型写的是MyModes，不是enum

public:
    CustomButton(QWidget *parent = 0);

public:
    //设置按钮的模式，枚举范围1-3
    enum MyModes {
        cwModeSwitchWhenPressed = 1,
        cwModeSwitchUntilReleased= 2,
        cwModeIndicator         = 3
        };
    Q_ENUM(MyModes)
    MyModes Mode();
    void SetMode(MyModes mode);
```
注意事项：  
3.1 枚举变量要用Q_ENUM()宏进行注册声明，而且宏声明要放在枚举变量定义的后面  
3.2 枚举变量的定义一定要写到这个类的内部，否则这个属性在属性编辑器里显示不出来  
如果在其他头文件中（非类的内部）定义了枚举变量，即使include了这个头文件也不行  
使用其他地方的枚举变量不会报错，但在属性编辑器中就显示不出这条属性了  
备注：实际中遇到了这个问题，要用到的枚举变量在其他头文件中，而且不是在类的内部  
解决办法是在这个类的内部再写一个名字不同但内容相同的枚举变量，然后用函数把两个枚举变量对应起来  
3.3 对于其他类中定义的枚举变量，也可以在这个类中添加为属性  
但是要求写上全名(OtherClass::MyModes)，而且其他类也必须继承于QObject，并用Q_ENUM()宏进行注册  
4. 非QT标准类型的属性类型
以引入Labview中的CWButton拨杆按钮为例：  
一般常见的属性类型都是QString、QColor、int、bool等标准的属性类型  
但在CWButton的项目中，这个按钮还有一些自定义的类型，例如：  
```
class CWUICONTROLSLIB_EXPORT CWPictureDisp : public QAxObject
{
public:
    explicit CWPictureDisp(IDispatch *subobject = nullptr, QAxObject *parent = nullptr);
......
}

class CWUICONTROLSLIB_EXPORT CWButton : public QAxWidget
{
    inline CWUIControlsLib::CWPictureDisp* BackgroundImage() const;
    inline void SetBackgroundImage(CWUIControlsLib::CWPictureDisp* value);
......
}
```
上面的这个CWPictureDisp类型就是一个自定义的类型，用来传输图片对象  
根据网上，自定义的属性类型需要用Q_DECLARE_METATYPE宏进行注册，这样就可以存储在QVariant中了  
但是具体怎么添加这种类型的属性一直还没有测试成功，总是有各种报错  


## Q_ENUM宏
Q_ENUM()宏是属于QObject类中的一个宏  
枚举类型的变量必须要用Q_ENUM()宏来注册声明到元对象系统中  
注册之后元对象系统就能识别到枚举变量的名称，进而能调用setProperty()函数  


## Q_CLASSINFO宏
Q_CLASSINFO宏以键值对的形式向类中添加额外的的信息，并连接到属性系统  
Q_CLASSINFO宏可以将额外的'name-value'对加入到一个类的元对象中  
头文件示例：在类中添加宏  
```
Q_CLASSINFO("Version", "3.0.0")
Q_CLASSINFO("Name", "SkyplotWidget")
```
源文件示例：输出查看name和value值  
```
qDebug() << skyplotWidget -> metaObject() -> classInfo(0).name();
qDebug() << skyplotWidget -> metaObject() -> classInfo(0).value();
qDebug() << skyplotWidget -> metaObject() -> classInfo(1).name();
qDebug() << skyplotWidget -> metaObject() -> classInfo(1).value();
```
