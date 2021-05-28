#include "qdicethread.h"

QDiceThread::QDiceThread()
{

}

void QDiceThread::diceBegin()
{
    m_paused = false;
}

void QDiceThread::dicePause()
{
    m_paused = true;
}

void QDiceThread::stopThread()
{

    m_stop = true;
}

bool QDiceThread::readVaule(int *seq, int *diceValue)
{
    //被主线程调用，读取数据并传递给主线程
    if(mutex.tryLock())
    {
        *seq = m_seq;
        *diceValue = m_diceValue;
        mutex.unlock();
        return true;
    }
    else
        return false;
}

void QDiceThread::run()
{
    //执行线程任务
    m_stop = false;
    m_seq = 0;
    while(!m_stop)
    {
        if(!m_paused)
        {
            mutex.lock();
            m_diceValue = QRandomGenerator::global() -> bounded(1, 7);
            m_seq ++;
            mutex.unlock();
        }
        //假设线程任务执行一次需要3s
        sleep(3);
    }
    m_paused = true;
    quit();
}
