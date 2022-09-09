# QDataStream

## 基本功能
QDataStream用来向QIODevice中提供序列化的二进制数据，即读写二进制数据  
父类：无  
子类：无  


## 详细功能
1. 读写原始的二进制数据
C++基本数据类型  
例如：char、short、int、char *  
2. 读写Qt容器类
例如：QList、QVector、QSet、QHash等  
3. 读写其他Qt类
几乎所有Qt支持的类型都可以用QDataStream处理  
例如：QBrush、QColor, QImage、QIcon、QPoint等等  


## QDataStream和QTextStream的对比
QTextStream和QDataStream都是面向数据流的，都可以和QIODevice搭配使用  
QDataStream比QTextStream更强大，可以说TextStream能做的事情QDataStream都能做  
QTextStream和QDataStream二者的侧重点不同：  
1. QTextStream侧重于进行文本读写
这里所说的文本指的是普通的简单的QChar、QString、QLatin1Char、int等等  
和C语言中写文件或者网络传输的时候，先将内容填充到一个buffer，然后进行操作有点类似  
2. QDataStream侧重于数据格式和类型
在Linux C开发中，通过socket传输text文本数据比较容易  
但如果想通过socket传输特定的数据节结构而且跨平台以及CUP进行操作和解析就比较麻烦  
对于不同的平台以及不同的内存分配方式的CPU来说，解析的结果可能会有问题  
使用QDataSream就可以解决该问题，对特定格式的类型数据进行完美的输入与输出  


## 关于QDataStream版本的说明
QDataStream的二进制数据格式从Qt 1.0开始，就随着Qt版本的更新而不断进化  
当读写数据流时，必须确保读操作和写操作使用了相同版本的QDataStream  
1. 如果要使用当前版本的Qt对应的数据格式，则不需要设置版本  
2. 如果需要读取早期版本的Qt程序写入的数据，或者写下的数据会被早期版本的Qt程序读取  
则需要使用setVersion()方法来设置版本  
```
stream.setVersion(QDataStream::Qt_4_0);
```
3. 如果是自定义的二进制数据格式，推荐采用下面的操作  
在数据头部中写入一个魔法字符串和版本号，可以给将来的扩展预留空间  
写入文件时：  
```
QFile file("file.xxx");
file.open(QIODevice::WriteOnly);
QDataStream out(&file);

// Write a header with a "magic number" and a version
out << (quint32)0xA0B0C0D0;
out << (qint32)123;

out.setVersion(QDataStream::Qt_4_0);

// Write the data
out << lots_of_interesting_data;
```
读取文件时：  
```
QFile file("file.xxx");
file.open(QIODevice::ReadOnly);
QDataStream in(&file);

// Read and check the header
quint32 magic;
in >> magic;
if (magic != 0xA0B0C0D0)
    return XXX_BAD_FILE_FORMAT;

// Read the version
qint32 version;
in >> version;
if (version < 100)
    return XXX_BAD_FILE_TOO_OLD;
if (version > 123)
    return XXX_BAD_FILE_TOO_NEW;

if (version <= 110)
    in.setVersion(QDataStream::Qt_3_2);
else
    in.setVersion(QDataStream::Qt_4_0);

// Read the data
in >> lots_of_interesting_data;
if (version >= 120)
    in >> data_new_in_XXX_version_1_2;
in >> other_interesting_data;
```


## 关于QDataStream中读写函数的说明
1. writeBytes()和readBytes()是一组，writeRawData()和readRawData()是一组
读写函数需要对应，用什么函数写入的数据，就要用对应的函数读取出来，否则会出错  

2. 同样一组数据，使用writeRawData()方法和writeBytes()方法写入的内容不同
使用writeRawData()方法写入的数据：  
```
7a68 616e 6700 0000 00a0 0b6d 0a00 0000
b81e 85eb 5138 5640
```
使用writeBytes()方法写入的数据：  
```
0000 0018 7a68 616e 6700 0000 00a0 a935
0a00 0000 b81e 85eb 5138 5640
```
可以看出，writeBytes()方法会在数据之前添加一个'0000 0018'，这个是Qt特有的标识，用于Qt自身的验证  
用writeBytes()方法写出来的文件不能通用，如果用C语言中fread()方法去读该文件可能就有问题  
如果需要写入最原始的内存数据，推荐使用writeRawData()方法，更加通用  


