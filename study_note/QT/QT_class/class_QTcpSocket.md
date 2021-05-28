# QTcpSocket

## 基本功能
QTcpSocket提供TCP套接字相关的功能，在建立TCP连接之后进行数据流的传输，和QTcpServer配套使用  
```
TCP客户端包括：QTcpSocket
TCP服务端包括：QTcpSocket、QTcpServer
```
注意：TCP套接字不能以'QIODevice::Unbuffered'模式打开  
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  
备注：QTcpSocket中基本没有成员函数，所有的函数都来自于继承QAbstractSocket  


## 继承关系
```
                                            | - QSctpSocket
QIODevice - QAbstractSocket - |-QTcpSocket -| - QSslSocket
                              |-QUdpSocket
```


## 工作过程
1. 客户端的QTcpSocket对象通过connectToHost()函数尝试连接到指定的服务端
2. connectToHost()函数是异步方式去连接服务器，不会阻塞程序运行  
如果想用阻塞方式连接服务器，则使用waitForConnected()函数阻塞程序运行，直到连接成功或失败  
3. 当与服务端建立socket连接后，就可以向缓冲区中写入数据或读取数据  
当缓冲区有新数据时，会发射readyRead()信号，在此信号对应的槽函数中去读取缓冲区的数据  


## 两个套接字之间的数据通信
QTcpSocket是从QIODevice间接继承的，因此可以实现流数据读写功能  
一个QTcpSocket对象既可以接收数据，也可以发送数据，而且接收与发送是异步工作的，有各自的缓冲区  
客户端和服务端的socket之间进行通信时，需要提前规定二者之间的通信协议，即传输的数据如何解析  
socket之间的通信协议一般有两种：  
1. 基于行的通信协议
一般用于纯文本数据的通信，每一行数据以一个换行符结束  
现有canReadLine()函数判断是否有新的一行数据需要读取，再用readLine()函数读取一行数据  
```
void MainWindow::onSocketReadyRead()
{
    //当缓冲区有新的数据可读时，读取数据
    while (tcp_socket -> canReadLine())
    {
        ui -> textBrowser -> append(tcp_socket -> readLine());
    }
}

void MainWindow::on_button_send_message_clicked()
{
    //发送一行消息，以换行符'\n'结束
    if(tcp_socket -> isValid())
    {
        QString message = ui -> message -> text();
        ui -> textBrowser -> append("[out] " + message);
        ui -> message -> clear();
        QByteArray string = message.toUtf8();
        string.append('\n');
        tcp_socket -> write(string);
    }
    else
    {
        ui -> textBrowser -> append("**套接字不合法，无法发送..");
    }
}
```
2. 基于数据块的通信协议
一般用于二进制数据的传输，可以使用数据流的方式来传输图片等任意格式的文件，但是需要自定义具体的格式  


## 构造函数
1. QTcpSocket::QTcpSocket(QObject \*parent = nullptr)
创建一个套接字对象，默认处于UnconnectedState的状态  