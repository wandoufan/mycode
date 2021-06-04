# QAbstractSocket

## 基本功能
QAbstractSocket是QTcpSever和QUdpSocket的基类，提供了所有套接字的公共基础函数  
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  
如果需要创建套接字，一般有两个选择：  
1. 实例化QTcpSever或QUdpSocket
2. 创建一个本地的套接字描述，然后将QAbstractSocket实例化，再调用setSocketDescriptor()函数将本地套接字包起来


## 关于UDP建立连接的说明
QAbstractSocket的API统一了这两个协议之间的大部分区别  
例如，尽管UDP是无连接的协议，connectToHost()函数也会为UDP套接字建立起一个虚拟的连接  
因此使用QAbstractSocket可以或多或少的忽视底层协议的区别  


## 继承关系
```
                                            | - QSctpSocket
QIODevice - QAbstractSocket - |-QTcpSocket -| - QSslSocket
                              |-QUdpSocket
```


## 常用公共函数
1. [virtual] void QAbstractSocket::connectToHost(const QString &hostName, quint16 port, QIODevice::OpenMode openMode = ReadWrite, QAbstractSocket::NetworkLayerProtocol protocol = AnyIPProtocol)
尝试在某个主机上与给定的端口建立起一个连接，具体过程为：套接字以给定的模式打开，进入HostLookupState状态，根据主机名去查找对应的主机，如果查找成功，就发出hostFound()信号，然后套接字进入ConnectingState状态，然后去尝试连接查找返回的地址，最后如果成功建立起连接，套接字进入ConnectedState状态，然后发出connected()信号；如果在其中任何节点发生错误，套接字都会发出errorOccurred()信号  
注意：在进行读写操作之前，套接字必须已经进入ConnectedState状态  
备注：connectToHost()是用异步方式去连接服务端，即不会阻塞程序的运行  
hostName参数用来设置要连接的主机名，可以是IP地址，也可以是主机名称  
port参数用来设置要连接的端口号  
openMode参数用来设置打开模式，默认为读写模式  
protocol参数用来区分使用的是哪个网络协议，默认为IPV4和IPV6  

2. [virtual] void QAbstractSocket::connectToHost(const QHostAddress &address, quint16 port, QIODevice::OpenMode openMode = ReadWrite)
重载函数，可以根据一个QHostAddress类型的参数去查找主机  

3. [virtual] void QAbstractSocket::disconnectFromHost()
断开连接，关闭套接字  
如果还有数据等待写入，套接字会进入ClosingState状态，并等待数据都写完  
最终，套接字会进入UnconnectedState状态，并发出disconnected()信号  

4. bool QAbstractSocket::isValid() const
如果套接字是合法的，并且已经准备好了进行读写，则返回true，否则返回false  

5. QAbstractSocket::SocketState QAbstractSocket::state() const
返回套接字当前的状态  

6. QAbstractSocket::SocketError QAbstractSocket::error() const
返回最近一次发生错误的类型  

7. QHostAddress QAbstractSocket::localAddress() const
如果本地套接字可用，则返回本地主机地址，否则返回QHostAddress::Null  

8. quint16 QAbstractSocket::localPort() const
如果本地套接字可用，则返回本地端口号，否则返回0  

9. QHostAddress QAbstractSocket::peerAddress() const
如果套接字处于ConnectedState状态，则返回对方套接字的主机地址，否则返回QHostAddress::Null  

10. quint16 QAbstractSocket::peerPort() const
如果套接字处于ConnectedState状态，则返回对方套接字的端口号，否则返回0  

11. QString QAbstractSocket::peerName() const
返回对方套接字的主机名称，主机名称为connectToHost()函数中的定义，如果没有调用connectToHost()函数，则返回空字符串  

12. qint64 QAbstractSocket::readBufferSize() const
返回内部读取缓冲区的大小，该大小决定了read()和readAll()函数能读出的数据的大小  
缓冲区大小默认为0，代表缓冲区没有尺寸限制，确保不会有数据丢失  

13. [virtual] void QAbstractSocket::setReadBufferSize(qint64 size)
设置内部读取缓冲区的大小  

