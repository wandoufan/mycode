# 单例模式 Singleton Pattern

## 基本概念
在有的场景下，对某些类要求最多只能创建一个实例化对象，这样的类称为单例类


## 特点
1. 单例类最多只能有一个实例化对象
2. 该单例对象必须由单例类自行创建
3. 单例类对外提供一个访问其唯一实例化对象的全局访问点


## 优点
1. 在内存中只有一个实例化对象，节约了内存资源，尤其是减少了频繁创建和销毁实例化对象的内存开销
2. 在内存中只有一个实例化对象，保证了数据内容的一致性，在代码的不同地方访问到的都是同一个实例化对象


## 缺点
单例类没有接口，不能继承，与单一职责原则冲突


## 应用场景
1. 在Windows系统中只能同时打开一个任务管理器，避免打开多个窗口时浪费内存资源，或者窗口显示内容不一致
2. 定义了一个校长类、老师类、学生类，但对于校长类只能实例化出一个对象
3. 一些设备管理器常常设计为单例模式，比如一个电脑有两台打印机，在输出的时候就要处理不能两台打印机打印同一个文件
4. 一些数据不用每次变化时都往数据库进行读写，可以先存入到单例对象中，最后再从单例对象中写入数据库


## 单例类的实现要求
1. 将类的构造函数声明为Private的，以防止外界创建单例类的实例化对象
2. 使用类的私有静态指针变量指向类的唯一实例化对象
3. 使用一个共有的静态方法获取该实例化对象


## 单例模式的实现方式：1. 线程不安全的懒汉式(Lazy Singleton)
1. 概念
懒汉式就是在需要使用的时候才去进行实例化，单例类在第一次被调用时才实例化出类对象
2. 特点
实现方式简单，但没有同步锁，在多线程的情况下可能会产生线程安全问题
例如，当唯一的实例化对象还没有被创建时，多个线程同时去调用实例化对象
多个线程会同时检测到实例化对象还不存在，从而各自创建出一个实例化对象
3. 代码示例
头文件
```
class Singleton
{
public:
    //外部获取唯一实例化对象的接口
    static Singleton *getInstance();

private:
    //把所有的构造函数都声明为Private的
    Singleton();//正常构造函数
    Singleton(const Singleton&);//赋值构造函数
    Singleton& operator=(const Singleton&);//拷贝构造函数
    //用私有静态指针指向唯一的实例化对象
    static Singleton *m_instance;
};
```
源文件
```
//静态成员变量的初始化要放在类外面
Singleton *Singleton::m_instance = nullptr;//类指针先设置为一个空指针

//先判断类指针是否为空，如果为空就先实例化类对象
Singleton *Singleton::getInstance()
{
    if(m_instance == nullptr)
    {
        m_instance = new Singleton;
    }
    return m_instance;
}

Singleton::Singleton()
{

}

Singleton::Singleton(const Singleton &)
{

}

Singleton &Singleton::operator=(const Singleton &)
{

}
```


## 单例模式的实现方式：2. 线程安全的懒汉式(Lazy Singleton)
1. 说明
懒汉式单例类的线程安全问题可以通过加锁来解决实现，但加锁会影响效率，当线程很多时，也可能会造成线程阻塞
2. 代码示例
头文件
```
class Singleton
{
public:
    //外部获取唯一实例化对象的接口
    static Singleton *getInstance();

private:
    //把所有的构造函数都声明为Private的
    Singleton();//正常构造
    Singleton(const Singleton&);//赋值构造
    Singleton& operator=(const Singleton&);//拷贝构造
    //用私有静态指针指向唯一的实例化对象
    static Singleton *m_instance;
    //在多线程中解决线程安全问题的锁
    static QMutex *m_mutex;
};
```
源文件
```
//静态成员变量的初始化要放在类外面
Singleton *Singleton::m_instance = nullptr;//类指针先设置为一个空指针
QMutex *Singleton::m_mutex = new QMutex;

//先判断类指针是否为空，如果为空就先实例化类对象
Singleton *Singleton::getInstance()
{
    m_mutex -> lock();//添加互斥锁
    if(m_instance == nullptr)
    {
        m_instance = new Singleton;
    }
    m_mutex -> unlock();
    return m_instance;
}

Singleton::Singleton()
{

}

Singleton::Singleton(const Singleton &)
{

}

Singleton &Singleton::operator=(const Singleton &)
{

}
```


## 单例模式的实现方式：3. 饿汉式(Eager Singleton)
1. 概念
饿汉式就是不管是否能用到，在程序一开始运行时就立刻实例化出类对象
2. 特点
这种方式会在一开始就获得唯一一个实例化对象，但这些对象不一定每次都用到，这样就造成了内存空间的占用和浪费
3. 代码示例
头文件
```
class Singleton
{
public:
    //外部获取唯一实例化对象的接口
    static Singleton *getInstance();

private:
    //把所有的构造函数都声明为Private的
    Singleton();//正常构造
    Singleton(const Singleton&);//赋值构造
    Singleton& operator=(const Singleton&);//拷贝构造
    //用私有静态指针指向唯一的实例化对象
    static Singleton *m_instance;
};
```
源文件
```
//静态成员变量的初始化要放在类外面
Singleton *Singleton::m_instance = new Singleton;//类指针直接指向唯一一个类对象

Singleton *Singleton::getInstance()
{
    return m_instance;
}

Singleton::Singleton()
{

}

Singleton::Singleton(const Singleton &)
{

}

Singleton &Singleton::operator=(const Singleton &)
{

}
```