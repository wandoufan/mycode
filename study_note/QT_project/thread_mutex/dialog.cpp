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
    connect(&timer, SIGNAL(timeout()), this, SLOT(onTimeOut()));
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
    event -> accept();
}

void Dialog::on_startButton_clicked()
{
    //启动线程
    threadA.start();
    ui -> startButton -> setEnabled(false);
    ui -> beginButton -> setEnabled(true);
    ui -> pauseButton -> setEnabled(false);
    ui -> finishButton -> setEnabled(true);
}

void Dialog::on_beginButton_clicked()
{
    //开始投掷
    threadA.diceBegin();
    timer.start(100); //每100ms去读一次数据
    ui -> beginButton -> setEnabled(false);
    ui -> pauseButton -> setEnabled(true);
}

void Dialog::on_pauseButton_clicked()
{
    //暂停投掷
    threadA.dicePause();
    timer.stop();
    ui -> beginButton -> setEnabled(true);
    ui -> pauseButton -> setEnabled(false);
}

void Dialog::on_finishButton_clicked()
{
    //结束线程
    threadA.stopThread();
    threadA.wait();
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
    ui -> textBrowser -> append("thread started");
}

void Dialog::onthreadA_finished()
{
    //对线程发出的finished()信号进行响应
    ui -> textBrowser -> append("thread finished");
}

void Dialog::onTimeOut()
{
    /*函数功能：调用子线程中的readValue()函数来读取数据
      由于定时器的周期为100ms，小于掷骰子产生数据的周期(3s)，因此读出的数据可能是旧的
      需要比较掷骰子的次序来判断是否为新数据*/
    int tmp_seq = 0, tmp_value = 0;
    bool valid = threadA.readVaule(&tmp_seq, &tmp_value);
    if(valid && (tmp_seq != mSeq))
    {
        //此次读到的是新数据
        mSeq = tmp_seq;
        mDiceValue = tmp_value;
        if(mSeq != 0)
        {
            QString result = QTime::currentTime().toString() + "  ";
            result += QString("第%1次投掷，点数为%2").arg(mSeq).arg(mDiceValue);
            ui -> textBrowser -> append(result);
        }
    }
}
