#ifndef DIALOG_H
#define DIALOG_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QDialog>
#include <QCloseEvent>
#include <QTime>
#include <QDebug>
#include "qdicethread.h"

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
    //点击按钮槽函数
    void on_startButton_clicked();
    void on_beginButton_clicked();
    void on_pauseButton_clicked();
    void on_finishButton_clicked();
    void on_clearButton_clicked();
    //自定义槽函数
    void onthreadA_started();
    void onthreadA_finished();
    void onthreadA_newValue(int seq, int diceValue);

private:
    Ui::Dialog *ui;
    QDiceThread threadA;
};
#endif // DIALOG_H
