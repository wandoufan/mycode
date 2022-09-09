# QIODevice

## 基本功能
QIODevice是Qt中所有I/O设备的公共基类，提供了读取和写入数据块的抽象接口  
父类：QObject  
子类：QAbstractSocket、QBuffer、QFileDevice、QLocalSocket、QNetworkReply、QProcess  


## 关于设备的分类
1. 序列化的顺序访问设备
这种设备只能从头开始，连续读取，读取过程中可以向前或向后跳转  
最常见的序列化设备就是网络套接字  

2. 支持随机访问的设备
与序列化设备相反，随机设备没有开始位置、结束位置、设备大小等概念
随机设备在读取过程中不支持顺序跳转，只能实现随机跳转  


## 代码示例
1.  readyRead()信号对应的槽函数
```
void MainWindow::onSocketReadyRead()
{
    //当缓冲区有新的数据可读时，读取数据
    while (tcp_socket -> canReadLine())
    {
        ui -> textBrowser -> append(tcp_socket -> readLine());
    }
}
```


## 构造函数
注意：QIODevice是一个抽象类，因此只能用作基类，不能被直接实例化使用  
1. QIODevice::QIODevice(QObject \*parent)

2. QIODevice::QIODevice()


## 常用公共函数：获取设备状态信息
1. bool QIODevice::isOpen() const
判断设备是否是打开状态  
备注：只有设备随时可以读写，设备才算处于打开状态，如果OpenMode是NotOpen，则返回false  

2. QIODevice::OpenMode QIODevice::openMode() const
返回该设备的打开模式  

3. bool QIODevice::isReadable() const
判断设备是否是可读的，即设备打开模式中包含了QIODevice::ReadOnly  

4. bool QIODevice::isWritable() const
判断设备是否是可写的，即设备打开模式中包含了QIODevice::WriteOnly  

5. bool QIODevice::isTextModeEnabled() const
判断设备是否是文本模式，即设备打开模式中包含了QIODevice::Text  

6. QString QIODevice::errorString() const
以字符串形式返回报错  

7. [virtual] bool QIODevice::isSequential() const
判断设备是否是序列化设备  

8. int QIODevice::readChannelCount() const
当设备处于打开状态时，返回可以读取的通道的数量，否则返回0  
备注：这个函数是在Qt 5.7版本引入  

9. int QIODevice::writeChannelCount() const
备注：这个函数是在Qt 5.7版本引入  

10. [virtual] qint64 QIODevice::size() const
对于处于打开状态的随机访问设备，返回设备的大小  
对于处于打开状态的顺序访问设备，返回bytesAvailable()的值  
对于没有打开的设备，返回值不能反映设备的实际大小  


## 常用公共函数：设备中可以读写的数据
1. [virtual] bool QIODevice::canReadLine() const
如果设备上有一行完整的数据可以读取，则返回true，否则返回false  
这个函数经常在readyRead()信号函数的关联槽函数中进行使用  
注意：对于没有缓冲区的设备，没有办法探测是否有数据可以读取，永远返回false  

2. [virtual] qint64 QIODevice::bytesAvailable() const
返回设备中可读数据的字节数  
这个函数通常用来在读取数据之前获取数据的数量，从而分配缓冲区的空间  
注意：子类在对该函数进行重定义时，需要加上QIODevice的缓冲区大小  
```
qint64 CustomDevice::bytesAvailable() const
{
	return buffer.size() + QIODevice::bytesAvailable();
}
```

3. [virtual] qint64 QIODevice::bytesToWrite() const
对于带有缓冲区的设备，返回要往缓冲区中写入的数据的字节数  
对于没有缓冲区的设备，返回0  

4. [virtual] bool QIODevice::atEnd() const
判断当前读写位置是否到达文件末尾(例如，文件中没有任何可读数据)  

5. int QIODevice::currentReadChannel() const
返回当前正在读取的通道的索引号  
备注：这个函数是在Qt 5.7版本引入  

6. int QIODevice::currentWriteChannel() const
返回当前正在写入的通道的索引号  
备注：这个函数是在Qt 5.7版本引入  

7. void QIODevice::setCurrentReadChannel(int channel)
备注：这个函数是在Qt 5.7版本引入  

