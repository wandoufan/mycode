# QIODevice

## 基本功能
QIODevice是Qt中所有I/O设备的公共基类  
QIODevice提供了读取和写入数据块的抽象接口，常用子类包括QFile、QBuffer、QTcpSocket  
注意：QIODevice是一个抽象类，因此只能用作基类，不能被直接实例化使用  


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


## 常用公共函数

[virtual] bool QIODevice::canReadLine() const
如果设备上有一行完整的数据可以读取，则返回true，否则返回false  
这个函数经常在readyRead()信号函数的关联槽函数中进行使用  
注意：对于没有缓冲区的设备，没有办法探测是否有数据可以读取，永远返回false  


qint64 QIODevice::read(char \*data, qint64 maxSize)


QByteArray QIODevice::read(qint64 maxSize)
这是一个重载函数  

qint64 QIODevice::readLine(char \*data, qint64 maxSize)

QByteArray QIODevice::readLine(qint64 maxSize = 0)
这是一个重载函数  

QByteArray QIODevice::readAll()


qint64 QIODevice::write(const char \*data, qint64 maxSize)

qint64 QIODevice::write(const char \*data)
这是一个重载函数  

qint64 QIODevice::write(const QByteArray &byteArray)
这是一个重载函数  



## 公共静态函数
1. [signal] void QIODevice::readyRead()
每次缓冲区中有新的数据可以读取时都会发出该信号，在此信号对应的槽函数中去读取缓冲区的数据  


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