#include <QThread>
#include <QMutex>
#include <QWaitCondition>
#include <QRandomGenerator>
#include <QDebug>


class QThreadProducer : public QThread
{
    //"生产者"线程，用来生产数据，即掷骰子产生点数
    Q_OBJECT
public:
    QThreadProducer(QMutex *mut, QWaitCondition *condition);
    void stopThread();
    int getSeq();
    int getValue();

protected:
    void run();

private:
    bool m_stop = false; // 停止线程
    int m_seq = 0;//掷骰子的次数
    int m_dice_value = 0;//掷骰子产生的点数
    QMutex *mutex;
    QWaitCondition *newdataAvailable;
};


class QThreadConsumer : public QThread
{
    //"消费者"线程，用来消费数据，把读取骰子的点数并送给主线程进行显示
    Q_OBJECT
public:
    QThreadConsumer(QThreadProducer *thread_producer, QMutex *mut, QWaitCondition *condition);
    void stopThread();

protected:
    void run();

private:
    bool m_stop = false; //停止线程
    QThreadProducer *producer;
    QMutex *mutex;
    QWaitCondition *newdataAvailable;

signals:
    void newValue(int seq, int diceValue);
};


