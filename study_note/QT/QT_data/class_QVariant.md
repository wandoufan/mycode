# QVariant

## 基本功能
QVariant类提供了QT的通用数据类型的封装容器，支持几乎所有QT数据类型，有点类似json  
支持的类型包括int、float、char、json、bool、bytearray、list、hash、string等等  
如果有几种不同类型的数据需要传递，QVariant常用来替代结构体struct  
导出QVariant的数据类型和导入QVariant的数据类型是一致的  
注意：QVariant变量中一次只能存放一个数据，不能同时存储多个数据  


## 使用示例
1. 使用setValue()函数来添加数据  
```
QVariant v;
v.setValue("abc");
```
2. 以下两种方法在创建QVariant变量时直接添加数据  
```
QVariant v_string("abc");
QVariant v_string = "abc";
```
3. 可以直接作为一个函数参数，不需要再创建一个QVariant类型的变量，减少变量命名
```
item->setData(Qt::DecorationRole, QVariant(inner_color));
```
4. 把一个QVariant对象转换成指定的数据类型
```
result = variant1.value<qint32>();//转换成qint32型
result = variant2.value<QSerialPort::DataBits>();//转换成enum QSerialPort::DataBits
```


## 构造函数
QVariant的构造函数非常多，几乎每种数据类型都对应有一个QVariant  
特别的，可以将自定义的struct类型转换为QVariant类型  
备注：需要用到Q_DECLARE_METATYPE宏，详见QT_property.md  
```
//构建一个列表，其中列表的元素是自定义出来的结构体  
struct ChannelInfo{
    int id;
    QString text;
};
Q_DECLARE_METATYPE(ChannelInfo)

QVariant channel_info;
QList<QVariant> all_channel_info;

ChannelInfo mychannel;//创建一个结构体并赋值
mychannel.id = i;
mychannel.text = QString::number(i);
channel_info.setValue(mychannel);//将结构体转换为QVariant
all_channel_info.append(channel_info);//将QVariant添加到列表里
```


## 数据类型转换相关的常用公共函数
1. template <typename T> T QVariant::value() const
把QVariant变量转换为模板类型T，转换前要先用canConvert()判断是否可以转换  
```
//将struct转换得到的QVariant，再转换回struct
QVariant v;
MyCustomStruct c;

if (v.canConvert<MyCustomStruct>())
{
	c = v.value<MyCustomStruct>();
}
```

2. int QVariant::toInt(bool \*ok = nullptr) cons
如果数据是数字、字符、字符串、布尔型等，就以int形式返回；否则，返回0  
如果数据可以被转换为int类型，则ok指针会被设置为true；否则，ok指针设置为false  
备注：这里没有搞太懂，实际使用时可以不写ok参数  

3. bool QVariant::toBool() const

4. QChar QVariant::toChar() const

5. QString QVariant::toString() const

6. QStringList QVariant::toStringList() const

7. QTime QVariant::toTime() const

8. QSize QVariant::toSize() const

9. QPoint QVariant::toPoint() const


## QVariant转换为QColor等类型的注意事项
因为QVariant是Qt Core模块的一部分，因此不能提供函数来转换到Qt GUI中的数据类型(如： QColor、QImage、QPixmap等类型)  
也就是说，没有QVariant::toColor()这个函数  
可以使用QVariant::value()函数来实现QVariant转换为QColor  
```
QVariant v_color;
QColor color = v_color.value<QColor>();
```
备注：将QColor等类型转换为QVariant类型则不存在这个问题，可以直接转换  
```
QColor color = palette().background().color();
QVariant v_color = color;
```


## 常用公共函数
1. QVariant::Type QVariant::type() const
以QVariant::Type的类型返回QVariant中存储的数据类型  
备注：不知道QVariant::Type类型怎么用  

2. const char \*QVariant::typeName() const
以char的形式返回QVariant中存储的数据类型  

3. template <typename T> bool QVariant::canConvert() const
判断QVariant变量是否可以被转换成指定模板类型T，返回true或false  
```
//int型的QVariant既可以转换为int，也可以转换为QString
QVariant v = 42;
v.canConvert<int>();              // returns true
v.canConvert<QString>();          // returns true
//自定义的结构体型的QVariant只能转换回结构体类型
MyCustomStruct s;
v.setValue(s);
v.canConvert<int>();              // returns false
v.canConvert<MyCustomStruct>();   // returns true
```


