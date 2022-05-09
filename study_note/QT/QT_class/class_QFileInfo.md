# QFileInfo

## 基本功能
QFileInfo提供了依赖于操作系统的文件信息  
父类：无  
子类：无  


## 构造函数
1. QFileInfo::QFileInfo(const QFileInfo &fileinfo)

2. QFileInfo::QFileInfo(const QDir &dir, const QString &file)
如果dir参数包含相对路径，则QFileInfo也包含相对路径  
如果file参数是一个绝对路径，则会忽略dir参数中的路径，以file参数为准  

3. QFileInfo::QFileInfo(const QFile &file)

4. QFileInfo::QFileInfo(const QString &file)
file参数中可以包含相对路径或绝对路径  
```
QFileInfo fileinfo("D:/file.text");
```

5. QFileInfo::QFileInfo()


## 常用公共函数：获取文件的基本信息
1. qint64 QFileInfo::size() const
返回文件的大小  


## 常用公共函数：判断文件的基本信息
1. bool QFileInfo::exists() const
判断文件是否存在  
备注：如果文件是一个链接/快捷方式，且原文件不存在，则返回false  

2. bool QFileInfo::isAbsolute() const
判断是否是绝对路径  

3. bool QFileInfo::isRelative() const
判断是否是相对路径  

4. bool QFileInfo::isDir() const
判断是否是目录或目录的快捷方式  

5. bool QFileInfo::isFile() const

6. bool QFileInfo::isHidden() const

7. bool QFileInfo::isExecutable() const

8. bool QFileInfo::isReadable() const

9. bool QFileInfo::isWritable() const


## 常用公共函数：获取文件路径信息
1. QDir QFileInfo::absoluteDir() const

2. QString QFileInfo::absoluteFilePath() const
返回文件的绝对路径，包含文件本身  
```
"D:/file.text"
```

3. QString QFileInfo::absolutePath() const
返回文件的绝对路径，不包含文件本身  
```
"D:/"
```

4. QString QFileInfo::canonicalPath() const
返回文件的标准路径，不包含文件本身  
```
"D:/"
```

5. QString QFileInfo::baseName() const
返回文件名，不包含第一个.开始的文件后缀名  
```
QFileInfo fi("/tmp/archive.tar.gz");
QString base = fi.baseName();  // base = "archive"
```

6. QString QFileInfo::completeBaseName() const
返回文件名，不包含最后一个.的文件后缀名  
```
QFileInfo fi("/tmp/archive.tar.gz");
QString base = fi.completeBaseName();  // base = "archive.tar"
```

7. QString QFileInfo::suffix() const
返回文件的后缀名，后缀名从最后一个.开始，一直到最后  
```
QFileInfo fi("/tmp/archive.tar.gz");
QString ext = fi.suffix();  // ext = "gz"
```

8. QString QFileInfo::completeSuffix() const
返回文件的后缀名，后缀名从第一个.开始，一直到最后  
```
QFileInfo fi("/tmp/archive.tar.gz");
QString ext = fi.completeSuffix();  // ext = "tar.gz"
```

9. QString QFileInfo::fileName() const
```
"file.text"
```

10. QString QFileInfo::filePath() const
```
"D:/file.text"
```

11. QDir QFileInfo::dir() const
返回父目录，即文件所在目录  


## 常用公共函数：获取文件的时间信息
备注：用QFileDevice::fileTime()方法也可以获得下面的时间信息  
1. QDateTime QFileInfo::birthTime() const
获取文件的创建时间  

2. QDateTime QFileInfo::fileTime(QFile::FileTime time) const
获取文件的指定时间信息

3. QDateTime QFileInfo::lastModified() const

4. QDateTime QFileInfo::lastRead() const

5. QDateTime QFileInfo::metadataChangeTime() const


## 静态公共函数
1. [static] bool QFileInfo::exists(const QString &file)
判断文件是否存在  
备注：如果文件是一个链接/快捷方式，且原文件不存在，则返回false  