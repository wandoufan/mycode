#ifndef SERIALPORT485_H
#define SERIALPORT485_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QMainWindow>
#include <QSerialPortInfo>
#include <QSerialPort>
#include <QDebug>
#include <QTime>
#include <QTimer>
#include <QThread>
#include <iostream>
using namespace std;

QT_BEGIN_NAMESPACE
namespace Ui { class SerialPort485; }
QT_END_NAMESPACE

class SerialPort485 : public QMainWindow
{
    Q_OBJECT

public:
    SerialPort485(QWidget *parent = nullptr);
    ~SerialPort485();

public:
    void auto_test();
    void ui_init();
    void parse_data();

public:
    QList<QSerialPortInfo> port_list;
    QList<qint32> baudrate_list;
    QSerialPort *serialport;
    QSerialPortInfo serialportinfo;
    QString readData;
    QByteArray writedata;
    QTime sendTime, receiveTime;
    QTimer *timer;
    int readDataLength = 0;
    int queryMode = 0;
    int send_count = 0;
    int receive_count = 0;
    bool port_state = 0;

public slots:
    void onRead();
    void send_command();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_test_clicked();

    void on_pushButton_7_clicked();

    void on_pushButton_8_clicked();

    void on_pushButton_9_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

private:
    Ui::SerialPort485 *ui;
};
#endif // SERIALPORT485_H


