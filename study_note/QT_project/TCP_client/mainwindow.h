#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QMainWindow>
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
//    void closeEvent(QCloseEvent *evet);

private slots:
    //按键槽函数
    void on_button_connect_server_clicked();
    void on_button_disconnect_server_clicked();
    void on_button_clear_clicked();
    void on_button_quit_clicked();
    void on_button_send_message_clicked();
    //自定义槽函数
    void onClientConnected();
    void onClientDisconnected();
    void onSocketReadyRead();
    void onSocketStateChange(QAbstractSocket::SocketState socketState);
    void onErrorOccurred(QAbstractSocket::SocketError error);

private:
    QString getLocalIP();

private:
    Ui::MainWindow *ui;
    QTcpSocket *tcp_socket;
    QLabel *socket_status;
};

#endif // MAINWINDOW_H
