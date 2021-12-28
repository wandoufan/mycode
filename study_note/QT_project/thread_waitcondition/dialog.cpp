#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    setWindowTitle("Qt多线程应用测试");
    ui -> startButton -> setEnabled(true);
    ui -> finishButton -> setEnabled(false);

    mut = new QMutex();
    condition = new QWaitCondition();
    thread_producer = new QThreadProducer(mut, condition);
    thread_consumer = new QThreadConsumer(thread_producer, mut, condition);

    connect(thread_producer, SIGNAL(started()), this, SLOT(onProduceStarted()));
    connect(thread_producer, SIGNAL(finished()), this, SLOT(onProduceFinished()));
    connect(thread_consumer, SIGNAL(started()), this, SLOT(onConsumerStarted()));
    connect(thread_consumer, SIGNAL(finished()), this, SLOT(onConsumerFinished()));
    connect(thread_consumer, SIGNAL(newValue(int, int)), this, SLOT(readNewValue(int, int)));
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::closeEvent(QCloseEvent *event)
{
    //重载函数，在窗口关闭时确保线程被停止
    if(thread_consumer -> isRunning() || thread_producer -> isRunning() )
    {
        thread_consumer -> stopThread();
        thread_consumer -> wait();
        thread_producer -> stopThread();
        thread_producer -> wait();
    }
    event -> accept();
}

void Dialog::on_startButton_clicked()
{
    //启动线程（先consumer，再producer）
    thread_consumer -> start();
    thread_producer -> start();
    ui -> startButton -> setEnabled(false);
    ui -> finishButton -> setEnabled(true);
}

void Dialog::on_finishButton_clicked()
{
    //结束线程（先consumer，再producer）
    thread_consumer -> stopThread();
    thread_consumer -> wait();
    thread_producer -> stopThread();
    thread_producer -> wait();
    ui -> startButton -> setEnabled(true);
    ui -> finishButton -> setEnabled(false);
}

void Dialog::on_clearButton_clicked()
{
    //清空文本
    ui -> textBrowser -> clear();
}

void Dialog::onProduceStarted()
{
    //对线程发出的started()信号进行响应
    ui -> textBrowser -> append("producer thread started");
}

void Dialog::onProduceFinished()
{
    //对线程发出的started()信号进行响应
    ui -> textBrowser -> append("producer thread finished");
}

void Dialog::onConsumerStarted()
{
    //对线程发出的started()信号进行响应
    ui -> textBrowser -> append("consumer thread started");
}

void Dialog::onConsumerFinished()
{
    //对线程发出的started()信号进行响应
    ui -> textBrowser -> append("consumer thread finished");
}

void Dialog::readNewValue(int seq, int diceValue)
{
    //对线程发出的newValue()信号进行响应
    QString result = QTime::currentTime().toString() + "  ";
    result += QString("第%1次投掷，点数为%2").arg(seq).arg(diceValue);
    ui -> textBrowser -> append(result);
}


