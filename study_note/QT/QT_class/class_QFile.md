# QFile

## 基本功能
QFile类提供了接口用来读文件和写文件  
QFile可以单独使用，也经常和QTextStream或QDataStream搭配使用  
```
继承关系
QObject - QIODevice - QFile - QTemporaryFile
```


## 代码示例
```
QFile file("in.txt");
if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
	return;

while (!file.atEnd())
{
	QByteArray line = file.readLine();
	process_line(line);
}
```

## 构造函数
1. QFile::QFile(const QString &name, QObject \*parent)

2. QFile::QFile(QObject \*parent)

3. QFile::QFile(const QString &name)

4. QFile::QFile()


## 常用公共函数
备注：QFile中有很多常用函数继承自QIODevice，如write()、close()等  
1. void setFileName(const QString &name)
设置文件名字，名字中可以是相对路径，可以是绝对路径，也可以没有路径  
注意：文件名路径时只支持"/"，不支持"\"  
```
myfile.setFileName("E:/test.raw");
```

2. bool QFile::copy(const QString &newName)
把当前文件拷贝一份，新文件命名为newName  
注意：如果已经有一个名为newName的文件存在，则该文件不会被覆盖重写，函数执行失败，返回false  

3. bool QFile::exists() const
判断文件是否存在  

4. bool QFile::moveToTrash()
把文件放到回收站里，有的操作系统不支持回收站，会返回false  

5. bool QFileDevice::flush()
冲洗掉文件缓冲区的所有数据，返回返回ture或false  

6. bool QFile::remove()
删除文件  

7. bool QFile::rename(const QString &newName)
文件重命名  


## 公共静态函数
1. [static] bool QFile::copy(const QString &fileName, const QString &newName)
把fileName文件拷贝一份，新文件命名为newName  
注意：如果已经有一个名为newName的文件存在，则该文件不会被覆盖重写，函数执行失败，返回false  

2. [static] bool QFile::exists(const QString &fileName)
判断文件是否存在  
注意：如果fileName是一个文件链接，指向了一个不存在的文件，则返回false  

3. [static] bool QFile::moveToTrash(const QString &fileName, QString \*pathInTrash = nullptr)
把文件放到回收站里  

4. [static] bool QFile::link(const QString &fileName, const QString &linkName)
给fileName文件创建一个链接linkName  

5. [static] bool QFile::remove(const QString &fileName)
删除文件  

6. [static] bool QFile::rename(const QString &oldName, const QString &newName)
文件重命名  