# QNetWorkInterface

## 基本功能
QNetWorkInterface可以获得运行程序的主机的所有IP地址和网络接口列表  
一个网络接口可能包含多个IP地址，每个IP地址与掩码或广播地址关联  
如果不需要知道子网掩码和广播的IP地址，可以使用allAdresses()获得主机上所有的IP地址列表  


## 代码示例
1. 返回主机上所有的网络接口列表
```
QList<QNetworkInterface> interface_list = QNetworkInterface::allInterfaces();
for(int i = 0; i < interface_list.size(); i++)
{
    QNetworkInterface interface = interface_list[i];
    if(interface.isValid()) \\对于每个网络接口要判断其是否合法
    {
        qDebug() << interface.hardwareAddress();
        qDebug() << interface.name();
        qDebug() << interface.humanReadableName();
        //返回该网络接口的IP地址列表
        QList<QNetworkAddressEntry> entry_list = interface.addressEntries();
        for(int j = 0; j < entry_list.size(); j++)
        {
            QNetworkAddressEntry entry = entry_list[j];
            qDebug() << "IP地址" << entry.ip().toString();
            qDebug() << "子网掩码" << entry.netmask().toString();
            qDebug() << "网关地址" << entry.broadcast().toString();
        }
    }
    else
        continue;
}
```


## 构造函数
1. QNetworkInterface::QNetworkInterface(const QNetworkInterface &other)
将其他的QNetworkInterface对象拷贝为一个新的QNetworkInterface对象  

2. QNetworkInterface::QNetworkInterface()
创建一个空的QNetworkInterface对象  


## 常用公共函数
1. QList<QNetworkAddressEntry> QNetworkInterface::addressEntries() const
返回该网络接口(包括子网掩码和广播地址)的IP地址列表  

2. QString QNetworkInterface::hardwareAddress() const
返回该接口的硬件地址(即以太网中的MAC地址)  

3. QString QNetworkInterface::humanReadableName() const
如果有易于读懂的网络接口名称，如'Local Area Connection'，则返回该名称  
如果没有设置易于读懂的名称，则返回结果和name()函数一致  

4. bool QNetworkInterface::isValid() const
判断QNetworkInterface对象是否包含合法的网络接口信息  

5. QString QNetworkInterface::name() const
返回网络接口的名称  


## 公共静态函数
1. [static] QList<QHostAddress> QNetworkInterface::allAddresses()
返回主机上所有的IP地址列表  
```
QHostInfo::addresses()和QNetworkInterface::allAddresses()的功能类似，都是返回QList<QHostAddress>
区别在于，QNetworkInterface返回地址更多，包含了本机127.0.0.1，而QHostInfo不会返回本机
```

2. [static] QList<QNetworkInterface> QNetworkInterface::allInterfaces()
返回主机上所有的网络接口列表  

