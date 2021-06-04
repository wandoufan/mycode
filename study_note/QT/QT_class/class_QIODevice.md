# QIODevice

## 基本功能
QIODevice是Qt中所有I/O设备的公共基类，提供了读取和写入数据块的抽象接口  
父类：QObject  
子类：QAbstractSocket、QBuffer、QFileDevice、QLocalSocket、QNetworkReply、QProcess  


## 代码示例
1. readyRead()信号对应的槽函数
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


## 常用公共函数
1. [virtual] bool QIODevice::canReadLine() const
如果设备上有一行完整的数据可以读取，则返回true，否则返回false  
这个函数经常在readyRead()信号函数的关联槽函数中进行使用  
注意：对于没有缓冲区的设备，没有办法探测是否有数据可以读取，永远返回false  

2. bool QIODevice::isOpen() const
判断设备是否是打开状态  
备注：只有设备随时可以读写，设备才算处于打开状态，如果OpenMode是NotOpen，则返回false  

3. bool QIODevice::isReadable() const
判断设备是否是可读状态  

4. [virtual] qint64 QIODevice::bytesAvailable() const
返回设备中可读数据的字节数

5. QString QIODevice::errorString() const
以字符串形式返回报错  

6. [virtual] bool QIODevice::open(QIODevice::OpenMode mode)
以指定的OpenMode打开一个设备，返回是否打开成功  
备注：在WriteOnly和ReadWrite模式下，如果文件不存在，会在打开前自动创建该文件  

7. QIODevice::OpenMode QIODevice::openMode() const
返回该设备的打开模式  

8. [virtual] void QIODevice::close()
首先发出aboutToClose()信号，然后关闭设备，并把设备的OpenMode设置为NotOpen  

9. bool QIODevice::getChar(char \*c)
从设备中读取一个字符，并将其存在c参数中  
如果c是一个空指针，字符会被丢弃  

10. qint64 QIODevice::read(char \*data, qint64 maxSize)
从设备中读取至多maxSize个字节的数据，并存入data中，返回读到的字节数  
如果读取过程中发生错误，则返回-1  
如果设备中没有数据可读，则返回0  

11. QByteArray QIODevice::read(qint64 maxSize)
这是一个重载函数，从设备中读取至多maxSize个字节的数据，然后将数据以QByteArray的形式返回  

12. qint64 QIODevice::readLine(char \*data, qint64 maxSize)
从设备中读取一行ASCII码数据，而且读取至多(maxSize - 1)个字节的数据，并存入data中，返回读到的字节数  
如果这行数据不能被读取，并且没有错误发生，函数返回0  
如果发生了错误，函数返回可以读到的数据长度，如果什么都没读到，则函数返回-1  
备注：数据后面总会被加上一个终止符'\0'，所以maxSize一定比1大  

13. QByteArray QIODevice::readLine(qint64 maxSize = 0)
这是一个重载函数，从设备中读取一行ASCII码数据，而且读取至多(maxSize - 1)个字节的数据，然后将数据以QByteArray的形式返回    

14. QByteArray QIODevice::readAll()
从设备中读取剩余的所有数据，然后将数据以QByteArray的形式返回  
这个函数不会产生报错，当返回一个空的QByteArray时，可能是设备中没有数据可读，也可能是发生了错误  

15. qint64 QIODevice::write(const char \*data, qint64 maxSize)
从data向设备中写入至多maxSize个字节的数据，返回实际写入的数据字节个数，如果发生错误则返回-1  

16. qint64 QIODevice::write(const char \*data)
这是一个重载函数，把一个连续的8位字符组成的字符串写入设备中，返回实际写入的数据字节个数，如果发生错误则返回-1  
函数等价于"QIODevice::write(data, qstrlen(data));"  

17. qint64 QIODevice::write(const QByteArray &byteArray)
这是一个重载函数，把QByteArray类型的数据写入设备中，返回实际写入的数据字节个数，如果发生错误则返回-1  

18. [virtual] bool QIODevice::waitForBytesWritten(int msecs)
阻塞程序，等待msecs毫秒，直到缓冲区中的待写入数据被写入设备中，然后发出bytesWritten()信号  
如果数据被成功写入设备中，返回true，如果时间超时或发生错误，返回false  
msecs参数设为-1，则时间永远不会超时  
备注：对于Unbuffered的设备，函数会立刻返回  

19. [virtual] bool QIODevice::waitForReadyRead(int msecs)
阻塞程序，等待msecs毫秒，直到设备中有新的数据可读，然后发出readyRead()信号  
如果设备中有数据可读，返回true，如果时间超时或发生错误，返回false  
msecs参数设为-1，则时间永远不会超时  


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
Constant   Value   Description
QIODevice::NotOpen   0x0000   设备没有打开
QIODevice::ReadOnly   0x0001   只读模式打开
QIODevice::WriteOnly   0x0002   只写模式打开，注意：对于文件系统的子类(如QFile)，使用这个模式意味着截断
QIODevice::ReadWrite   ReadOnly | WriteOnly   读写模式打开
QIODevice::Append   0x0004   追加模式打开
QIODevice::Truncate   0x0008   如果可能，设备在打开之前会被截断，设备中所有的早期内容都会丢失
QIODevice::Text   0x0010   文本模式打开，当读入时行尾会被转换为'\n'，当写入时行尾会被转换为本地编码，如'\r\n'
QIODevice::Unbuffered   0x0020   设备中的任何缓冲区都会被绕过
QIODevice::NewOnly   0x0040   如果要打开的文件已经存在，则会失败
QIODevice::ExistingOnly   0x0080   如果要打开的文件不存在，则会失败
```
注意：可以同时有多个模式存在(模式之间不能互相冲突)  
```
file.open(QIODevice::WriteOnly | QIODevice::Truncate);
file.open(QIODevice::ReadOnly | QIODevice::Text);
```