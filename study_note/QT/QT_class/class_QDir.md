# QDir

## 基本功能
QDir用来访问目录结构以及目录中的内容，也用来访问Qt资源系统  
备注：文件路径中使用"/"，而不是使用"\"  
父类：无  
子类：无  


## 代码示例
1. 构造一个QDir对象，输出目录中的文件和子目录
```
QDir *dir = new QDir("D:/1");
QStringList name_filter;
name_filter << "*.pdf" << "*.xlsx" << "*.png";
if(dir -> exists())
{
    qDebug() << dir -> count();
    qDebug() << dir -> entryList(name_filter);
    qDebug() << dir -> entryInfoList();
}
```


## 构造函数
1. QDir::QDir(const QString &path, const QString &nameFilter, QDir::SortFlags sort = SortFlags(Name \| IgnoreCase), QDir::Filters filters = AllEntries)
如果path是一个空字符串，则QDir会认为是"."(当前目录)  
如果nameFilter是一个空字符串，则QDir会认为是"\*"(匹配所有文件)  
注意：path不一定必须是一个实际存在的合法路径  

2. QDir::QDir(const QString &path = QString())
如果path是一个空字符串，则QDir会认为是"."(当前目录)  
注意：path不一定必须是一个实际存在的合法路径  

3. QDir::QDir(const QDir &dir)


## 常用公共函数：目录的基本信息
1. uint QDir::count() const
返回当前目录中子目录和文件的总数  

2. bool QDir::exists(const QString &name) const
判断文件是否存在  
除非name是一个绝对路径，否则默认是当前目录中的文件  

3. bool QDir::exists() const
重载函数  

4. bool QDir::isAbsolute() const
判断是否是绝对路径  

5. bool QDir::isRelative() const
判断是否是相对路径  

6. bool QDir::isRoot() const
判断是否是根路径  

7. bool QDir::isEmpty(QDir::Filters filters = Filters(AllEntries | NoDotAndDotDot)) const
判断目录是否为空  

8. bool QDir::isReadable() const
判断目录是否有权限打开，这个方法不一定准确  


## 常用公共函数：获取目录的路径信息
1. QString QDir::dirName() const
返回目录本身的名字，不包含前面的路径  

2. QString QDir::absoluteFilePath(const QString &fileName) const
返回目录中文件的绝对路径(不检查该文件是否真的存在于该目录)  
绝对路径中多余的分割符或'.'或'..'不会被删除  

3. QString QDir::filePath(const QString &fileName) const
返回目录中的文件路径(不检查该文件是否真的存在于该目录)  
如果QDir是相对路径，则返回值也是相对路径  
绝对路径中多余的分割符或'.'或'..'不会被删除  

4. QString QDir::absolutePath() const
返回目录的绝对路径  
绝对路径以'/'为开头，路径中可能包括符号链接，但一定不包含多余的分割符或'.'或'..'  

5. QString QDir::canonicalPath() const
返回目录的标准路径  
如果标准路径不存在，则返回空字符串  
标准路径中不包括符号链接，也不包含多余的分割符或'.'或'..'  
在不支持符号链接的操作系统中，标准路径和绝对路径相同  

6. QString QDir::relativeFilePath(const QString &fileName) const


## 设置目录的基本属性
1. void QDir::setPath(const QString &path)
设置QDir的当前目录  

2. bool QDir::makeAbsolute()
把当前路径转换为绝对路径  
如果当前路径已经是绝对路径，则不做任何处理  


## 常用公共函数：设置过滤器
1. QDir::Filters QDir::filter() const

2. void QDir::setFilter(QDir::Filters filters)
按文件类型设置过滤器  
过滤器针对entryList()方法和entryInfoList()方法生效  

3. QStringList QDir::nameFilters() const

4. void QDir::setNameFilters(const QStringList &nameFilters)
按文件名设置过滤器  
过滤器针对entryList()方法和entryInfoList()方法生效  


## 常用公共函数：设置排序器
1. QDir::SortFlags QDir::sorting() const

2. void QDir::setSorting(QDir::SortFlags sort)


## 常用公共函数：获取目录中的文件和子目录
1. QStringList entryList(const QStringList &nameFilters, QDir::Filters filters = NoFilter, QDir::SortFlags sort = NoSort) const
以字符串列表的形式返回目录中所有的文件和子目录  
可以不写任何函数参数  
```
qDebug() << dir -> entryList();
```
也可以只设置第一个函数参数  
```
QStringList name_filter;
name_filter << "*.pdf" << "*.xlsx";
qDebug() << dir -> entryList(name_filter);
```

2. QStringList entryList(QDir::Filters filters = NoFilter, QDir::SortFlags sort = NoSort) const
重载函数  

3. QFileInfoList QDir::entryInfoList(const QStringList &nameFilters, QDir::Filters filters = NoFilter, QDir::SortFlags sort = NoSort) const
以QFileInfo列表的形式返回目录中所有的文件和子目录  

