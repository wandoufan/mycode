# QHostAddress

## 基本功能
QHostAddress提供一个基于IPV4或IPV6的地址  
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  


## 构造函数
1. QHostAddress::QHostAddress(QHostAddress::SpecialAddress address)
以SpecialAddress集合中的某个值为参数构建一个地址对象  
参数详见下面的enum QHostAddress::SpecialAddress  

2. QHostAddress::QHostAddress(const QHostAddress &address)
将其他QHostAddress对象拷贝为一个新的QHostAddress对象  

3. QHostAddress::QHostAddress(const QString &address)
根据IP地址字符串构建一个新的对象  
```
QString ip = ui -> listen_ip -> text();
QHostAddress address(ip);
```

4. QHostAddress::QHostAddress()
创建一个空的地址对象，这个空地址对于任何主机或接口都是非法的  


## 常用公共函数
1. QAbstractSocket::NetworkLayerProtocol QHostAddress::protocol() const
返回该IP地址对应的网络协议  
详见下面的enum QAbstractSocket::NetworkLayerProtocol  

2. QString QHostAddress::toString() const
以字符串的形式返回IP地址  

3. void QHostAddress::clear()
把主机的地址对象设置为Null，把协议设置为QAbstractSocket::UnknownNetworkLayerProtocol  

4. bool QHostAddress::isNull() const
如果主机地址对于任何主机或接口都是非法的，则返回true  


## enum QHostAddress::SpecialAddress
```
Constant   Value   Description
QHostAddress::Null   0   空地址，等于QHostAddress()
QHostAddress::LocalHost   2   IPV4本机地址，等于("127.0.0.1")
QHostAddress::LocalHostIPv6   3   IPv6本机地址，等于("::1")
QHostAddress::Broadcast   1   IPv4广播地址，等于("255.255.255.255")
QHostAddress::AnyIPv4   6   IPv4任意地址，等于("0.0.0.0")，绑定在该端口上的套接字只在IPV4接口上监听
QHostAddress::AnyIPv6   5   IPV6任意地址，等于("::")，绑定在该端口上的套接字只在IPV6接口上监听
QHostAddress::Any   4   任意地址，绑定在该端口上的套接字会同时监听IPV6接口和IPV4接口
```

