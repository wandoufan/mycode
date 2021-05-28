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
    connect(udp_socket, SIGNAL(stateChanged(QAbstractSocket::SocketState)), this, SLOT(onSocketStateChange(QAbstractSocket::SocketState)));
    connect(udp_socket, SIGNAL(readyRead()), this, SLOT(onSocketReadyRead()));
    onSocketStateChange(udp_socket -> state());

    ui -> button_bind_port -> setEnabled(true);
    ui -> button_unbind_port -> setEnabled(false);
    ui -> button_send_message -> setEnabled(false);
    ui -> button_broadcast_message -> setEnabled(false);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_button_bind_port_clicked()
{
    //绑定端口
    int port = ui -> send_port -> value();
    if(udp_socket -> bind(port))
    {
        ui -> textBrowser -> append("**端口绑定成功..");
        ui -> button_bind_port -> setEnabled(false);
        ui -> button_unbind_port -> setEnabled(true);
        ui -> button_send_message -> setEnabled(true);
        ui -> button_broadcast_message -> setEnabled(true);
    }
    else
    {
        ui -> textBrowser -> append("**端口绑定失败..");
    }
}

void MainWindow::on_button_unbind_port_clicked()
{
    //解绑端口
    udp_socket -> abort();
    ui -> textBrowser -> append("**端口解除绑定");
    ui -> button_bind_port -> setEnabled(true);
    ui -> button_unbind_port -> setEnabled(false);
    ui -> button_send_message -> setEnabled(false);
    ui -> button_broadcast_message -> setEnabled(false);
}

void MainWindow::on_button_clear_clicked()
{
    ui -> textBrowser -> clear();
}

void MainWindow::on_button_quit_clicked()
{

}

void MainWindow::on_button_send_message_clicked()
{
    //发送单播消息，需要指定IP+端口
    QString receive_ip = ui -> receive_ip -> text();
    QHostAddress receive_address(receive_ip);
    int receive_port = ui -> receive_port -> value();
    QString message = ui -> message -> text();
    QByteArray data = message.toUtf8();
    udp_socket -> writeDatagram(data, receive_address, receive_port);//发出数据报
    ui -> textBrowser -> append("[unicast-out] " + message);
    ui -> message -> clear();
}

void MainWindow::on_button_broadcast_message_clicked()
{
    //发送广播消息，只需要指定端口，IP设为QHostAddress::Broadcast即可
    int receive_port = ui -> receive_port -> value();
    QString message = ui -> message -> text();
    QByteArray data = message.toUtf8();
    udp_socket -> writeDatagram(data, QHostAddress::Broadcast, receive_port);//发出数据报
    ui -> textBrowser -> append("[broadcast-out] " + message);
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
