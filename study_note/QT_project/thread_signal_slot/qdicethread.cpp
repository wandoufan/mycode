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

void QDiceThread::run()
{
    //执行线程任务
    m_stop = false;
    m_seq = 0;
    while(!m_stop)
    {
        if(!m_paused)
        {
            m_diceValue = QRandomGenerator::global() -> bounded(1, 7);
            m_seq ++;
            emit newValue(m_seq, m_diceValue);
        }
        //假设线程任务执行一次需要1s
        sleep(1);
    }
    m_paused = true;
    quit();
}
