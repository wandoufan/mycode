#include "serialport485.h"
#include "ui_serialport485.h"

SerialPort485::SerialPort485(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::SerialPort485)
{
    ui->setupUi(this);
    this -> setWindowTitle("震动传感器SD123-Z3TD");
    ui_init();
    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(send_command()));
}

SerialPort485::~SerialPort485()
{
    delete ui;
}


void SerialPort485::auto_test()
{
    //输出各种串口信息
    qDebug() << "port description:" << serialportinfo.description();
    qDebug() << "systemLocation:" << serialportinfo.systemLocation();
    qDebug() << "serialNumber:" << serialportinfo.serialNumber();
    qDebug() << "manufacturer:" << serialportinfo.manufacturer();
    qDebug() << "portInfoName:" << serialportinfo.portName();
    qDebug() << "productIdentifier:" << serialportinfo.productIdentifier();
    qDebug() << "vendorIdentifier:" << serialportinfo.vendorIdentifier();
    qDebug() << "portName:" << serialport -> portName();
    cout << "baudRate:" << serialport  -> baudRate() << endl;
    cout << "error:" << serialport -> error() << endl;
    cout << "dataBits:" << serialport -> dataBits() << endl;
    cout << "stopBits:" << serialport -> stopBits() << endl;
    cout << "parity:" << serialport -> parity() << endl;
    cout << "ReadBufferSize:" << serialport -> readBufferSize() << endl;
}

void SerialPort485::ui_init()
{
    ui -> comboBox -> addItem("COM1");
    ui -> comboBox -> addItem("COM2");
    ui -> comboBox -> addItem("COM3");
    ui -> comboBox -> addItem("COM4");
    ui -> comboBox -> addItem("COM5");
    ui -> comboBox -> addItem("COM6");
    ui -> comboBox -> setCurrentIndex(4);
    ui -> comboBox_2 -> addItem("4800", QSerialPort::Baud4800);
    ui -> comboBox_2 -> addItem("9600", QSerialPort::Baud9600);
    ui -> comboBox_2 -> addItem("19200", QSerialPort::Baud19200);
    ui -> comboBox_2 -> addItem("38400", QSerialPort::Baud38400);
    ui -> comboBox_2 -> addItem("57600", QSerialPort::Baud57600);
    ui -> comboBox_2 -> addItem("115200", QSerialPort::Baud115200);
    ui -> comboBox_2 -> setCurrentIndex(1);
    ui -> comboBox_3 -> addItem("5", QSerialPort::Data5);
    ui -> comboBox_3 -> addItem("6", QSerialPort::Data6);
    ui -> comboBox_3 -> addItem("7", QSerialPort::Data7);
    ui -> comboBox_3 -> addItem("8", QSerialPort::Data8);
    ui -> comboBox_3 -> setCurrentIndex(3);
    ui -> comboBox_4 -> addItem("1", QSerialPort::OneStop);
    ui -> comboBox_4 -> addItem("1.5", QSerialPort::OneAndHalfStop);
    ui -> comboBox_4 -> addItem("2", QSerialPort::TwoStop);
    ui -> comboBox_4 -> setCurrentIndex(0);
    ui -> comboBox_5 -> addItem("NoParity", QSerialPort::NoParity);
    ui -> comboBox_5 -> addItem("EvenParity", QSerialPort::EvenParity);
    ui -> comboBox_5 -> addItem("OddParity", QSerialPort::OddParity);
    ui -> comboBox_5 -> addItem("SpaceParity", QSerialPort::SpaceParity);
    ui -> comboBox_5 -> addItem("MarkParity", QSerialPort::MarkParity);
    ui -> comboBox_5 -> setCurrentIndex(0);
}

void SerialPort485::parse_data()
{
    //将接收到的数据进行解析
//    qDebug() << "readData:" << readData;
    bool ok;
    int temperature = readData.mid(6, 4).toInt(&ok, 16);
    ui -> lcdNumber -> display(temperature/10);
    int shake_x = readData.mid(10, 4).toInt(&ok, 16);
    ui -> lcdNumber_2 -> display(shake_x/10);
    int shake_y = readData.mid(14, 4).toInt(&ok, 16);
    ui -> lcdNumber_3 -> display(shake_y/10);
    int shake_z = readData.mid(18, 4).toInt(&ok, 16);
    ui -> lcdNumber_4 -> display(shake_z/10);
    readData = "";
    readDataLength = 0;
}

void SerialPort485::send_command()
{
    //发送指令：查询温度和x\y\z轴震动参数
    sendTime = QTime::currentTime();
    QString timeInfo = QString("发送时间 %1分:%2秒:%3毫秒").arg(sendTime.minute())\
            .arg(sendTime.second()).arg(sendTime.msec());
    ui -> textBrowser -> append("\n");
    ui -> textBrowser -> append(timeInfo);
    QString command = "01 03 00 00 00 04 44 09";
    writedata = QByteArray::fromHex(command.toLatin1());
    cout << "sendData: " << writedata.data() << endl;
    serialport -> write(writedata);
    send_count += 1;
    ui -> send_cout -> setText(QString::number(send_count));
}

