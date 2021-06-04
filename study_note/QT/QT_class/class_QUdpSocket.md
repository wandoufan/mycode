# QUdpSocket

## 基本功能
QUdpSocket提供了一个UDP套接字  
UDP通信是无连接的，不需要提前建立socket连接，每次传输数据都要指定目标地址和端口  
UDP通信也没有服务端，是由两个UDP的socket实现的  
一般的UDP通信程序都是在不同的计算机上运行，约定一个固定的端口作为通信端口  
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  
备注：在同一台计算机上进行运行测试时，两个运行实例必须使用不同的端口上，否则会造成冲突，如果是在不同的计算机上运行，多个运行实例可以使用相同的端口  
备注：单播和多播模式的多个实例可以在同一台计算机(即相同IP)上运行测试，组播的多个实例必须在不同IP的计算机上运行  


## 继承关系
```
                                            | - QSctpSocket
QIODevice - QAbstractSocket - |-QTcpSocket -| - QSslSocket
                              |-QUdpSocket
```


## 工作过程
先使用bind()函数把一个地址和端口绑定起来，之后调用writeDatagram()、readDatagram()、receiveDatagram()等函数来传输数据  
如果想要使用QIODevice中的标准函数，如read()、readLine()、write()等，那必须先调用connectToHost()函数来建立连接到另外一个UDP socket上  
每次有数据写入时，socket都会发出bytesWritten()信号，如果socket只为了发送数据，就不需要调用bind()函数  
每次有数据到达时，socket都会发出readyRead()信号，此时hasPendingDatagrams()函数会返回true，先使用pendingDatagramSize()来获得即将到达的数据块的尺寸，然后使用readDatagram()、receiveDatagram()来读取数据  


## UDP消息传送模式
1. 单播模式(unicast)
一对一数据传输  
2. 组播/多播模式(multicast)
一对多数据传输，目的地址要使用D类IP地址，详见IPV4.md  
使用joinMulticastGroup()和leaveMulticastGroup()函数来控制组内的成员的进入和退出  
使用QAbstractSocket::MulticastTtlOption和QAbstractSocket::MulticastLoopbackOption两个集合来设置TTL和socket选项  
使用setMulticastInterface()来控制组播数据的接口，使用multicastInterface()来查询组播数据的接口  
3. 广播模式(broadcast)
一对所有数据传输，常用于实现网络发现的协议  
要获取广播数据只需指定接收端地址为QHostAdress:Broadcast，相当于"255.255.255.255"  


## 构造函数
1. QUdpSocket::QUdpSocket(QObject \*parent = nullptr)


## 常用公共函数
1. qint64 QUdpSocket::readDatagram(char \*data, qint64 maxSize, QHostAddress \*address = nullptr, quint16 \*port = nullptr)
接收一个不大于maxSize字节的数据包，然后把它存储到data参数中  
如果接收成功，返回接收数据包的大小，否则返回-1  
address参数和port参数是指数据发送方的地址和端口  
maxSize参数如果太小，数据包剩余的部分会丢失，如果设为0，会将整个数据包丢弃  
为了避免数据丢失，可以在读取数据之前先调用pendingDatagramSize()函数来确定数据包的尺寸  
注意：address参数和port参数并不是为了传递值，而是为了接收值，因此两个参数可以是未初始化的空对象  
```
QByteArray datagram;
datagram.resize(udp_socket -> pendingDatagramSize());
QHostAddress send_address;
quint16 send_port;
udp_socket -> readDatagram(datagram.data(), datagram.size(), &send_address, &send_port); //读取数据报
QString  message = datagram.data();
ui -> textBrowser -> append("[in] " + message);
ui -> textBrowser -> append("发送地址：" + send_address.toString());
ui -> textBrowser -> append("发送端口：" + QString::number(send_port));
```

2. QNetworkDatagram QUdpSocket::receiveDatagram(qint64 maxSize = -1)
接收一个不大于maxSize字节的数据包，然后用QNetworkDatagram对象返回，如果接收失败，返回一个不合法的对象  
如果可能，函数会尝试搞清楚数据包的终点地址和端口，以及数据包在传输过程中的跳转次数  
maxSize参数如果太小，数据包剩余的部分会丢失，如果设为0，会将整个数据包丢弃  
maxSize参数默认为-1，即函数会尝试读取整个数据包  

3. qint64 QUdpSocket::writeDatagram(const char \*data, qint64 size, const QHostAddress &address, quint16 port)
将大小为size的char格式的数据data，发送给指定的IP地址和端口  
如果发送成功，返回发送数据包的大小，否则返回-1  
如果数据包太大，函数会返回-1，产生报错'DatagramTooLargeError'  
数据包的最大尺寸依赖于操作系统，但至少有8192字节  
一般不建议发送的数据包大于512字节，即使能够发送成功，在传输过程中数据包也可能会变成碎片  
注意：如果UDP套接字已经使用connectToHost()建立了虚拟连接，请使用write()函数发送数据，否则可能会造成错误  

4. qint64 QUdpSocket::writeDatagram(const QNetworkDatagram &datagram)
这是一个重载函数，使用一个QNetworkDatagram对象作为参数  
数据包的数据内容、目的地址、端口、跳转次数限制等都包含在这个QNetworkDatagram对象中  
如果没有设置目标地址和端口，数据包会被发送到connectToHost()函数中设置的地址  
注意：如果UDP套接字已经使用connectToHost()建立了虚拟连接，请使用write()函数发送数据，否则可能会造成错误  

5. qint64 QUdpSocket::writeDatagram(const QByteArray &datagram, const QHostAddress &host, quint16 port)
这是一个重载函数，发送QByteArray格式的数据到指定的地址和端口  
```
udp_socket -> writeDatagram(data, receive_address, receive_port); \\单播模式
udp_socket -> writeDatagram(data, QHostAddress::Broadcast, receive_port); \\广播模式
```

6. qint64 QUdpSocket::pendingDatagramSize() const
返回下一个要读取的UDP数据包的尺寸，如果没有数据可读，返回-1  

7. bool QUdpSocket::hasPendingDatagrams() const
判断后续是否还有可读取的数据包  

8. bool QUdpSocket::joinMulticastGroup(const QHostAddress &groupAddress)
加入一个组播小组，具体的接口由操作系统自动选择  
注意：调用函数之前，socket必须处于BoundState状态，否则会发生错误  
注意：要加入一个IPV4的小组，socket一定不能使用IPV6(QHostAddress::Any)，必须使用QHostAddress::AnyIPv4  

9. bool QUdpSocket::joinMulticastGroup(const QHostAddress &groupAddress, const QNetworkInterface &iface)
这是一个重载函数，可以指定接口  

10. bool QUdpSocket::leaveMulticastGroup(const QHostAddress &groupAddress)
离开一个组播小组，具体的接口由操作系统自动选择  
注意：调用函数之前，socket必须处于BoundState状态，否则会发生错误  
注意：调用这个函数时使用的参数应该和之前调用joinMulticastGroup()函数的参数一致  

11. bool QUdpSocket::leaveMulticastGroup(const QHostAddress &groupAddress, const QNetworkInterface &iface)
这是一个重载函数，可以指定接口  
注意：调用这个函数时使用的参数应该和之前调用joinMulticastGroup()函数的参数一致  



