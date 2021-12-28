#include "qmythread.h"

QThreadProducer::QThreadProducer(QMutex *mut, QWaitCondition *condition)
{
    mutex = mut;
    newdataAvailable = condition;
}

void QThreadProducer::stopThread()
{
    m_stop = true;
}

int QThreadProducer::getSeq()
{
    return m_seq;
}

int QThreadProducer::getValue()
{
    return m_dice_value;
}

void QThreadProducer::run()
{
    m_stop = false;
    while(!m_stop)
    {
        mutex -> lock();
        m_dice_value = QRandomGenerator::global() -> bounded(1, 7);
        m_seq ++;
        mutex -> unlock();
        newdataAvailable -> wakeAll(); //新数据已经产生，可以唤醒所有线程
        sleep(2); //假设线程任务执行一次需要2s
    }
    quit();
}

QThreadConsumer::QThreadConsumer(QThreadProducer *thread_producer, QMutex *mut, QWaitCondition *condition)
{
    producer = thread_producer;
    mutex = mut;
    newdataAvailable = condition;
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
        mutex -> lock();
        newdataAvailable -> wait(mutex);
        //被wake方法唤醒之后，从生产者线程的数据接口中读取新的数据内容
        int seq = producer -> getSeq();
        int dice_value = producer -> getValue();
        emit newValue(seq, dice_value);
        mutex -> unlock();
    }
    quit();
}
