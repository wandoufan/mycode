#ifndef DIALOG_H
#define DIALOG_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QDialog>
#include <QTime>
#include <QCloseEvent>
#include "qmythread.h"

QT_BEGIN_NAMESPACE
namespace Ui { class Dialog; }
QT_END_NAMESPACE

class Dialog : public QDialog
{
    Q_OBJECT

public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();

protected:
    void closeEvent(QCloseEvent *event);

private slots:
    //点击按钮响应槽函数
    void on_startButton_clicked();
    void on_finishButton_clicked();
    void on_clearButton_clicked();
    //自定义槽函数
    void onProduceStarted();
    void onProduceFinished();
    void onConsumerStarted();
    void onConsumerFinished();
    void readNewValue(int seq, int diceValue);

private:
    Ui::Dialog *ui;
    QThreadProducer thread_producer;
    QThreadConsumer thread_consumer;
};
#endif // DIALOG_H