14. QAbstractSocket::SocketType QAbstractSocket::socketType() const
返回套接字的类型(TCP、UDP或其他)  

15. [virtual] bool QAbstractSocket::waitForConnected(int msecs = 30000)
如果在指定的时间内建立起连接，则返回true，否则返回false  
如果参数设置为-1，则函数永远不会超时  

16. [virtual] bool QAbstractSocket::waitForDisconnected(int msecs = 30000)
如果在指定的时间内断开连接，则返回true，否则返回false  
时间超时、发生错误或套接字已经处于断开状态等情况都会返回false  
如果msecs参数设置为-1，则函数永远不会超时  

17. bool QAbstractSocket::bind(const QHostAddress &address, quint16 port = 0, QAbstractSocket::BindMode mode = DefaultForPlatform)
使用指定的绑定模式，将一个地址和端口绑定起来，一般常用于UDP套接字  
如果绑定成功，函数返回true，套接字进入BoundState状态，否则返回false  
对于UDP socket，在绑定之后，当UDP数据报到达特定的地址和端口之后，会发出readyRead()信号  
默认情况下，如果没有指定具体的端口，会随机选择一个端口  
注意：这里的端口是指发送方的端口，不是接收方的端口，接收方的端口在发送数据的函数中指定  
```
//对于UDP单播或多播
if(udp_socket -> bind(port))
//对于UDP组播
if(udp_socket -> bind(QHostAddress::AnyIPv4, group_port, QAbstractSocket::ShareAddress))
```

18. bool QAbstractSocket::bind(quint16 port = 0, QAbstractSocket::BindMode mode = DefaultForPlatform)
这是一个重载函数，绑定到任意地址的指定端口上，不需要写具体的地址参数  

19. void QAbstractSocket::abort()
终止当前的连接，并重置socket，相当于解绑端口  
和disconnectFromHost()不同的是，abort()函数会立刻关闭socket，丢掉缓冲区中还没读写完成的数据  

20. [virtual] void QAbstractSocket::setSocketOption(QAbstractSocket::SocketOption option, const QVariant &value)
将socket对象设置为给定的选项  
其中MulticastTtlOption是UDP组播数据报的生存周期，数据报每跨越一个路由就数值减1  
默认值为1，表示组播数据包只能在同一个路由下的局域网内传播  
```
//将socket的QAbstractSocket::MulticastTtlOption值设置为1
udp_socket -> setSocketOption(QAbstractSocket::MulticastTtlOption, 1);
```


## 重载实现公共函数
1. [override virtual] qint64 QAbstractSocket::bytesAvailable() const
返回要从缓冲区读取的数据的字节数  

2. [override virtual] bool QAbstractSocket::canReadLine() const
如果有一行数据可以从套接字中读取，就返回true，否则返回false  

3. [override virtual] bool QAbstractSocket::waitForReadyRead(int msecs = 30000)
是对QIODevice::waitForReadyRead(int msecs)函数进行重载  
这个函数会被一直阻塞，直到有新的数据可以读取以及readyRead()信号已经被发出，此时返回true，否则返回false  

4. [override virtual] bool QAbstractSocket::waitForBytesWritten(int msecs = 30000)
是对QIODevice::waitForBytesWritten(int msecs)函数进行重载  
这个函数会被一直阻塞，直到至少有一个字节的数据已经写入套接字中以及bytesWritten()信号已经被发出，此时返回true，否则返回false  


## 信号函数
1. [signal] void QAbstractSocket::connected()
在调用connectToHost()函数，并成功建立起一个连接之后就会发出信号  
备注：在某些操作系统上，在调用connectToHost()函数后会直接发出该信号  

2. [signal] void QAbstractSocket::disconnected()
当套接字关闭时发出该信号  
备注：如果想要在该信号函数关联的槽函数中删除发射信号的对象，应该使用deleteLater()函数  
```
void MainWindow::onClientDisconnected()
{
    //disconnected()信号关联的槽函数
    ui -> textBrowser -> append("**已经与客户端断开连接..");
    tcp_socket -> deleteLater();
}
```

3. [signal] void QAbstractSocket::errorOccurred(QAbstractSocket::SocketError socketError)
当错误发生时发出该信号，socketError参数为发生的错误类型  

