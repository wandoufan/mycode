#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QMainWindow>
#include <QTcpServer>
#include <QTcpSocket>
#include <QAbstractSocket>
#include <QCloseEvent>
#include <QLabel>
#include <QHostInfo>
#include <QHostAddress>
#include <QDebug>


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

protected:
//    void closeEvent(QCloseEvent *event);

private slots:
    //按键槽函数
    void on_button_start_listen_clicked();
    void on_button_stop_listen_clicked();
    void on_button_clear_clicked();
    void on_button_quit_clicked();
    void on_button_send_message_clicked();
    //自定义槽函数
    void onNewConnection();
    void onSocketStateChange(QAbstractSocket::SocketState socketState);
    void onClientConnected();
    void onClientDisconnected();
    void onSocketReadyRead();
    void onErrorOccurred(QAbstractSocket::SocketError error);

private:
    QString getLocalIP();

private:
    Ui::MainWindow *ui;
    QTcpServer *tcp_server;
    QTcpSocket *tcp_socket;
    QLabel *listen_status, *socket_status;


};
#endif // MAINWINDOW_H
