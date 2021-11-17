# QSerialPort

## 基本功能
QSerialPort提供了操作串口的相关函数，在Qt 5.1中引入  
QSerialPort是继承于QIODevice，除了串口特有的几个属性需要单独设置之外，可以像一般的IO设备一样去访问串口  
父类：QIODevice  
备注：使用前要先在.pro文件中加入'QT += serialport'  


## 详细说明
1. 关于QSerialPort对象是先用open()方法打开端口，还是先设置波特率等各种属性，没有找到明确的说明
网上各种操作都有，目前倾向于先open端口，然后再设置属性  


## 构造函数
1. QSerialPort::QSerialPort(const QSerialPortInfo &serialPortInfo, QObject \*parent = nullptr)
用QSerialPortInfo对象构造一个QSerialPort对象
```
QSerialPortInfo serialportinfo;
...
QSerialPort *myserialport;
myserialport = new QSerialPort(serialportinfo);
```

2. QSerialPort::QSerialPort(const QString &name, QObject \*parent = nullptr)

3. QSerialPort::QSerialPort(QObject \*parent = nullptr)


## 常用成员变量
1. baudRate : qint32
这个属性是指定传输方向的波特率  
如果设置成功或在打开端口之前就已经做过设置，则返回true  
如果设置失败，则返回false，并且为成员变量error设置一个错误码  
设置波特率可以用enum QSerialPort::BaudRate中的值，也可以自己任意写一个正的qin32值  
备注：默认波特率是9600  
1.1 读函数
qint32 baudRate(QSerialPort::Directions directions = AllDirections) const
1.2 写函数
bool setBaudRate(qint32 baudRate, QSerialPort::Directions directions = AllDirections)
备注：在windows平台上，传输方向参数只支持AllDirections模式
1.3 信号函数
void baudRateChanged(qint32 baudRate, QSerialPort::Directions directions)

2. error : SerialPortError
这个属性用来记录串口的错误状态，当各种操作失败时，可以根据这个属性值查找错误原因  
属性的取值都来自于enum QSerialPort::SerialPortError  
备注：默认值为QSerialPort::NoError  
2.1 读函数
QSerialPort::SerialPortError error() const
2.2 写函数
void clearError()
调用后会把属性值重置为QSerialPort::NoError

3. dataBits : DataBits
这个属性用来记录使用的数据位的个数  
如果设置成功或在打开端口之前就已经做过设置，则返回true  
如果设置失败，则返回false，并且为成员变量error设置一个错误码  
属性的取值都来自于enum QSerialPort::DataBits  
默认值为Data8  
3.1 读函数
QSerialPort::DataBits dataBits() const
3.2 写函数
bool setDataBits(QSerialPort::DataBits dataBits)
3.3 信号函数
void dataBitsChanged(QSerialPort::DataBits dataBits)

4. parity : Parity
这个属性用来记录奇偶校验的模式  
如果设置成功或在打开端口之前就已经做过设置，则返回true  
如果设置失败，则返回false，并且为成员变量error设置一个错误码  
属性的取值都来自于enum QSerialPort::Parity  
默认值为NoParity  
4.1 读函数
QSerialPort::Parity parity() const
4.2 写函数
bool setParity(QSerialPort::Parity parity)
4.3 信号函数
void parityChanged(QSerialPort::Parity parity)

5. stopBits : StopBits
这个属性用来记录使用的停止位的个数  
如果设置成功或在打开端口之前就已经做过设置，则返回true  
如果设置失败，则返回false，并且为成员变量error设置一个错误码  
属性的取值都来自于enum QSerialPort::StopBits  
默认值为OneStop  
5.1 读函数
QSerialPort::StopBits stopBits() const
5.2 写函数
bool setStopBits(QSerialPort::StopBits stopBits)
5.3 信号函数
void stopBitsChanged(QSerialPort::StopBits stopBits)

6. flowControl : FlowControl
这个属性用来设置串口的流控制  
注意：只有RS-232接口可以设置流控制，RS-422/RS-485接口不存在流控制，也不必设置  
如果设置成功或在打开端口之前就已经做过设置，则返回true  
如果设置失败，则返回false，并且为成员变量error设置一个错误码  
属性的取值都来自于enum QSerialPort::FlowControl  
默认值为NoFlowControl  
6.1 读函数
QSerialPort::FlowControl flowControl() const
6.2 写函数
bool setFlowControl(QSerialPort::FlowControl flowControl)
6.3 信号函数
void flowControlChanged(QSerialPort::FlowControl flow)


## 常用公共函数
1. void QSerialPort::setPort(const QSerialPortInfo &serialPortInfo)
设置一个端口，这个端口来自于QSerialPortInfo对象中  
```
QSerialPortInfo serialportinfo;
...
serialport = new QSerialPort();
serialport -> setPort(serialportinfo);
```

2. void QSerialPort::setPortName(const QString &name)
设置串口的名字  
QSerialPortInfo中的端口名不可更改，而QSerialPort中的端口名称可以进行自定义  
默认情况下，QSerialPort中的端口名和QSerialPortInfo中的端口名是完全一致的  
注意：QSerialPort中的端口名称虽然可以设置，但只是临时的，程序关闭后设置的名称就会丢失，下次打开程序读取到的还是默认的端口名  
```
qDebug() << serialport -> portName(); //输出："COM5"
serialport -> setPortName("myport");
qDebug() << serialport -> portName(); //输出："myport"
```

3. qint64 QSerialPort::readBufferSize() const
读取readbuffer的大小，默认值为0  
当readbuffer为0时，表示缓冲区大小没有限制，所有传递过来的数据都可以放入缓冲区  

4. void QSerialPort::setReadBufferSize(qint64 size)
设置readbuffer的大小  
readbuffer的大小限制了客户端在调用read()或readAll()之前能够接收的数据的数量  

5. bool QSerialPort::flush()
将缓冲区的数据立刻发送到串口  
如果写入了数据，则返回true，否则返回false，成功写入的字符数取决于操作系统  
一般情况下，不需要调用这个函数，因为QSerialPort会根据事件循环来自动发送数据  
```
serialport -> write(writedata);
serialport -> flush();
```

6. bool QSerialPort::setDataTerminalReady(bool set)
设置DTR信号线的高低电平，set参数为true代表高电平，否则代表低电平  
备注：只针对RS-232接口，RS-422/RS-485接口不必设置  

7. bool QSerialPort::setRequestToSend(bool set)
设置RTS信号线的高低电平，set参数为true代表高电平，否则代表低电平  
备注：只针对RS-232接口，RS-422/RS-485接口不必设置  


## 信号函数



## enum QSerialPort::Direction
集合描述了数据传输的方向  


## enum QSerialPort::BaudRate
集合描述了最常用的几种波特率标准  


## enum QSerialPort::Parity
集合描述了奇偶校验方式  


## enum QSerialPort::DataBits
集合描述了每个字符中使用的数据位的个数(5-8之间)  


## enum QSerialPort::StopBits
集合描述了使用的停止位的个数(1-3之间)  


## enum QSerialPort::SerialPortError
集合描述了常见的串口报错  


## enum QSerialPort::FlowControl
集合描述了流控制的3种方法  
```
QSerialPort::NoFlowControl         0   No flow control
QSerialPort::HardwareControl       1   Hardware flow control (RTS/CTS)
QSerialPort::SoftwareControl       2   Software flow control (XON/XOFF)
QSerialPort::UnknownFlowControl   -1   Unknown flow control
```