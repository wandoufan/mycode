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

    listen_status = new QLabel("监听状态：");
    listen_status -> setMinimumWidth(300);
    ui -> statusbar -> addWidget(listen_status);

    socket_status = new QLabel("socket状态：");
    socket_status -> setMinimumWidth(200);
    ui -> statusbar -> insertWidget(1, socket_status);

    ui -> button_start_listen -> setEnabled(true);
    ui -> button_stop_listen -> setEnabled(false);
    ui -> button_send_message -> setEnabled(false);

    tcp_socket = new QTcpSocket(this);
    tcp_server = new QTcpServer(this);
    connect(tcp_server, SIGNAL(newConnection()), this, SLOT(onNewConnection()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_button_start_listen_clicked()
{
    //开始监听
    QString ip = ui -> listen_ip -> text();
    int port = ui -> listen_port -> value();
    QHostAddress address(ip);
    tcp_server -> listen(address, port);
    ui -> textBrowser -> append("**开始监听..");
    ui -> textBrowser -> append("**监听地址：" + tcp_server -> serverAddress().toString());
    ui -> textBrowser -> append("**监听端口：" + QString::number(tcp_server -> serverPort()));
    listen_status -> setText("监听状态：正在监听");
    ui -> button_start_listen -> setEnabled(false);
    ui -> button_stop_listen -> setEnabled(true);
    ui -> button_send_message -> setEnabled(false);
}

void MainWindow::on_button_stop_listen_clicked()
{
    //停止监听
    if(tcp_server -> isListening())
    {
        tcp_server -> close();
        ui -> textBrowser -> append("**停止监听..");
        listen_status -> setText("监听状态：停止监听");
        ui -> button_start_listen -> setEnabled(true);
        ui -> button_stop_listen -> setEnabled(false);
        ui -> button_send_message -> setEnabled(false);
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

void MainWindow::onNewConnection()
{
    //当有新的连接请求时，进行响应
    ui -> textBrowser -> append("有新的连接请求了");
    tcp_socket = tcp_server -> nextPendingConnection();
    /*
     * 这个地方很奇怪，connected()信号函数一直没能生效，onClientConnected()槽函数没有被调用，具体原因没找到
     * 但在TCP客户端程序里，connected()信号函数是可以正常发出的，对应的槽函数也正常运行了
     * 现在只能用if判断来手动调用槽函数onClientConnected()
    */
//    connect(tcp_socket, SIGNAL(connected()), this, SLOT(onClientConnected()));
    if(tcp_socket -> state() == QAbstractSocket::ConnectedState)
        onClientConnected();
    connect(tcp_socket, SIGNAL(disconnected()), this, SLOT(onClientDisconnected()));
    connect(tcp_socket, SIGNAL(stateChanged(QAbstractSocket::SocketState)), this, SLOT(onSocketStateChange(QAbstractSocket::SocketState)));
    connect(tcp_socket, SIGNAL(readyRead()), this, SLOT(onSocketReadyRead()));
    connect(tcp_socket, SIGNAL(errorOccurred(QAbstractSocket::SocketError)), this, SLOT(onErrorOccurred(QAbstractSocket::SocketError)));
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

void MainWindow::onClientConnected()
{
    //当与客户端建立连接之后，进行响应
    ui -> textBrowser -> append("**已经与客户端建立连接..");
    ui -> textBrowser -> append("**客户端地址：" + tcp_socket -> peerAddress().toString());
    ui -> textBrowser -> append("**客户端端口：" + QString::number(tcp_socket -> peerPort()));
    ui -> button_send_message -> setEnabled(true);
}

void MainWindow::onClientDisconnected()
{
    //当与客户端断开连接之后，进行响应
    ui -> textBrowser -> append("**已经与客户端断开连接..");
    tcp_socket -> deleteLater();
}

void MainWindow::onSocketReadyRead()
{
    //当缓冲区有新的数据可读时，读取数据
    while (tcp_socket -> canReadLine())
    {
        ui -> textBrowser -> append("[in] " + tcp_socket -> readLine());
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
