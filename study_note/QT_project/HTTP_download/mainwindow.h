#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QMainWindow>
#include <QNetworkRequest>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QFile>
#include <QFileInfo>
#include <QMessageBox>


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

//一个通过HTTP进行网络文件下载的demo
class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    //按键槽函数
    void on_pushButton_download_clicked();
    //自定义槽函数
    void on_finished();
    void on_readyRead();
    void on_downloadProgress(qint64 bytesReceived, qint64 bytesTotal);

private:
    Ui::MainWindow *ui;
    QNetworkAccessManager manage; //网络管理
    QNetworkRequest request; //网络请求
    QNetworkReply *reply; //网络响应
    QFile *download_file; //下载保存的临时文件
};
#endif // MAINWINDOW_H
