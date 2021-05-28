#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QString ip = "TCP 客户端 -- 本机IP:";
    ip += getLocalIP();
    this -> setWindowTitle(ip);

    socket_status = new QLabel("socket状态：");
    socket_status -> setMinimumWidth(300);
    ui -> statusbar -> addWidget(socket_status);

    ui -> button_connect_server -> setEnabled(true);
    ui -> button_disconnect_server -> setEnabled(false);
    ui -> button_send_message -> setEnabled(false);

    tcp_socket = new QTcpSocket(this);
    connect(tcp_socket, SIGNAL(connected()), this, SLOT(onClientConnected()));
    connect(tcp_socket, SIGNAL(disconnected()), this, SLOT(onClientDisconnected()));
    connect(tcp_socket, SIGNAL(stateChanged(QAbstractSocket::SocketState)), this, SLOT(onSocketStateChange(QAbstractSocket::SocketState)));
    connect(tcp_socket, SIGNAL(readyRead()), this, SLOT(onSocketReadyRead()));
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_button_connect_server_clicked()
{
    //连接到指定的服务器
    QString ip = ui -> server_ip -> text();
    int port = ui -> server_port -> value();
    tcp_socket -> connectToHost(ip, port);
}

void MainWindow::on_button_disconnect_server_clicked()
{
    //断开与服务器的连接
    if(tcp_socket -> state() == QAbstractSocket::ConnectedState)
    {
        tcp_socket -> disconnectFromHost();
    }
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
    //发送一行消息，以换行符'\n'结束
    if(tcp_socket -> isValid())
    {
        QString message = ui -> message -> text();
        ui -> textBrowser -> append("[out] " + message);
        ui -> message -> clear();
        QByteArray string = message.toUtf8();
        string.append('\n');
        tcp_socket -> write(string);
    }
    else
    {
        ui -> textBrowser -> append("**套接字不合法，无法发送..");
    }
}

void MainWindow::onClientConnected()
{
    ui -> textBrowser -> append("**正在连接到服务器..");
    ui -> textBrowser -> append("**服务器地址：" + tcp_socket -> peerAddress().toString());
    ui -> textBrowser -> append("**服务器端口：" + QString::number(tcp_socket -> peerPort()));
    ui -> button_connect_server -> setEnabled(false);
    ui -> button_disconnect_server -> setEnabled(true);
    ui -> button_send_message -> setEnabled(true);
}

void MainWindow::onClientDisconnected()
{
    ui -> textBrowser -> append("**已经断开与服务器的连接..");
    ui -> button_connect_server -> setEnabled(true);
    ui -> button_disconnect_server -> setEnabled(false);
    ui -> button_send_message -> setEnabled(false);
}

void MainWindow::onSocketReadyRead()
{
    //当缓冲区有新的数据可读时，读取数据
    while (tcp_socket -> canReadLine())
    {
        ui -> textBrowser -> append("[in] " + tcp_socket -> readLine());
    }
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

void MainWindow::onErrorOccurred(QAbstractSocket::SocketError error)
{
    //当发生错误时，进行响应
    qDebug() << "发生错误：" << error;
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

