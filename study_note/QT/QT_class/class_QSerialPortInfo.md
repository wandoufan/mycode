# QSerialPortInfo

## 基本功能
QSerialPortInfo可以提供已经存在的串口的信息，在Qt 5.1中引入  
一般最常用静态函数获取所有的QSerialPortInfo对象  
QSerialPortInfo也常用作QSerialPort类中setPort()方法的输入参数  
备注：使用前要先在.pro文件中加入'QT += serialport'  


## 关于串口信息的说明
通常程序要指定使用某一个确定的串口，串口的名称等信息在不同电脑的不同USB口可能会有变化  
而串口的序列号是唯一不变的，可以用来确定一个串口  
备注：网上看的，没有验证过  


## 构造函数
1. QSerialPortInfo::QSerialPortInfo(const QSerialPortInfo &other)
拷贝一个QSerialPortInfo对象  

2. QSerialPortInfo::QSerialPortInfo(const QString &name)

3. QSerialPortInfo::QSerialPortInfo(const QSerialPort &port)

4. QSerialPortInfo::QSerialPortInfo()


## 常用公共函数
备注：以下串口信息都以震动传感器为例  
1. QString QSerialPortInfo::description() const
返回串口的描述信息，如果没有，就返回一个空字符串  
例如：`USB Serial Port`  

2. QString QSerialPortInfo::systemLocation() const
返回串口的系统位置  
例如：`\\\\.\\COM5`  

3. QString QSerialPortInfo::serialNumber() const
以字符串的形式返回串口号，如果没有，就返回一个空字符串  
备注：串口号中可能会包含字母   
例如：`AB0LHUSKA`  

4. quint16 QSerialPortInfo::productIdentifier() const
返回串口的产品ID，如果没有，就返回0  
例如：`24577`  

5. quint16 QSerialPortInfo::vendorIdentifier() const
返回串口的供应商ID，如果没有，就返回0  
例如：`1027`  

6. QString QSerialPortInfo::manufacturer() const
返回串口的制造商，如果没有，就返回一个空字符串  
例如：`FTDI`  

7. QString QSerialPortInfo::portName() const
返回串口的名字  
这里的串口名字是设备自带的名字，不可更改  
而且名字一般都是'COM5'这种规范格式，可以直接根据这个名字来确定端口  
例如：`COM5`  


## 静态公共函数
1. [static] QList<QSerialPortInfo> QSerialPortInfo::availablePorts()
以列表的形式返回系统中所有可用的串口  
```
QList<QSerialPortInfo> port_list;
port_list = QSerialPortInfo::availablePorts();
```

2. [static] QList<qint32> QSerialPortInfo::standardBaudRates()
以列表的形式返回系统能够支持的所有的波特率  
```
QList<qint32> baudrate_list;
baudrate_list = QSerialPortInfo::standardBaudRates();
for(int i = 0; i < baudrate_list.size(); i++)
{
    cout << "波特率：" << baudrate_list[i] << endl;
}
```
输出结果示例：  
```
波特率：110
波特率：300
波特率：600
波特率：1200
波特率：2400
波特率：4800
波特率：9600
波特率：14400
波特率：19200
波特率：38400
波特率：56000
波特率：57600
波特率：115200
波特率：128000
波特率：256000
```