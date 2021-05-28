#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    ui -> startButton -> setEnabled(true);
    ui -> finishButton -> setEnabled(false);
    connect(&thread_show, SIGNAL(newValue(int *, int, int)), this, SLOT(readNewValue(int *, int, int)));
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::closeEvent(QCloseEvent *event)
{
    if(thread_daq.isRunning() || thread_show.isRunning())
    {
        thread_show.terminate();
        thread_daq.terminate();
    }
    event -> accept();
}

void Dialog::readNewValue(int *data, int count, int seq)
{
    QString result = QString("第%1个缓冲区：").arg(seq);
    for(int i = 0; i < count; i++)
    {
        result += QString("%1, ").arg(data[i]);
    }
    result += '\n';
    ui -> textBrowser -> append(result);
}


void Dialog::on_startButton_clicked()
{
    //先启动数据读取线程，再启动数据采集线程
    ui -> startButton -> setEnabled(false);
    ui -> finishButton -> setEnabled(true);
    thread_show.start();
    thread_daq.start();
}

void Dialog::on_finishButton_clicked()
{
    //先结束数据读取线程，再结束数据采集线程
    thread_show.stopThread();
//    thread_show.wait();
    thread_daq.stopThread();
//    thread_daq.wait();
    ui -> startButton -> setEnabled(true);
    ui -> finishButton -> setEnabled(false);
}

void Dialog::on_clearButton_clicked()
{
    ui -> textBrowser -> clear();
}