## 代码示例
详见QT_file.md  


## QDataStream支持的所有运算符
备注：只有这些基本数据类型可以使用运算符  
```
QDataStream &operator<<(qint8 i)
QDataStream &operator<<(quint8 i)
QDataStream &operator<<(qint16 i)
QDataStream &operator<<(quint16 i)
QDataStream &operator<<(qint32 i)
QDataStream &operator<<(quint32 i)
QDataStream &operator<<(qint64 i)
QDataStream &operator<<(quint64 i)
QDataStream &operator<<(std::nullptr_t ptr)
QDataStream &operator<<(bool i)
QDataStream &operator<<(qfloat16 f)
QDataStream &operator<<(float f)
QDataStream &operator<<(double f)
QDataStream &operator<<(const char *s)
QDataStream &operator>>(qint8 &i)
QDataStream &operator>>(quint8 &i)
QDataStream &operator>>(qint16 &i)
QDataStream &operator>>(quint16 &i)
QDataStream &operator>>(qint32 &i)
QDataStream &operator>>(quint32 &i)
QDataStream &operator>>(qint64 &i)
QDataStream &operator>>(quint64 &i)
QDataStream &operator>>(std::nullptr_t &ptr)
QDataStream &operator>>(bool &i)
QDataStream &operator>>(qfloat16 &f)
QDataStream &operator>>(float &f)
QDataStream &operator>>(double &f)
QDataStream &operator>>(char *&s)
```


## 构造函数
1. QDataStream::QDataStream(const QByteArray &a)

2. QDataStream::QDataStream(QByteArray \*a, QIODevice::OpenMode mode)

3. QDataStream::QDataStream(QIODevice \*d)
```
QFile file("D:/test.data");
QDataStream datastream(&file);
```

4. QDataStream::QDataStream()


## 常用公共函数：将QDataStream与QIODevice绑定
1. QIODevice \*QDataStream::device() const

2. void QDataStream::setDevice(QIODevice \*d)


## 常用公共函数：读写数据
1. QDataStream &QDataStream::readBytes(char \*&s, uint &l)
从数据流中读取数据到缓冲区s中，l为缓冲区的长度  
如果读取到的字符串为空，则s会被设置为nullptr，l会被设置为0  
备注：缓冲区s分配使用new[]，销毁使用delete[]，长度l需要是quint32格式的  
```
struct Student student1;
uint length = sizeof(Student);//数据类型必须是uint
char *temp1 = new char[length];//使用前申请内存空间
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadOnly))
{
    datastream.readBytes(temp1, length);
    memcpy(&student1, temp1, length);
}
file.close();
delete[] temp1;//使用后必须删除，防止内存泄漏
```

2. int QDataStream::readRawData(char \*s, int len)
从数据流中去读最多len个字节的数据到缓冲区s中，返回实际读取的字节数量  
如果读取过程中发生错误，返回-1  
备注：缓冲区s必须提前预分配好  

3. QDataStream &QDataStream::writeBytes(const char \*s, uint len)
把缓冲区s中len长度的数据写入到数据流中  
备注：长度len需要是quint32格式的  

4. int QDataStream::writeRawData(const char \*s, int len)
从缓冲区s中写len个字节的数据到数据流中，返回实际写入的字节数量  
如果写入过程中发生错误，返回-1  

5. int QDataStream::skipRawData(int len)

6. bool QDataStream::atEnd() const
如果已经读到数据流的末尾，或者没有设置任何QIODevice，则返回true，否则返回false  


## 常用公共函数：QDataStream的版本
1. int QDataStream::version() const

2. void QDataStream::setVersion(int v)
设置QDataStream的版本，不同的版本对应着不同的数据序列化格式  
v的取值参见enum QDataStream::Version  

3. void QDataStream::setFloatingPointPrecision(QDataStream::FloatingPointPrecision precision)
对应不同的QDataStream版本，可能需要设置浮点数是单精度还是双精度  

4. QDataStream::FloatingPointPrecision QDataStream::floatingPointPrecision() const


## 常用公共函数：数据流状态
1. QDataStream::Status QDataStream::status() const

2. void QDataStream::setStatus(QDataStream::Status status)
设置数据流的状态  
设置了之后，随后再调用setStatus()都会被忽略，直到调用resetStatus()  

3. void QDataStream::resetStatus()
重置数据流的状态  


