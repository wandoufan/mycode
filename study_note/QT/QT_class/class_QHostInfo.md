# QHostInfo

## 基本功能
QHostInfo提供了一些静态函数，可以用来查询主机名等各种主机信息  
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  
```
构造对象时，lookup ID是怎么来的？代表什么含义？
```


## 代码示例
1. 返回IP地址列表
```
QList<QHostAddress> address_list = info.addresses();
if(!address_list.isEmpty())
{
    for(int i = 0; i < address_list.size(); i++)
    {
        qDebug() << address_list[i].toString();
        qDebug() << address_list[i].protocol();
    }
}
```
2. 查询本机的IPV4地址
```
QString MainWindow::getLocalIP()
{
    QString host_name = QHostInfo::localHostName(); //本地主机名
    QHostInfo host_info = QHostInfo::fromName(host_name); //本地主机信息
    QString local_ip = "";
    QList<QHostAddress> address_list = host_info.addresses();
    if(!address_list.isEmpty())
    {
        for(int i = 0; i < address_list.size(); i++)
        {
            QHostAddress address = address_list[i];
            if(address.protocol() == QAbstractSocket::IPv4Protocol)
            {
                local_ip = address.toString();
                break;
            }
        }
    }
    return local_ip;
}
```


## 构造函数
1. QHostInfo::QHostInfo(const QHostInfo &other)
将其他hostinfo对象拷贝为一个新的hostinfo对象  

2. QHostInfo::QHostInfo(int id = -1)
构建一个空的hostinfo对象，其中id参数代表lookup ID，默认值为-1  


## 常用公共函数
1. QString QHostInfo::hostName() const
查询主机名  

2. void QHostInfo::setHostName(const QString &hostName)
设置主机名  

3. int QHostInfo::lookupId() const
返回lookup ID  

4. void QHostInfo::setLookupId(int id)
设置lookup ID  

5. QHostInfo::HostInfoError QHostInfo::error() const
如果查找失败，返回错误类型，否则返回NoError  

6. void QHostInfo::setError(QHostInfo::HostInfoError error)
设置错误类型（没有明白什么意思）  

7. QString QHostInfo::errorString() const
如果查找失败，返回一个易于读懂的错误描述，否则返回"Unknown error"  

8. void QHostInfo::setErrorString(const QString &str)
设置查找失败时的错误描述  

9. QList<QHostAddress> QHostInfo::addresses() const
根据主机名返回相关的IP地址列表，主机名不唯一，因此可能会有重复  
```
QHostInfo::addresses()和QNetworkInterface::allAddresses()的功能类似，都是返回QList<QHostAddress>
区别在于，QNetworkInterface返回地址更多，包含了本机127.0.0.1，而QHostInfo不会返回本机
```

10. void QHostInfo::setAddresses(const QList<QHostAddress> &addresses)
用一个地址列表给主机设置IP地址  


## 公共静态函数
1. [static] void QHostInfo::abortHostLookup(int id)
中断查找指定ID的主机，就像lookupHost()函数返回的  

2. [static] QHostInfo QHostInfo::fromName(const QString &name)
根据指定的主机名返回IP地址，在查找期间函数会被阻塞，也就是说程序会等到查询结果出来再继续往下执行  
如果传入IP地址作为函数参数，则会返回对应的主机名  
```
QString host_name = QHostInfo::localHostName();
QHostInfo info = QHostInfo::fromName(host_name);
```

3. [static] QString QHostInfo::localDomainName()
返回本机的DNS域名  

4. [static] QString QHostInfo::localHostName()
返回本机的主机名，主机名不保证全局唯一  

5. [static] int QHostInfo::lookupHost(const QString &name, QObject \*receiver, const char \*member)
查找主机信息，返回一个lookup ID  
name参数可以是表示主机名、域名或IP地址的字符串  
receiver参数可以设置成信号函数或槽函数，查找可能需要一定时间，但不会阻塞进程，当查找完成时，就可以用QHostInfo作为参数来调用这些函数  
```
QHostInfo::lookupHost("www.kde.org", this, SLOT(lookedUp(QHostInfo)));
```
对应的槽函数可以根据查找结果将IP地址等基本信息输出出来，或者当失败时报告一个错误  
```
void MyWidget::lookedUp(const QHostInfo &host)
{
    if (host.error() != QHostInfo::NoError)
    {
        qDebug() << "Lookup failed:" << host.errorString();
        return;
    }

    const auto addresses = host.addresses();
    for (const QHostAddress &address : addresses)
        qDebug() << "Found address:" << address.toString();
}
```
主机名也可以用IP地址进行代替  
```
QHostInfo::lookupHost("192.168.1.1", this, SLOT(lookedUp(QHostInfo)));
```


## enum QHostInfo::HostInfoError
主机查找的报错码  
```
QHostInfo::NoError   0   查找成功
QHostInfo::HostNotFound   1   没有找到对应的主机
QHostInfo::UnknownError   2   未知的错误
```