# QTcpServer

## 基本功能
QTcpServer提供一个基于TCP的服务端，可以接收到来的TCP连接请求并建立连接  
可以自己指定一个端口，也可以让QTcpServer自动选择一个端口  
可以监听一个特定地址，也可以监听所有主机的地址  
```
TCP客户端包括：QTcpSocket
TCP服务端包括：QTcpSocket、QTcpServer
```
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  
备注：TCP的客户端和服务端可以在同一计算机(即相同IP)上进行运行测试  


## 继承关系
注意：QTcpServer不是QAbstractSocket的子类  
```
                                            | - QSctpSocket
QIODevice - QAbstractSocket - |-QTcpSocket -| - QSslSocket
                              |-QUdpSocket
```


## 工作过程
1. 服务端首先使用listen()开始监听，当有新的TCP连接请求时，QTcpServer内部的incomingConnection()函数会创建一个与客户端连接的QTcpSocket对象，然后发射信号newConnection()  
2. 在newConnection()信号对应的槽函数中，可以用nextPendingConnection()接受客户端的连接，然后使用QTcpSocket对象与客户端通信  
3. QTcpServer主要负责建立起TCP连接，在连接建立起来之后，具体的数据通信由一对QTcpSocket完成  


## TCP通信与多线程
TCP通信只有单播模式，而一般情况下，TCP的服务端要允许多个客户端接入  
为了每组socket之间的通信独立，互不影响，需要采用多线程，即为每一个socket创建一个线程  


## 构造函数
1. QTcpServer::QTcpServer(QObject \*parent = nullptr)


## 常用公共函数
1. void QTcpServer::close()
关闭服务端，服务端不再监听任何TCP连接请求  
注意：在socket已经连接之后，停止监听不会影响原有socket之间的通信，只会忽视新的socket连接请求  

2. bool QTcpServer::listen(const QHostAddress &address = QHostAddress::Any, quint16 port = 0)
告诉服务端在指定的主机地址和端口上监听TCP连接请求，返回true或false  
address参数默认为QHostAddress::Any，即服务端会监听所有的网络接口  
port参数默认为0，服务端会自动选择一个端口  
一般一个服务程序只监听某个端口的网络连接  

3. bool QTcpServer::isListening() const
判断服务端是否正在监听  

4. [virtual] QTcpSocket \*QTcpServer::nextPendingConnection()
返回下一个等待接入的连接套接字，如果没有等待接入的连接，则返回空指针nullptr  
备注：这个套接字是服务端的一个子类，也就是说，当QTcpServer对象被销毁时，QTcpSocket会被自动删除  
注意：返回的QTcpSocket对象不能其他线程使用，如果想在其他线程中使用下一个连接的QTcpSocket对象，需要重写incomingConnection()函数  

5. QHostAddress QTcpServer::serverAddress() const
如果服务端正处于监听状态，返回服务端的地址，否则返回QHostAddress::Null  

6. quint16 QTcpServer::serverPort() const
如果服务端正处于监听状态，返回服务端的端口，否则返回0  

7. bool QTcpServer::waitForNewConnection(int msec = 0, bool \*timedOut = nullptr)
以阻塞方式等待新的连接，如果在等待时间内有新的连接，则返回true，否则返回false  
如果等待超时了，且timeOut参数不是空指针nullptr，则timeOut参数会被设置为true  
如果msec参数设置为-1，则永远不超时  


## 信号函数
1. [signal] void QTcpServer::acceptError(QAbstractSocket::SocketError socketError)
如果在接收一个新的TCP连接请求时发生错误，则会发出该信号  
socketError参数为发生错误的类型  

2. [signal] void QTcpServer::newConnection()
每次有新的连接请求时，则会发出该信号  


## 保护函数
1. [virtual protected] void QTcpServer::incomingConnection(qintptr socketDescriptor)
当有新的连接请求时，QTcpServer会在内部调用该函数，创建一个QTcpSocket对象，然后添加到内部可用新连接的列表中，最后发射newConnection()信号函数  
如果是一个继承于QTcpServer的子类，则可以在子类中对该函数进行重写，但必须调用addPendingConnection()函数  
socketDescriptor参数代表一个本地套接字，对应即将建立的TCP连接  

2. [protected] void QTcpServer::addPendingConnection(QTcpSocket \*socket)
这个函数一般在incomingConnection()函数的内部中调用，将创建的QTcpSocket对象添加到内部可用新连接的列表中  
