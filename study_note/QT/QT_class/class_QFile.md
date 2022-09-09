# QFile

## 基本功能
QFile类提供了接口用来读写文本文件和二进制文件  
备注：QFile中有很多常用函数继承自QIODevice，如write()、close()等  
父类：QFileDevice  
子类：QTemporaryFile  


## 使用方式
1. 通过QFile可以获取到文件的一些基本信息，并对文件进行一些基本操作  
如果想获取更多的信息，如文件名、文件所在目录名等，请使用QFileInfo和QDir  

2. QFile提供的接口函数并不多，很多接口都是定义在父类QFileDevice和QIODevice中

3. 对文件进行数据读写时，经常使用QTextStream和QDataStream
但也可以调用继承自QIODevice中的read()、readLine()、write()等方法来实现读写  

4. QFile中的静态公共函数使用方便，推荐使用


## 注意事项
1. 不管在任何操作系统上，QFile的文件名路径中只支持"/"，不支持"\"  


## 构造函数
1. QFile::QFile(const QString &name, QObject \*parent)

2. QFile::QFile(QObject \*parent)

3. QFile::QFile(const QString &name)

4. QFile::QFile()


## 常用公共函数：对QIODevice中的open()方法进行重载
1. bool QFile::open(FILE \*fh, QIODevice::OpenMode mode, QFileDevice::FileHandleFlags handleFlags = DontCloseHandle)
fh参数为已经打开的文件的句柄  
注意：如果是在windows平台上，fh句柄必须是以二进制文件的格式打开  
handleFlags参数定义文件关闭时的方式  
注意：handleFlags参数仅对QFile有效，并不是对所有QIODevice有效  

2. bool QFile::open(int fd, QIODevice::OpenMode mode, QFileDevice::FileHandleFlags handleFlags = DontCloseHandle)
fd参数是一个文件描述符  


## 常用公共函数：获取文件信息
1. bool QFile::exists() const
判断文件是否存在  

2. QString QFile::symLinkTarget() const
返回一个文件链接/快捷方式所指向的源文件的绝对路径  


## 常用公共函数：对文件进行操作
1. void setFileName(const QString &name)
设置文件名字，名字中可以是相对路径，可以是绝对路径，也可以没有路径  
```
myfile.setFileName("E:/test.raw");
```

2. bool QFile::copy(const QString &newName)
把当前文件拷贝一份，新文件命名为newName  
注意：如果已经有一个名为newName的文件存在，则该文件不会被覆盖重写，函数执行失败，返回false  

3. bool QFile::link(const QString &linkName)
创建一个文件链接/快捷方式，返回是否创建成功  
备注：在windows系统上，一个合法的linkName的后缀必须是.lnk  

4. bool QFile::moveToTrash()
把文件放到回收站里，有的操作系统不支持回收站，会返回false  

5. bool QFile::remove()
删除文件，文件在删除之前必须是closed状态  

6. bool QFile::rename(const QString &newName)
文件重命名，文件在删除之前必须是closed状态  
注意：如果已经有一个名为newName的文件存在，则该文件不会被覆盖重写，函数执行失败，返回false  


## 公共静态函数
备注：这些公共静态函数和常用公共函数的功能基本类似，推荐使用静态函数更方便
1. [static] bool QFile::copy(const QString &fileName, const QString &newName)
把fileName文件拷贝一份，新文件命名为newName  
注意：如果已经有一个名为newName的文件存在，则该文件不会被覆盖重写，函数执行失败，返回false  

2. [static] bool QFile::exists(const QString &fileName)
判断文件是否存在  
注意：如果fileName是一个文件链接，指向了一个不存在的文件，则返回false  

3. [static] bool QFile::moveToTrash(const QString &fileName, QString \*pathInTrash = nullptr)
把文件放到回收站里  

4. [static] bool QFile::link(const QString &fileName, const QString &linkName)
给fileName文件创建一个文件链接/快捷方式linkName  

5. [static] bool QFile::remove(const QString &fileName)
删除文件  

6. [static] bool QFile::rename(const QString &oldName, const QString &newName)
文件重命名  

7. [static] bool QFile::resize(const QString &fileName, qint64 sz)
重新调整文件的大小为sz字节  
如果文件当前大小比sz更小，则新增加的字节都设置为0  
如果文件当前大小比sz更大，则多余的字节会被截断  

8. [static] QString QFile::symLinkTarget(const QString &fileName)
返回一个文件链接/快捷方式所指向的源文件的绝对路径  


