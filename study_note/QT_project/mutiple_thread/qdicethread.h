#ifndef QDICETHREAD_H
#define QDICETHREAD_H

#include <QThread>
#include <QRandomGenerator>
#include <QDebug>

class QDiceThread : public QThread
{
    Q_OBJECT
public:
    QDiceThread();
    void diceBegin(); //掷一次骰子
    void dicePause(); //暂停
    void stopThread(); //结束线程

protected:
    void run();

private:
    int m_seq = 0; //掷骰子的次数
    int m_diceValue; //骰子点数
    bool m_paused = true; //暂停
    bool m_stop = false; //停止

signals:
    void newValue(int seq, int diceValue); //产生新点数的信号
};

#endif // QDICETHREAD_H
