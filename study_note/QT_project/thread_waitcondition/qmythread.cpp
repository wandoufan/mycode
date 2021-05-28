#include "qmythread.h"

QMutex mutex;
QWaitCondition newdataAvailable;
int seq = 0;
int dice_value = 0;


QThreadProducer::QThreadProducer()
{

}

void QThreadProducer::stopThread()
{
    m_stop = true;
}

void QThreadProducer::run()
{
    m_stop = false;
    seq = 0;
    while(!m_stop)
    {
        mutex.lock();
        dice_value = QRandomGenerator::global() -> bounded(1, 7);
        seq ++;
        mutex.unlock();
        newdataAvailable.wakeAll(); //新数据已经产生，可以唤醒所有线程
        sleep(3); //假设线程任务执行一次需要3s
    }
    quit();
}

QThreadConsumer::QThreadConsumer()
{

}

void QThreadConsumer::stopThread()
{
    m_stop = true;
}

void QThreadConsumer::run()
{
    m_stop = false;
    while(!m_stop)
    {
        mutex.lock();
        newdataAvailable.wait(&mutex); //设置wait条件，等待被唤醒
        emit newValue(seq, dice_value);
        mutex.unlock();
    }
    quit();
}
