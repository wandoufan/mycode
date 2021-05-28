#include <QThread>
#include <QMutex>
#include <QWaitCondition>
#include <QRandomGenerator>


class QThreadProducer : public QThread
{
    //"生产者"线程，用来生产数据，即掷骰子产生点数
    Q_OBJECT
public:
    QThreadProducer();
    void stopThread();

protected:
    void run();

private:
    bool m_stop = false; // 停止线程
};


class QThreadConsumer : public QThread
{
    //"消费者"线程，用来消费数据，把读取骰子的点数并送给主线程进行显示
    Q_OBJECT
public:
    QThreadConsumer();
    void stopThread();

protected:
    void run();

private:
    bool m_stop = false; //停止线程

signals:
    void newValue(int seq, int diceValue);
};


