# QFileDevice

## 基本功能
QFileDevice是Qt5新增加的类，提供了有关文件操作的通用实现  
父类：QIODevice  
子类：QFile、QSaveFile  


## 构造函数
注意：QFileDevice没有提供构造函数，不能直接实例化，成员函数都是在子类中使用的  


## 常用公共函数：获取文件信息
1. QFileDevice::FileError QFileDevice::error() const
获取文件操作过程中的报错信息，详见enum QFileDevice::FileError  

2. [virtual] QString QFileDevice::fileName() const
返回文件名，这里的文件名是构造函数或setFileName()中设置的名称  
文件名中可能会包含文件路径，也可能不包含，具体取决于之前的设置  

3. QDateTime QFileDevice::fileTime(QFileDevice::FileTime time) const
获取文件的各种时间信息  
time参数取值详见enum QFileDevice::FileTime  

4. int QFileDevice::handle() const
返回文件的句柄，如果文件没有打开，或者打开报错，则返回-1  
返回结果是一个小的正整数，适合用于C库函数，如fdopen()和fcntl()  

5. [virtual] QFileDevice::Permissions QFileDevice::permissions() const
获取文件的权限信息，详见enum QFileDevice::Permission  


## 常用公共函数：对文件进行操作
1. bool QFileDevice::flush()
把缓冲区中的所有数据都立即写入到文件设备中，返回是否成功  

2. [virtual] bool QFileDevice::resize(qint64 sz)
重新调整文件的大小为sz字节  
如果文件当前大小比sz更小，则新增加的字节都设置为0  
如果文件当前大小比sz更大，则多余的字节会被截断  

3. bool QFileDevice::setFileTime(const QDateTime &newDate, QFileDevice::FileTime fileTime)
设置文件的各种时间信息  
注意：设置之前，文件必须是打开状态的  

4. [virtual] bool QFileDevice::setPermissions(QFileDevice::Permissions permissions)
设置文件的权限信息  

5. void QFileDevice::unsetError()
取消文件报错，把文件的报错状态设置为QFileDevice::NoError  


## enum QFileDevice::FileTime
这个集合中包含了文件的时间信息类型  
```
Constant 							Value 	Description
QFileDevice::FileAccessTime			0 		文件最近被访问的时间
QFileDevice::FileBirthTime 			1 		文件的创建时间(Unix系统可能不支持)
QFileDevice::FileMetadataChangeTime 2 		文件的元数据的最近修改时间
QFileDevice::FileModificationTime   3 		文件最近的修改时间
```


## enum QFileDevice::Permission
这个集合包含了文件的权限状态  
在不同的操作系统上，文件权限都所不同  
```
Constant 					Value 		Description
QFileDevice::ReadOwner		0x4000		The file is readable by the owner of the file.
QFileDevice::WriteOwner		0x2000		The file is writable by the owner of the file.
QFileDevice::ExeOwner		0x1000		The file is executable by the owner of the file.
QFileDevice::ReadUser		0x0400		The file is readable by the user.
QFileDevice::WriteUser		0x0200		The file is writable by the user.
QFileDevice::ExeUser		0x0100		The file is executable by the user.
QFileDevice::ReadGroup		0x0040		The file is readable by the group.
QFileDevice::WriteGroup		0x0020		The file is writable by the group.
QFileDevice::ExeGroup		0x0010		The file is executable by the group.
QFileDevice::ReadOther		0x0004		The file is readable by anyone.
QFileDevice::WriteOther		0x0002		The file is writable by anyone.
QFileDevice::ExeOther		0x0001		The file is executable by anyone.
```
在NTFS文件系统上，出于性能考虑，文件所有权和权限检查默认都被禁用了  
如果要启用，要在代码中添加以下行：  
```
extern Q_CORE_EXPORT int qt_ntfs_permission_lookup;
```


## enum QFileDevice::FileError
这个集合包含了文件处理过程中的所有报错  
```
Constant 						Value 	Description
QFileDevice::NoError			0 		No error occurred.
QFileDevice::ReadError			1 		An error occurred when reading from the file.
QFileDevice::WriteError			2 		An error occurred when writing to the file.
QFileDevice::FatalError			3 		A fatal error occurred.
QFileDevice::ResourceError		4 		Out of resources (e.g., too many open files, out of memory, etc.)
QFileDevice::OpenError			5 		The file could not be opened.
QFileDevice::AbortError			6 		The operation was aborted.
QFileDevice::TimeOutError		7 		A timeout occurred.
QFileDevice::UnspecifiedError	8 		An unspecified error		 occurred.
QFileDevice::RemoveError		9 		The file could not be removed.
QFileDevice::RenameError		10 		The file could not be renamed.
QFileDevice::PositionError		11 		The position in the file could not be changed.
QFileDevice::ResizeError		12 		The file could not be resized.
QFileDevice::PermissionsError	13 		The file could not be accessed.
QFileDevice::CopyError			14 		The file could not be copied.
```