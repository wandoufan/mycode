# Qt中的串口通信

## 基本信息
Qt串口模块提供了一些基本的功能：配置、I/O操作、获取及设置RS-232的控制信号  
注意：要在项目中使用Qt串口模块，需要先在.pro文件中加入'QT += serialport'  
备注：Qt5.15帮助手册中只提到了RS-232接口，但实际测试RS-485接口的设备也支持  


## Qt串口模块不支持的功能
1. 终端功能，如echo、控制CR/LF等等
2. Text模式
3. 在数据读写时配置超时和延迟时间
4. Pinout引出线的信号改变时发出通知
5. 一些特殊的收发器条件，如框架报错、奇偶报错、break条件报错


## 串口通信相关的类
1. QSerialPort
提供了操作串口的相关函数  
2. QSerialPortInfo
提供了已经存在的串口的各种信息  


## 关于选择COM口以及端口名称问题
1. 打开指定COM口
在串口调试工具上一般都要选择要连接的COM口，设备具体使用哪个COM口要在设备管理器中查看  
用户在下拉菜单中选择了的COM口选项之后，程序就要去找到并打开对应的COM口  
在QSerialPort和QSerialPortInfo中都提供了portName()方法来获得端口名称  
QSerialPortInfo中的端口名一般都是'COM5'这种规范的格式，而且不可更改  
QSerialPort中的端口名可以自己设置为任意名称，不一定就是'COM5'这种格式  
因此，一般用QSerialPortInfo中的端口名来和用户选择的COM口进行对应  
```
qDebug() << serialport -> portName(); //输出："COM5"
qDebug() << serialportinfo.portName(); //输出："COM5"
serialport -> setPortName("myport");
qDebug() << serialport -> portName(); //输出："myport"
qDebug() << serialportinfo.portName(); //输出："COM5"
```
2. 另外要注意一点，portName方法的返回值都是QString，如果用cout输出就显示为一串数字  
```
cout << serialport -> portName().data() << endl;//输出：000001B7611CD9E8
cout << serialportinfo -> portName().data() << endl;//输出：000001B7611CDD78
```
但如果用QDebug()直接把QString输出出来，就能得到正常可读的端口名称  
```
qDebug() << serialport -> portName();//输出："COM5"
qDebug() << serialportinfo.portName();//输出："COM5"
```


## 关于RS-485串口的说明
RS-485是半双工协议，因此上位机和下位机之间无法同时发送数据  
如果在下位机向上位机发送数据时，上位机同时向下位机发送指令，会造成RS-485线路的电平信号异常，上位机无法正常接收数据，下位机也无法正确接收指令  
因此，上位机在发送指令之前，要先检测数据通道是否被占用  
备注：实际上没有检测，只是把发送指令的周期拉长来确保不会产生冲突  


## 关于串口程序同时打开多个串口
1. 情况描述
有一个使用485串口的震动传感器，编写了一个接收并解析震动数据的Qt程序  
程序本身使用完全正常，程序也能同时打开运行多个实例，但无法同时读取多个COM口的数据  
也就是说，即使运行了多个实例，只能有一个实例可以打开COM口，其他实例打开COM口失败  
2. 原因分析
可能是写程序时没有启用多线程  
如果需要同时读取多个COM口设备数据，需要考虑一下这个问题  


## 关于串口发送指令的数据格式
在串口调试工具上一般都有一个选项：是否以HEX方式发送数据  
在使用串口发送数据时一般有两种数据格式  
1. 以字符串格式发送
先将数据转换为二进制，然后再按照8位(假设串口数据位为8位)形式发送出去  
实际使用时，就是直接把QByteArray对象发送出去，没有调用转换二进制的方法  
```
QString str = "01 03 00 00 00 01 84 0A";//查询指令
QByteArray ba = str.toLatin1();
serialport -> write(writedata);
```
2. 以十六进制格式发送
先将数据转换为十六进制，然后再按照8位(假设串口数据位为8位)形式发送出去  
QByteArray提供了很方便16进制编码和解码方法，可以直接调用，不必自己编写  
发送数据：  
```
void SerialPort485::sendData()
{
	QString str = "01 03 00 00 00 01 84 0A";//查询指令
	QByteArray ba = str.toLatin1();
	writedata = QByteArray::fromHex(ba);
	cout << writedata.data() << endl;//输出出来是乱码
	serialport -> write(writedata);
}
```
接收数据：  
```
void SerialPort485::receiveData()
{
	//这个函数是readyRead()信号关联的槽函数
	QByteArray readData = serialport -> readAll();
	cout << "readData: " << readData.data() << endl;//输出出来是乱码
	QString str = QString::fromLatin1(readData.toHex(' '));//输出出来是正常可读数据
	ui -> textBrowser -> setText(str);
}
```
3. 关于两种格式的说明
在对485接口震动传感器的实际测试中发现，这个设备只能接收16进制格式的指令  
如果是以字符串格式指令发送过去之后，会没有任何响应  
如果是错误的指令内容或者任意输入的数据，在发送过去之后也会没有任何响应  


## 关于十六进制指令的进一步说明
1. 要注意，以十六进制发送数据时要调用的是fromHex解码，接收数据时要调用toHex编码  
这与直观的感觉刚好相反，如果发送时用toHex，串口会不识别发送的指令，也不会有响应  
2. 要发送的指令经过fromHex解码之后，得到的数据输出出来会显示乱码(类似象形文字一样)
同样的，接收到的数据直接输出出来也会显示为乱码，在经过toHex编码之后才会正常显示  
最开始以为是错了，但实际上串口是能够正确识别解析这些数据的  
```
QString str = "01 03 00 00 00 01 84 0A";//查询指令
QByteArray ba = str.toLatin1();
cout << ba.toHex(' ').data() << endl;
//输出：30 31 20 30 33 20 30 30 20 30 30 20 30 30 20 30 31 20 38 34 20 30 41
cout << QByteArray::fromHex(ba).data() << endl;
//输出：(乱码)
```


## 关于fromHex()方法和toHex()方法
这两个方法是由QByteArray直接提供的，但其背后的实现原理并不知道  
网上找了一些相关的16进制转换函数作为参考(没有看太懂)  
1. 函数定义：  
```
void SerialPort485::StringToHex(QString str, QByteArray &senddata)
{
    int hexdata,lowhexdata;
    int hexdatalen = 0;
    int len = str.length();
    senddata.resize(len / 2);
    char lstr,hstr;
    for (int i = 0; i < len; )
    {
        hstr = str[i].toLatin1();
        if(hstr == ' ')
        {
            ++i;
            continue;
        }
        ++i;
        if(i >= len)
            break;
        lstr = str[i].toLatin1();
        hexdata = ConvertHexChar(hstr);
        lowhexdata = ConvertHexChar(lstr);
        if((hexdata == 16) || (lowhexdata == 16))
            break;
        else
        {
            hexdata = hexdata*16 + lowhexdata;
            ++i;
            senddata[hexdatalen] = (char)hexdata;
            ++hexdatalen;
        }
    }
    senddata.resize(hexdatalen);
}

char SerialPort485::ConvertHexChar(char ch)
{
    if ((ch >= '0') && (ch <= '9'))
      return ch - 0x30;
     else if ((ch >= 'A') && (ch <= 'F'))
      return ch - 'A' + 10;
     else if ((ch >= 'a') && (ch <= 'f'))
      return ch - 'a' + 10;
     else return -1;
}
```
2. 函数调用：  
```
QByteArray writedata;
QString temp = "01 03 00 00 00 01 84 0A";
StringToHex(temp, writedata);
serialport -> write(writedata);
```