8. void QIODevice::setCurrentWriteChannel(int channel)
备注：这个函数是在Qt 5.7版本引入  

9. [virtual] bool QIODevice::waitForBytesWritten(int msecs)
阻塞程序，等待msecs毫秒，直到缓冲区中的待写入数据被写入设备中，然后发出bytesWritten()信号  
如果数据被成功写入设备中，返回true，如果时间超时或发生错误，返回false  
msecs参数设为-1，则时间永远不会超时  
备注：对于Unbuffered的设备，函数会立刻返回  
备注：这个函数在write()后多了一个等待的过程，但除非发送的数据量特别大，一般没有必要  
备注：如果是循环发送数据时可以调用这个函数，系统可能在循环结束后一次性发数据发过去，而不是循环一次发送一次  
备注：是否调用这个函数和是否发出bytesWritten()信号没有关系，即使不调用，在write()之后也会发出信号  

10. [virtual] bool QIODevice::waitForReadyRead(int msecs)
阻塞程序，等待msecs毫秒，直到设备中有新的数据可读，然后发出readyRead()信号  
如果设备中有数据可读，返回true，如果时间超时或发生错误，返回false  
msecs参数设为-1，则时间永远不会超时  


## 常用公共函数：打开/关闭设备
1. [virtual] bool QIODevice::open(QIODevice::OpenMode mode)
以指定的OpenMode打开一个设备，返回是否打开成功  
备注：在WriteOnly和ReadWrite模式下，如果文件不存在，会在打开前自动创建该文件  
注意：实际测试，open()方法只能调用一次  
也就是对于一个已经处于打开状态的QIODevice对象，再次调用open()方法会返回打开失败  

2. [virtual] void QIODevice::close()
首先发出aboutToClose()信号，然后关闭设备，并把设备的OpenMode设置为NotOpen  


## 常用公共函数：读取数据
1. bool QIODevice::getChar(char \*c)
从设备中读取一个字符，并将其存在c参数中  
如果c是一个空指针，字符会被丢弃  

2. qint64 QIODevice::read(char \*data, qint64 maxSize)
从设备中读取至多maxSize个字节的数据，并存入data中，返回读到的字节数  
如果读取过程中发生错误，则返回-1  
如果设备中没有数据可读，则返回0  

3. QByteArray QIODevice::read(qint64 maxSize)
重载函数  
从设备中读取至多maxSize个字节的数据，然后将数据以QByteArray的形式返回  

4. qint64 QIODevice::readLine(char \*data, qint64 maxSize)
从设备中读取一行ASCII码数据，而且读取至多(maxSize - 1)个字节的数据，并存入data中，返回读到的字节数  
如果这行数据不能被读取，并且没有错误发生，函数返回0  
如果发生了错误，函数返回可以读到的数据长度，如果什么都没读到，则函数返回-1  
备注：数据后面总会被加上一个终止符'\0'，所以maxSize一定比1大  

5. QByteArray QIODevice::readLine(qint64 maxSize = 0)
重载函数  
从设备中读取一行ASCII码数据，而且读取至多(maxSize - 1)个字节的数据，然后将数据以QByteArray的形式返回  

6. QByteArray QIODevice::readAll()
从设备中读取剩余的所有数据，然后将数据以QByteArray的形式返回  
这个函数不会产生报错，当返回一个空的QByteArray时，可能是设备中没有数据可读，也可能是发生了错误  

7. qint64 QIODevice::peek(char \*data, qint64 maxSize)
从设备中读取最多maxSize个字节的数据到data中，返回实际读取的字节数，没有副作用  
如果读取过程中发生错误，则返回-1  
如果设备中没有数据可读，则返回0  
例如，在调用peek()方法后，再调用read()方法，两次读到的数据是相同的  
备注：我理解，peek()方法没有副作用的意思是应该是读取数据之后，指针的位置不变  

8. QByteArray QIODevice::peek(qint64 maxSize)
重载函数  
从设备中读取至多maxSize个字节的数据，然后将数据以QByteArray的形式返回  


## 常用公共函数：写入数据
1. bool QIODevice::putChar(char c)
向设备中写入字符c，返回是否写入成功  

2. qint64 QIODevice::write(const char \*data, qint64 maxSize)
从data向设备中写入至多maxSize个字节的数据，返回实际写入的数据字节个数，如果发生错误则返回-1  