4. [signal] void QAbstractSocket::hostFound()
在调用connectToHost()函数，并查找主机成功之后就会发出该信号  

5. [signal] void QAbstractSocket::proxyAuthenticationRequired(const QNetworkProxy &proxy, QAuthenticator \*authenticator)
当使用需要身份验证的代理时，可以发出此信号，然后可以用所需的详细信息填充authenticator对象，以允许身份验证并继续连接  

6. [signal] void QAbstractSocket::stateChanged(QAbstractSocket::SocketState socketState)
当套接字的状态改变时发出该信号，socketState参数为新的状态  


## enum QAbstractSocket::SocketState
这个集合包含了套接字的不同状态  
备注：这个集合是没有注册的元对象，使用时必须用Q_DECLARE_METATYPE()和qRegisterMetaType()去注册  
```
Constant   Value   Description
QAbstractSocket::UnconnectedState   0   套接字没有连接
QAbstractSocket::HostLookupState   1   套接字正在执行主机名查找
QAbstractSocket::ConnectingState   2   套接字正在建立一个连接
QAbstractSocket::ConnectedState   3   套接字已经建立一个连接
QAbstractSocket::BoundState   4   套接字被绑定到一个地址和端口上了
QAbstractSocket::ClosingState   6   套接字正在关闭连接(如果有未写完的数据，就等待写完后再关闭)
QAbstractSocket::ListeningState   5   套接字正在监听(只供内部使用)
```
stateChanged()信号对应的槽函数  
```
void MainWindow::onSocketStateChange(QAbstractSocket::SocketState socketState)
{
    //当套接字状态变化时，进行响应
    switch (socketState)
    {
    case QAbstractSocket::UnconnectedState:
        socket_status -> setText("socket状态：UnconnectedState");
        break;
    case QAbstractSocket::HostLookupState:
        socket_status -> setText("socket状态：HostLookupState");
        break;
    case QAbstractSocket::ConnectingState:
        socket_status -> setText("socket状态：ConnectingState");
        break;
    case QAbstractSocket::ConnectedState:
        socket_status -> setText("socket状态：ConnectedState");
        break;
    case QAbstractSocket::BoundState:
        socket_status -> setText("socket状态：BoundState");
        break;
    case QAbstractSocket::ClosingState:
        socket_status -> setText("socket状态：ClosingState");
        break;
    case QAbstractSocket::ListeningState:
        socket_status -> setText("socket状态：ListeningState");
        break;
    }
}
```


## enum QAbstractSocket::NetworkLayerProtocol
这个集合包含了网络连接使用的各种协议  
```
Constant   Value   Description
QAbstractSocket::IPv4Protocol   0   IPv4
QAbstractSocket::IPv6Protocol   1   IPv6
QAbstractSocket::AnyIPProtocol   2   IPv4 或 IPv6
QAbstractSocket::UnknownNetworkLayerProtocol   -1   非IPv4和IPv6的其他类型
```


## enum QAbstractSocket::SocketType
这个集合包含了使用的协议类型  
```
Constant   Value   Description
QAbstractSocket::TcpSocket   0   TCP
QAbstractSocket::UdpSocket   1   UDP
QAbstractSocket::SctpSocket   2   SCTP
QAbstractSocket::UnknownSocketType   -1   非TCP、UDP、SCTP的其他类型
```


## enum QAbstractSocket::SocketError
这个集合包含了套接字的所有错误类型  
备注：这个集合是没有注册的元对象，使用时必须用Q_DECLARE_METATYPE()和qRegisterMetaType()去注册  
```

```


## enum QAbstractSocket::SocketOption
这个集合包含了套接字可以设置的选项  
可以在接收到connected()信号之后进行设置，或者在从QTcpServer接收到一个新的socket对象之后进行设置  
```

```


## enum QAbstractSocket::BindMode/BindFlag
这个集合包含了在使用bind()函数时的绑定模式  
```
Constant   Value   Description
QAbstractSocket::ShareAddress   0x1
QAbstractSocket::DontShareAddress   0x2
QAbstractSocket::ReuseAddressHint   0x4
QAbstractSocket::DefaultForPlatform   0x0
```
