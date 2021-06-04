#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QString ip = "TCP 服务端 -- 本机IP:";
    ip += getLocalIP();
    this -> setWindowTitle(ip);

    socket_status = new QLabel("socket状态：");
    socket_status -> setMinimumWidth(200);
    ui -> statusbar -> addWidget(socket_status);

    udp_socket = new QUdpSocket(this);
    udp_socket -> setSocketOption(QAbstractSocket::MulticastTtlOption, 1); //设置只能在同一个路由下的局域网内进行传播
    connect(udp_socket, SIGNAL(stateChanged(QAbstractSocket::SocketState)), this, SLOT(onSocketStateChange(QAbstractSocket::SocketState)));
    connect(udp_socket, SIGNAL(readyRead()), this, SLOT(onSocketReadyRead()));
    onSocketStateChange(udp_socket -> state());

    ui -> button_join_group -> setEnabled(true);
    ui -> button_leave_group -> setEnabled(false);
    ui -> button_multicast_message -> setEnabled(false);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_button_join_group_clicked()
{
    QString ip = ui -> multiple_ip -> text();
    group_address = QHostAddress(ip); //组播地址
    quint16 group_port = ui -> multiple_port -> value(); //组播端口
    if(udp_socket -> bind(QHostAddress::AnyIPv4, group_port, QAbstractSocket::ShareAddress))//绑定端口
    {
        udp_socket -> joinMulticastGroup(group_address); //加入多播组
        ui -> textBrowser -> append("**加入多播组成功..");
        ui -> textBrowser -> append("**组播IP地址：" + ip);
        ui -> textBrowser -> append("**绑定端口：" + QString::number(group_port));
        ui -> button_join_group -> setEnabled(false);
        ui -> button_leave_group -> setEnabled(true);
        ui -> button_multicast_message -> setEnabled(true);
    }
    else
        ui -> textBrowser -> append("**绑定端口失败..");
}

void MainWindow::on_button_leave_group_clicked()
{
    udp_socket -> leaveMulticastGroup(group_address); //退出多播组
    udp_socket -> abort(); //解除绑定
    ui -> textBrowser -> append("**已退出多播组，解除端口绑定..");
    ui -> button_join_group -> setEnabled(true);
    ui -> button_leave_group -> setEnabled(false);
    ui -> button_multicast_message -> setEnabled(false);
}

void MainWindow::on_button_clear_clicked()
{
    ui -> textBrowser -> clear();
}

void MainWindow::on_button_quit_clicked()
{

}

void MainWindow::on_button_multicast_message_clicked()
{
    //发送组播消息，需要指定IP和端口，IP为组播IP
    quint16 group_port = ui -> multiple_port -> value();
    QString message = ui -> message -> text();
    QByteArray data = message.toUtf8();
    udp_socket -> writeDatagram(data, group_address, group_port); //发出数据报
    ui -> textBrowser -> append("[multicast-out] " + message);
    ui -> message -> clear();
}

void MainWindow::onSocketStateChange(QAbstractSocket::SocketState socketState)
{
    //当套接字状态变化时，进行响应
    switch (socketState)
    {
    case QAbstractSocket::UnconnectedState:
        socket_status -> setText("socket状态：UnconnectedState");
        break;
    case QAbstractSocket::HostLookupState:
        socket_status -> setText("socket状态：HostLookupState");
        break;
    case QAbstractSocket::ConnectingState:
        socket_status -> setText("socket状态：ConnectingState");
        break;
    case QAbstractSocket::ConnectedState:
        socket_status -> setText("socket状态：ConnectedState");
        break;
    case QAbstractSocket::BoundState:
        socket_status -> setText("socket状态：BoundState");
        break;
    case QAbstractSocket::ClosingState:
        socket_status -> setText("socket状态：ClosingState");
        break;
    case QAbstractSocket::ListeningState:
        socket_status -> setText("socket状态：ListeningState");
        break;
    }
}

void MainWindow::onSocketReadyRead()
{
    //读取接收到的数据报
    while(udp_socket -> hasPendingDatagrams())
    {
        QByteArray datagram;
        datagram.resize(udp_socket -> pendingDatagramSize());
        QHostAddress send_address;
        quint16 send_port;
        //注意：address参数和port参数并不是为了传递值，而是为了接收值，因此两个参数可以是未初始化的空对象
        udp_socket -> readDatagram(datagram.data(), datagram.size(), &send_address, &send_port); //读取数据报
        QString  message = datagram.data();
        ui -> textBrowser -> append("[in] " + message);
        ui -> textBrowser -> append("发送地址：" + send_address.toString());
        ui -> textBrowser -> append("发送端口：" + QString::number(send_port));
    }
}

QString MainWindow::getLocalIP()
{
    //查询本机IPV4地址
    QString host_name = QHostInfo::localHostName();
    QHostInfo host_info = QHostInfo::fromName(host_name);
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
