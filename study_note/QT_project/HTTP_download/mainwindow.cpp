#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_download_clicked()
{
    //开始下载
    //URL实例：http://pic37.nipic.com/20140113/8800276_184927469000_2.png
    QString url_string = ui -> url_path -> text().trimmed();
    QUrl url = QUrl::fromUserInput(url_string);
    if(!url.isValid())
    {
        QMessageBox::about(this, "URL错误", QString("错误信息：%1").arg(url.errorString()));
        return;
    }
    QString full_file_path = ui -> save_path -> text() + url.fileName();
    if(QFile::exists(full_file_path))
    {
        //如果文件已经存在，就先删除该文件
        QFile::remove(full_file_path);
        QMessageBox::about(this, "文件已存在", "旧文件已删除");
    }
    download_file =new QFile(full_file_path);
    if(!download_file -> open(QIODevice::WriteOnly))
    {
        QMessageBox::about(this, "错误", "临时文件打开错误");
        return;
    }
    ui -> pushButton_download -> setEnabled(false);
    //发起网络请求
    request = QNetworkRequest(url);
    reply = manage.get(request);
    connect(reply, SIGNAL(finished()), this, SLOT(on_finished()));
    connect(reply, SIGNAL(readyRead()), this, SLOT(on_readyRead()));
    connect(reply, SIGNAL(downloadProgress(qint64, qint64)), this, SLOT(on_downloadProgress(qint64, qint64)));
}

void MainWindow::on_finished()
{
    //finished()信号的响应函数
    download_file -> close();
    delete download_file;
    download_file = Q_NULLPTR;
    reply -> deleteLater();
    reply = Q_NULLPTR;
    ui -> pushButton_download -> setEnabled(true);
}

void MainWindow::on_readyRead()
{
    //readyRead()信号的响应函数
    download_file -> write(reply -> readAll());
}

void MainWindow::on_downloadProgress(qint64 bytesReceived, qint64 bytesTotal)
{
    //downloadProgress()信号的响应函数, 显示下载进度
    ui -> progressBar -> setMaximum(bytesTotal);
    ui -> progressBar -> setValue(bytesReceived);
}

