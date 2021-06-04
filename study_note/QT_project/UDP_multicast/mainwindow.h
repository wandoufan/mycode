#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QMainWindow>
#include <QUdpSocket>
#include <QLabel>
#include <QHostAddress>
#include <QHostInfo>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

//实现组播功能的UDP通信demo
class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    //按键槽函数
    void on_button_join_group_clicked();
    void on_button_leave_group_clicked();
    void on_button_clear_clicked();
    void on_button_quit_clicked();
    void on_button_multicast_message_clicked();
    //自定义槽函数
    void onSocketStateChange(QAbstractSocket::SocketState socketState);
    void onSocketReadyRead();

private:
    QString getLocalIP();

private:
    Ui::MainWindow *ui;
    QLabel *socket_status;
    QUdpSocket *udp_socket;
    QHostAddress group_address; //组播地址
};
#endif // MAINWINDOW_H
