#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    setWindowTitle("Qt多线程应用测试");
    ui -> startButton -> setEnabled(true);
    ui -> beginButton -> setEnabled(false);
    ui -> pauseButton -> setEnabled(false);
    ui -> finishButton -> setEnabled(false);

    connect(&threadA, SIGNAL(started()), this, SLOT(onthreadA_started()));
    connect(&threadA, SIGNAL(finished()), this, SLOT(onthreadA_finished()));
    connect(&threadB, SIGNAL(started()), this, SLOT(onthreadB_started()));
    connect(&threadB, SIGNAL(finished()), this, SLOT(onthreadB_finished()));
    connect(&threadC, SIGNAL(started()), this, SLOT(onthreadC_started()));
    connect(&threadC, SIGNAL(finished()), this, SLOT(onthreadC_finished()));

    connect(&threadA, SIGNAL(newValue(int, int)), this, SLOT(onthreadA_newValue(int, int)));
    connect(&threadB, SIGNAL(newValue(int, int)), this, SLOT(onthreadB_newValue(int, int)));
    connect(&threadC, SIGNAL(newValue(int, int)), this, SLOT(onthreadC_newValue(int, int)));
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::closeEvent(QCloseEvent *event)
{
    //重载函数，在窗口关闭时确保线程被停止
    if(threadA.isRunning())
    {
        threadA.stopThread();
        threadA.wait();
    }
    if(threadB.isRunning())
    {
        threadB.stopThread();
        threadB.wait();
    }
    if(threadC.isRunning())
    {
        threadC.stopThread();
        threadC.wait();
    }
    event -> accept();
}

void Dialog::on_startButton_clicked()
{
    //依次启动3个线程
    threadA.start();
    threadB.start();
    threadC.start();

    ui -> startButton -> setEnabled(false);
    ui -> beginButton -> setEnabled(true);
    ui -> pauseButton -> setEnabled(false);
    ui -> finishButton -> setEnabled(true);
}

void Dialog::on_beginButton_clicked()
{
    //开始投掷，每个线程的开始时间间隔2S
    threadA.diceBegin();
    QThread::sleep(2);
    threadB.diceBegin();
    QThread::sleep(2);
    threadC.diceBegin();

    ui -> beginButton -> setEnabled(false);
    ui -> pauseButton -> setEnabled(true);
}

void Dialog::on_pauseButton_clicked()
{
    //暂停投掷
    threadA.dicePause();
    threadB.dicePause();
    threadC.dicePause();

    ui -> beginButton -> setEnabled(true);
    ui -> pauseButton -> setEnabled(false);
}

void Dialog::on_finishButton_clicked()
{
    //结束线程
    threadA.stopThread();
    threadA.wait();
    threadB.stopThread();
    threadB.wait();
    threadC.stopThread();
    threadC.wait();

    ui -> startButton -> setEnabled(true);
    ui -> beginButton -> setEnabled(false);
    ui -> pauseButton -> setEnabled(false);
    ui -> finishButton -> setEnabled(false);
}

void Dialog::on_clearButton_clicked()
{
    //清空文本
    ui -> textBrowser -> clear();
}

void Dialog::onthreadA_started()
{
    //对线程发出的started()信号进行响应
    ui -> textBrowser -> append("threadA started!");
}

void Dialog::onthreadA_finished()
{
    //对线程发出的finished()信号进行响应
    ui -> textBrowser -> append("threadA finished!");
}

void Dialog::onthreadA_newValue(int seq, int diceValue)
{
    //对线程发出的newValue()信号进行响应
    QString result = QTime::currentTime().toString() + "  ";
    result += QString("线程A: 第%1次投掷，点数为%2").arg(seq).arg(diceValue);
    ui -> textBrowser -> append(result);
}

void Dialog::onthreadB_started()
{
    //对线程发出的started()信号进行响应
    ui -> textBrowser -> append("threadB started!");
}

void Dialog::onthreadB_finished()
{
    //对线程发出的finished()信号进行响应
    ui -> textBrowser -> append("threadB finished!");
}

void Dialog::onthreadB_newValue(int seq, int diceValue)
{
    //对线程发出的newValue()信号进行响应
    QString result = QTime::currentTime().toString() + "  ";
    result += QString("   线程B: 第%1次投掷，点数为%2").arg(seq).arg(diceValue);
    ui -> textBrowser -> append(result);
}

void Dialog::onthreadC_started()
{
    //对线程发出的started()信号进行响应
    ui -> textBrowser -> append("threadC started!");
}

void Dialog::onthreadC_finished()
{
    //对线程发出的finished()信号进行响应
    ui -> textBrowser -> append("threadC finished!");
}

void Dialog::onthreadC_newValue(int seq, int diceValue)
{
    //对线程发出的newValue()信号进行响应
    QString result = QTime::currentTime().toString() + "  ";
    result += QString("      线程C: 第%1次投掷，点数为%2").arg(seq).arg(diceValue);
    ui -> textBrowser -> append(result);
}

