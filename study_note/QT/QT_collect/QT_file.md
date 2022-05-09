# Qt中的文件系统

## 继承关系
```
                                              |- QSctpSocket
QIODevice -|- QAbstractSocket -|- QTcpSocket -|- QSslSocket
                               |- QUdpSocket

           |- QFileDevice -|- QFile -|- QTemporaryFile
                           |- QSaveFile
```


## QIODevice及其子类
QIODevice
所有 I/O 设备类的父类，提供了字节块读写的通用操作以及基本接口

QFileDevice
Qt5新增加的类，提供了有关文件操作的通用实现

QFlie
访问本地文件或者嵌入资源

QTemporaryFile
创建和访问本地文件系统的临时文件

QBuffer
读写QbyteArray, 内存文件

QProcess
运行外部程序，处理进程间通讯

QAbstractSocket
所有套接字类的父类

QTcpSocket
TCP协议网络数据传输

QUdpSocket
传输 UDP 报文

QSslSocket
使用 SSL/TLS 传输数据


## 与文件系统相关的其他类(不是QIODevice的子类)
QFileInfo
获取文件的详细信息

QDir
实现文件目录相关的功能



## 读写文件代码示例
1. 使用QFile读写文本文件
如果写入的是文本数据，则文件可以直接用各种文本编辑器打开查看内容
```
//写入一行文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    file.write("this is a QIODevice test");
}
file.close();

//写入多行文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    file.write("this is line 1\n");
    file.write("this is line 2\n");
    file.write("this is line 3\n");
    file.write("this is line 4\n");
    file.write("this is line 5\n");
}
file.close();

//读出所有文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    QByteArray array = file.readAll();
    QString content = QString::fromLatin1(array);
}
file.close();

//逐行读出文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    while(!file.atEnd())
    {
        QByteArray array = file.readLine();
        QString content = QString::fromLatin1(array);
        qDebug() << content;
    }
}
file.close();
```

2. 单独使用QFile读写二进制文件
备注：这种方式也能实现，但非常麻烦，不推荐
```
//写入二进制文件
qint32 nums[5] = {1,2,3,4,5};
//写入文件之前，要将数据以二进制方式存储到字节数组中
QByteArray array;
array.resize(sizeof(nums));
for(int i=0;i<5;i++)
{
    //借助指针，将每个整数拷贝到字节数组中
    memcpy(array.data()+i*sizeof(qint32),&(nums[i]),sizeof(qint32));
}
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite))
{
    file.write(array);
}
file.close();
```

3. 使用QTextStream/QDataStream + QFile读写二进制文件


4. 读取用C语言写入的二进制文件？
--> 齿轮箱配置文件：里面包含整型数组和字符数组
--> 是否还需要用到QDataStream
--> Qt中好像无法直接调用C语言中读写文件的fopen()函数
备注：实际测试，在Qt中也可以使用C语言中读写文件的函数，但会提醒函数已过时
用C语言写入二进制文件的代码
```

```
用C语言读取二进制文件的代码
```

```


---------------------------
1. 创建文件和文件夹
2. 读取文件
```
QFile file("in.txt");
if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
	return;

while (!file.atEnd())
{
	QByteArray line = file.readLine();
	process_line(line);
}
```


3. readyRead()信号对应的槽函数
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
