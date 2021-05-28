# QT中的网络通信


## 基本信息
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  


## 网络通信相关的类
### 1. 主机信息查询相关的类
* QHostInfo
查询主机名等各种主机信息  
* QNetWorkInterface
获得运行程序的主机的所有IP地址和网络接口列表  
* QHostAddress
提供一个基于IPV4或IPV6的地址  
* QNetworkAddressEntry
提供网关和子网掩码地址  

### 2. TCP/UDP通信相关的类
* QIODevice
QAbstractSocket的基类，提供了一些数据读写相关的函数  
* QAbstractSocket
QTcpSever和QUdpSocket的基类，提供了所有套接字的公共基础函数  
* QTcpSocket
提供TCP套接字相关的数据传输功能，基本没有自己的成员函数  
* QTcpSever
QTcpServer提供一个基于TCP的服务端，可以接收到来的TCP连接请求并建立连接  
* QUdpSocket
提供UDP套接字相关的数据传输功能，有一些自己的成员函数  
* QNetworkDatagram
一个UDP协议传输的数据包对象  


* QNetworkAccessManager
* QNetworkRequest
* QNetworkReply