4. QFileInfoList QDir::entryInfoList(QDir::Filters filters = NoFilter, QDir::SortFlags sort = NoSort) const
重载函数


## 常用公共函数：切换当前路径
1. bool QDir::cd(const QString &dirName)
切换到指定目录，如果新目录不存在，则返回false  

2. bool QDir::cdUp()
切换到上一级目录  

3. void QDir::swap(QDir &other)


## 常用公共函数：1.新建目录
1. bool QDir::mkdir(const QString &dirName) const
在当前目录中创建子目录dirName，如果子目录已经存在，则返回false  
```
dir -> mkdir("subdir");
```

2. bool QDir::mkpath(const QString &dirPath) const
创建一条路径dirPath，如果有必要，会创建出多层目录  
```
dir -> mkpath("a/b/c");
```


## 常用公共函数：2.删除目录/文件
1. bool QDir::remove(const QString &fileName)
删除指定文件

2. bool QDir::removeRecursively()
删除当前目录，以及目录中的文件和子目录  
如果目录或其中的文件无法被删除，方法会尽可能多的删除其他文件和子目录，然后返回fase  
注意：实际测试，目录及目录中的内容都是彻底删除，在回收站中也找不到，慎重使用  

3. bool QDir::rmdir(const QString &dirName) const
删除指定目录，dirName必须是一个空目录，否则删除失败  

4. bool QDir::rmpath(const QString &dirPath) const
删除多层路径，路径中的父目录都会被删除，目录必须都为空，与mkpath()刚好相反  


## 常用公共函数：3.重命名目录/文件
1. bool QDir::rename(const QString &oldName, const QString &newName)
对文件或目录进行重命名  


## 公共静态函数
1. [static] QDir QDir::current()
返回应用程序的当前工作目录  

2. [static] QString QDir::currentPath()
以字符串的形式返回应用程序的当前工作目录的绝对路径  

3. [static] QDir QDir::home()
返回用户的home目录

4. [static] QString QDir::homePath()
以字符串的形式返回用户的home目录的绝对路径  
在windows系统中，用户的home目录一般是：  
```
C:/Documents and Settings/Username
```

5. [static] bool QDir::isAbsolutePath(const QString &path)

6. [static] bool QDir::isRelativePath(const QString &path)

7. [static] QChar QDir::separator()
返回目录路径中的分隔符  
在Unix系统中，分隔符一般为'/'，在Windows系统中，分隔符一般为'\'  
备注：一般不需要用这个函数来构建路径，即使使用了'/'，Qt也会翻译为正确的分隔符  


## enum QDir::Filter
这个集合中包含了所有QDir支持的文件过滤器选项  
```
Constant 					Value 		Description
QDir::Dirs 					0x001 		列出匹配过滤器的所有目录
QDir::AllDirs 				0x400 		列出所有目录，不使用过滤器
QDir::Files 				0x002 		列出所有文件
QDir::Drives 				0x004 		列出所有磁盘驱动(在Unix系统中忽略)
QDir::NoSymLinks 			0x008 		不要列出链接符(在不支持链接符的系统中忽略)
QDir::NoDotAndDotDot 		NoDot | NoDotDot 	不要列出特殊目录'.'和'..'
QDir::NoDot 				0x2000 		不要列出特殊目录'.'
QDir::NoDotDot 				0x4000 		不要列出特殊目录'..'
QDir::AllEntries 			Dirs | Files | Drives 	列出目录、文件、磁盘驱动、链接符
QDir::Readable 				0x010 		列出程序具有读取权限的所有文件
QDir::Writable 				0x020 		列出程序具有写入权限的所有文件
QDir::Executable 			0x040 		列出程序具有执行权限的所有文件
QDir::Modified 				0x080 		列出被修改的文件(在Unix系统中忽略)
QDir::Hidden 				0x100 		列出隐藏文件(在Unix系统中，隐藏文件以'.'开头)
QDir::System 				0x200 		列出系统文件(windows系统中的.lnk文件)
QDir::CaseSensitive 		0x800 		设置过滤器区分大小写
```


## enum QDir::SortFlag
这个集合包含了QDir中文件目录的排序方式  
前四个选项一次只能选择一个  
```
Constant 			Value 		Description
QDir::Name 			0x00 		按文件名排序
QDir::Time 			0x01 		按修改时间排序
QDir::Size 			0x02 		按文件大小排序
QDir::Type 			0x80 		按文件类型(扩展名)排序
QDir::Unsorted 		0x03 		不排序
QDir::NoSort 		-1 			不排序，按默认顺序
QDir::DirsFirst 	0x04 		先显示目录，再显示文件
QDir::DirsLast 		0x20 		先显示文件，再显示目录
QDir::Reversed 		0x08 		逆序
QDir::IgnoreCase 	0x10 		排序时忽略大小写
QDir::LocaleAware 	0x40 		使用当前配置适当的排序
```