3. qint64 QIODevice::write(const char \*data)
重载函数  
把一个连续的8位字符组成的字符串写入设备中，返回实际写入的数据字节个数，如果发生错误则返回-1  
函数等价于"QIODevice::write(data, qstrlen(data));"  

4. qint64 QIODevice::write(const QByteArray &byteArray)
重载函数  
把QByteArray类型的数据写入设备中，返回实际写入的数据字节个数，如果发生错误则返回-1  


## 常用公共函数：在读写过程中的指针位置
1. [virtual] qint64 QIODevice::pos() const
对于随机访问设备，返回数据正在读写的位置  
对于顺序访问设备或处于关闭状态的设备，没有当前位置的概念，返回0  
备注：设备当前的读写位置是由QIODevice来维护的，因此在子类中对该方法进行重定义是没有必要的  

2. [virtual] bool QIODevice::reset()
对于随机访问设备，把指针重置到开始输入的位置，返回是否成功  

3. [virtual] bool QIODevice::seek(qint64 pos)
对于随机访问设备，把当前的读写位置设置为pos，返回是否成功  
对于顺序访问设备，则会产生一个警告信息，然后返回false  
在QIODevice的子类中进行重定义时，必须在重定义函数开头就先调用QIODevice::seek()，来保证QIODevice内置缓冲区的完整性  

4. qint64 QIODevice::skip(qint64 maxSize)
在设备中跳过maxSize个字节的数据，返回实际跳过的字节的数量  
如果发生错误，则返回-1  
如果设备是以文本模式(QIODevice::Text)打开的，行尾的截断符会被翻译为'\n'，算作一个字节  
skip()方法对于所有设备都通用，即使是不支持的seek()方法的顺序访问设备，也可以用来跳过不想要的数据  
备注：maxSize参数不能是负数  
备注：这个函数是在Qt 5.10版本引入  


## 信号函数
1. [signal] void QIODevice::readyRead()
每次缓冲区中有新的数据可以读取时都会发出该信号，在此信号对应的槽函数中去读取缓冲区的数据  

2. [signal] void QIODevice::aboutToClose()
当设备即将关闭(调用了close()函数)时发出该信号  
该信号对应的槽函数中一般执行一些关闭设备前必须要完成的操作  

3. [signal] void QIODevice::bytesWritten(qint64 bytes)
每次缓冲区中的待写入数据被写入到设备时，都会发出该信号  
bytes参数代表每次写入数据的字节数  
注意：这个信号不是递归的，在连续写入数据时也不会被重复发射信号  


## enum QIODevice::OpenMode
这个集合中的元素用来描述open()函数打开时的模式，也可以用openMode()函数进行查询  
```
Constant                    Value                   Description
QIODevice::NotOpen          0x0000                  设备没有打开
QIODevice::ReadOnly         0x0001                  只读模式打开
QIODevice::WriteOnly        0x0002                  只写模式打开，注意：对于文件系统的子类(如QFile)，使用这个模式意味着截断
QIODevice::ReadWrite        ReadOnly | WriteOnly    读写模式打开
QIODevice::Append           0x0004                  追加模式打开
QIODevice::Truncate         0x0008                  如果可能，设备在打开之前会被截断，设备中所有的早期内容都会丢失
QIODevice::Text             0x0010                  文本模式打开，当读入时行尾会被转换为'\n'，当写入时行尾会被转换为本地编码，如'\r\n'
QIODevice::Unbuffered       0x0020                  设备中的任何缓冲区都会被绕过
QIODevice::NewOnly          0x0040                  如果要打开的文件已经存在，则会失败
QIODevice::ExistingOnly     0x0080                  如果要打开的文件不存在，则会失败
```
注意：可以同时有多个模式存在(模式之间不能互相冲突)  
```
file.open(QIODevice::WriteOnly | QIODevice::Truncate);
file.open(QIODevice::ReadOnly | QIODevice::Text);
```
注意：如果读取的是二进制文件，不要使用QIODevice::Text模式  
实测发现，用Text打开文件会造成读取的数据中有少量的数字解析不准确，效果如下  
```
channel[1] : -1.57894e+141
channel[2] : -1.57431e+141
channel[3] : -4.02715e+143
```