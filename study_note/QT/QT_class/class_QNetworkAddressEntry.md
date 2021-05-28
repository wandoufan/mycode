# QNetworkAddressEntry

## 基本功能
QNetworkAddressEntry存储一个IP地址，以及相关的网关和子网掩码地址  


## 构造函数
1. QNetworkAddressEntry::QNetworkAddressEntry(const QNetworkAddressEntry &other)
将其他QNetworkAddressEntry对象拷贝为一个新的QNetworkAddressEntry对象  

2. QNetworkAddressEntry::QNetworkAddressEntry()
创建一个空对象  


## 常用公共函数
1. QHostAddress QNetworkAddressEntry::ip() const
返回网络接口中的IPV4或IPV6地址  

2. QHostAddress QNetworkAddressEntry::netmask() const
返回子网掩码地址，如'255.255.255.0'  

3. QHostAddress QNetworkAddressEntry::broadcast() const
返回网关地址，如'192.168.7.255'  



