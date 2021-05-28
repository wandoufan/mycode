#include <QSemaphore>
#include <QThread>
#include <QDebug>

class QThreadDAQ : public QThread
{
    //数据采集线程
    //例如数据采集卡在进行连续数据采集时，需要一个单独的线程将采集卡采集的数据读取到缓冲区
    Q_OBJECT
public:
    QThreadDAQ();
    void stopThread();

protected:
    void run();

private:
    bool m_stop = false;
};


class QThreadShow : public QThread
{
    //数据读取线程
    //用于读取已经存满数据的缓冲区中的数据，并传递给主线程显示，采用信号与槽机制与主线程交互
    Q_OBJECT
public:
    QThreadShow();
    void stopThread();

protected:
    void run();

private:
    bool m_stop = false;

signals:
    void newValue(int *data, int count, int seq);
};

