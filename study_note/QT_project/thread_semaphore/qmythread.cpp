﻿#include "qmythread.h"

const int buffer_size = 8;
int buffer1[buffer_size]; //1号缓冲区，存储采集到的数据
int buffer2[buffer_size]; //2号缓冲区，存储采集到的数据

int current_buffer = 1; //当前正在写入的buffer，值为1或2
int buffer_number = 0; //缓冲区序号（已经写入数据的缓冲区个数）
int counter = 0; //数据生成器(模拟采集卡采集到的数据)

QSemaphore empty_buffers(2); //信号量：空的缓冲区个数，初始资源为2个
QSemaphore full_buffers; //信号量：满的缓冲区个数，初始资源为0个

QThreadDAQ::QThreadDAQ()
{

}

void QThreadDAQ::stopThread()
{
    m_stop = true;
}

void QThreadDAQ::run()
{
    m_stop = false;
    current_buffer = 1;
    buffer_number = 0;
    counter = 0;
    if(empty_buffers.available() < 2) //保证线程启动时，空的缓冲区可用资源为2个
    {
        empty_buffers.release(2 - empty_buffers.available());
    }
    while(!m_stop)
    {
        empty_buffers.acquire(1); //申请一个空的缓冲区资源
        for(int i = 0; i < buffer_size; i++)//向缓冲区中写入数据
        {
            if(current_buffer == 1)
                buffer1[i] = counter;
            else
                buffer2[i] = counter;
            counter ++; //模拟数据采集卡采集到的数据
            msleep(50); //假设每50ms采集到一个数据
        }
        buffer_number ++; //已经写入数据的缓冲区个数+1
        if(current_buffer == 1) //切换到另一个buffer继续写入
            current_buffer = 2;
        else
            current_buffer = 1;
        full_buffers.release(1); //释放(创建)一个满的缓冲区资源，即可用满的缓冲区资源+1
    }
    quit();
}

QThreadShow::QThreadShow()
{

}

void QThreadShow::stopThread()
{
    m_stop = true;
}

void QThreadShow::run()
{
    m_stop = false;
    if(full_buffers.available() > 0) //将full_buffers信号量的可用资源初始化为0
    {
        full_buffers.acquire(full_buffers.available());
    }
    while(!m_stop)
    {
        full_buffers.acquire(1); //申请一个满的缓冲区资源(如果没有就阻塞等待数采线程释放资源)
        int buffer_data[buffer_size]; //存储从缓冲区读到数据
        int seq = buffer_number;
        if(current_buffer == 1) //如果当前正在写入的缓冲区是1，则说明2号缓冲区已经满了
        {
            for(int i = 0; i < buffer_size; i++)
            {
                buffer_data[i] = buffer2[i]; //从2号缓冲区中拷贝数据
            }
        }
        else
        {
            for(int i = 0; i < buffer_size; i++)
            {
                buffer_data[i] = buffer1[i]; //从1号缓冲区中拷贝数据
            }
        }
        empty_buffers.release(1); //释放(创建)一个空的缓冲区资源，即可用空的缓冲区资源+1
        emit newValue(buffer_data, buffer_size, seq);
    }
    quit();
}
