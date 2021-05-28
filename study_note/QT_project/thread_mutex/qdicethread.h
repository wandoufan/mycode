#ifndef QDICETHREAD_H
#define QDICETHREAD_H

#include <QThread>
#include <QRandomGenerator>
#include <QDebug>
#include <QMutex>
#include <QMutexLocker>

class QDiceThread : public QThread
{
    Q_OBJECT
public:
    QDiceThread();
    void diceBegin(); //掷一次骰子
    void dicePause(); //暂停
    void stopThread(); //结束线程
    bool readVaule(int *seq, int *diceValue); //用于主线程读取数据

protected:
    void run();

private:
    QMutex mutex; //互斥量
    int m_seq = 0; //掷骰子的次数
    int m_diceValue = 0; //骰子点数
    bool m_paused = true; //暂停
    bool m_stop = false; //停止
};

#endif // QDICETHREAD_H