## 常用公共函数：读写事务处理
备注：以下函数都是从Qt 5.7版本中引入，这些函数的作用没有完全搞明白  
1. void QDataStream::startTransaction()

2. void QDataStream::abortTransaction()

3. bool QDataStream::commitTransaction()

4. void QDataStream::rollbackTransaction()


## 常用公共函数：大端模式/小端模式
1. QDataStream::ByteOrder QDataStream::byteOrder() const

2. void QDataStream::setByteOrder(QDataStream::ByteOrder bo)
这里有个问题，Qt文档中说默认设置是大端模式，而且一般不建议修改模式  
但记得除了西门子使用大端模式之外，常见的操作系统都是采用小端模式  


## enum QDataStream::ByteOrder
这个集合包含了数据的字节序  
```
Constant 						Value 					Description
QDataStream::BigEndian			QSysInfo::BigEndian		大端模式
QDataStream::LittleEndian		QSysInfo::LittleEndian	小端模式
```


## enum QDataStream::Status
这个集合包含了当前数据流的状态  
```
Constant 						Value 	Description
QDataStream::Ok 				0 		数据流正在正常操作
QDataStream::ReadPastEnd 		1 		数据流已读取到底层设备中数据的末尾
QDataStream::ReadCorruptData 	2 		数据流读取到了损坏的数据
QDataStream::WriteFailed 		3 		数据流不能向底层设备中写数据了
```


## enum QDataStream::Version
这个集合包含了QDataStream的版本  
```
Constant 					Value 		Description
QDataStream::Qt_1_0 		1 			Version 1 (Qt 1.x)
QDataStream::Qt_2_0 		2 			Version 2 (Qt 2.0)
QDataStream::Qt_2_1 		3 			Version 3 (Qt 2.1, 2.2, 2.3)
QDataStream::Qt_3_0 		4 			Version 4 (Qt 3.0)
QDataStream::Qt_3_1 		5 			Version 5 (Qt 3.1, 3.2)
QDataStream::Qt_3_3 		6 			Version 6 (Qt 3.3)
QDataStream::Qt_4_0 		7 			Version 7 (Qt 4.0, Qt 4.1)
QDataStream::Qt_4_1 		Qt_4_0 		Version 7 (Qt 4.0, Qt 4.1)
QDataStream::Qt_4_2 		8 			Version 8 (Qt 4.2)
QDataStream::Qt_4_3 		9 			Version 9 (Qt 4.3)
QDataStream::Qt_4_4 		10 			Version 10 (Qt 4.4)
QDataStream::Qt_4_5 		11 			Version 11 (Qt 4.5)
QDataStream::Qt_4_6 		12 			Version 12 (Qt 4.6, Qt 4.7, Qt 4.8)
QDataStream::Qt_4_7 		Qt_4_6 		Same as Qt_4_6.
QDataStream::Qt_4_8 		Qt_4_7 		Same as Qt_4_6.
QDataStream::Qt_4_9 		Qt_4_8 		Same as Qt_4_6.
QDataStream::Qt_5_0 		13 			Version 13 (Qt 5.0)
QDataStream::Qt_5_1 		14 			Version 14 (Qt 5.1)
QDataStream::Qt_5_2 		15 			Version 15 (Qt 5.2)
QDataStream::Qt_5_3 		Qt_5_2 		Same as Qt_5_2
QDataStream::Qt_5_4 		16 			Version 16 (Qt 5.4)
QDataStream::Qt_5_5 		Qt_5_4 		Same as Qt_5_4
QDataStream::Qt_5_6 		17 			Version 17 (Qt 5.6)
QDataStream::Qt_5_7 		Qt_5_6 		Same as Qt_5_6
QDataStream::Qt_5_8 		Qt_5_7 		Same as Qt_5_6
QDataStream::Qt_5_9 		Qt_5_8 		Same as Qt_5_6
QDataStream::Qt_5_10 		Qt_5_9		Same as Qt_5_6
QDataStream::Qt_5_11 		Qt_5_10		Same as Qt_5_6
QDataStream::Qt_5_12 		18			Version 18 (Qt 5.12)
QDataStream::Qt_5_13 		19			Version 19 (Qt 5.13)
QDataStream::Qt_5_14 		Qt_5_13		Same as Qt_5_13
QDataStream::Qt_5_15 		Qt_5_14		Same as Qt_5_13
```