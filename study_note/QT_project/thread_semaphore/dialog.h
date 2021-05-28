#ifndef DIALOG_H
#define DIALOG_H

#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif

#include <QDialog>
#include <QDebug>
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
    void readNewValue(int *data, int count, int seq);

    void on_startButton_clicked();

    void on_finishButton_clicked();

    void on_clearButton_clicked();

private:
    Ui::Dialog *ui;
    QThreadDAQ thread_daq;
    QThreadShow thread_show;
};
#endif // DIALOG_H