void SerialPort485::onRead()
{
    //读取数据
    //实际测试发现：数据有时候是一次性返回，有时候是分两次返回
    receiveTime = QTime::currentTime();
    QString timeInfo = QString("接收时间 %1分:%2秒:%3毫秒").arg(receiveTime.minute())\
            .arg(receiveTime.second()).arg(receiveTime.msec());
    ui -> textBrowser -> append(timeInfo);
    cout << "bytesAvailable: " << serialport -> bytesAvailable() << endl;
    QByteArray receiveData = serialport -> readAll();
    cout << "receiveData: " << receiveData.data() << endl;
    ui -> textBrowser -> append(QString::fromLatin1(receiveData.toHex(' ')));
    readData.append(receiveData.toHex());
    readDataLength = readData.size();
    if(queryMode == 1 && readDataLength >= 26)
    {
        int spend_time;
        if(receiveTime.msec() > sendTime.msec())
            spend_time = receiveTime.msec() - sendTime.msec();
        else
            spend_time = receiveTime.msec() - sendTime.msec() + 1000;
        timeInfo = QString("本次查询耗时 %1毫秒").arg(spend_time);
        ui -> textBrowser -> append(timeInfo);
        parse_data();
    }
    receive_count += 1;
    ui -> receive_count -> setText(QString::number(receive_count));
}

void SerialPort485::on_pushButton_clicked()
{
    //清除接收文本框的内容
    ui -> textBrowser -> clear();
}

void SerialPort485::on_pushButton_2_clicked()
{
    //打开串口
    if(port_state && serialport -> isOpen())
    {
        ui -> textBrowser_3 -> setText("端口已经打开！");
        return;
    }
    port_list = QSerialPortInfo::availablePorts();
    if(port_list.size() == 0)
    {
        ui -> textBrowser_3 -> setText("电脑中没有可用的COM口！");
        return;
    }
    bool portFound = 0;//标记是否找到目标端口
    for(int i = 0; i < port_list.size(); i++)
    {
        if(port_list[i].portName() == ui -> comboBox -> currentText())
        {
            serialportinfo = port_list[0];
            serialport = new QSerialPort(serialportinfo);
            portFound = 1;
            break;
        }
    }
    if(!portFound)
    {
        ui -> textBrowser_3 -> setText(QString("没有找到端口%1!").arg(ui -> comboBox -> currentText()));
        return;
    }
    connect(serialport, SIGNAL(readyRead()), this, SLOT(onRead()));

    if(serialport -> open(QIODevice::ReadWrite))
    {
        port_state = 1;
        ui -> textBrowser_3 -> setText("端口打开成功！");
        serialport -> setBaudRate(ui -> comboBox_2 -> currentData().value<qint32>());
        serialport -> setDataBits(ui -> comboBox_3 -> currentData().value<QSerialPort::DataBits>());
        serialport -> setStopBits(ui -> comboBox_4 -> currentData().value<QSerialPort::StopBits>());
        serialport -> setParity(ui -> comboBox_5 -> currentData().value<QSerialPort::Parity>());
        auto_test();
    }
    else
    {
        ui -> textBrowser_3 -> setText("端口打开失败！");
        return;
    }
}

void SerialPort485::on_pushButton_3_clicked()
{
    //手动发送数据
    if(!port_state)
    {
        ui -> textBrowser_3 -> setText("串口还没有打开！");
        return;
    }
    queryMode = 2;
    sendTime = QTime::currentTime();
    QString timeInfo = QString("发送时间 %1分:%2秒:%3毫秒").arg(sendTime.minute())\
            .arg(sendTime.second()).arg(sendTime.msec());
    ui -> textBrowser -> append("\n");
    ui -> textBrowser -> append(timeInfo);
    writedata = QByteArray::fromHex(ui -> textEdit -> toPlainText().toLatin1());
    cout << "sendData: " << writedata.data() << endl;
    serialport -> write(writedata);
    send_count += 1;
    ui -> send_cout -> setText(QString::number(send_count));
}

void SerialPort485::on_pushButton_test_clicked()
{
    //临时测试

}

void SerialPort485::on_pushButton_7_clicked()
{
    //清除发送文本框的内容
    ui -> textEdit -> clear();
}

void SerialPort485::on_pushButton_8_clicked()
{
    //循环重复发送查询指令
    if(!port_state)
    {
        ui -> textBrowser_3 -> setText("串口还没有打开！");
        return;
    }
    queryMode = 1;
    timer -> start(200);
}

void SerialPort485::on_pushButton_9_clicked()
{
    //停止循环发送查询质量
    timer -> stop();
}

void SerialPort485::on_pushButton_4_clicked()
{
    //发送和接收的次数清零
    send_count = 0;
    receive_count = 0;
    ui -> send_cout -> setText("0");
    ui -> receive_count -> setText("0");
}

void SerialPort485::on_pushButton_5_clicked()
{
    //关闭串口
    if(!port_state)
        ui -> textBrowser_3 -> setText("串口已经关闭！");
    else
    {
        timer -> stop();
        serialport -> close();
        port_state = 0;
        ui -> textBrowser_3 -> setText("串口关闭成功！");
    }
}
