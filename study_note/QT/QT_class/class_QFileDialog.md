# QFileDialog

## 基本功能
QFileDialog提供了一个对话框，允许用户来选择本地文件和目录  
父类：QDialog  
子类：无  


## 代码示例
1. 使用公共静态函数快速获取用户选择的文件名
```
QString file_name = QFileDialog::getOpenFileName(this, "选择数据文件", "D:/1/data", "*.data");
```

2. 使用构造函数创建QFileDialog对象，设置各种属性之后再打开对话框
```
QFileDialog dialog(this, "QFileDialog测试", "D:/1", "*.pdf *.xlsx");
if(dialog.exec())
{
    QStringList files;
    files = dialog.selectedFiles();
    qDebug() << files;
}
```

3. 让用户一次选择多个文件
备注：通过按住ctrl键/shift键或者用鼠标圈中多个文件  
```
QFileDialog dialog(this, "QFileDialog测试", "D:/1", "*.pdf *.xlsx");
dialog.setFileMode(QFileDialog::ExistingFiles);//设置可以多选文件
if(dialog.exec())
{
    QStringList files;
    files = dialog.selectedFiles();
    qDebug() << files;
}
```

## 构造函数
1. QFileDialog::QFileDialog(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &directory = QString(), const QString &filter = QString())
caption参数设置对话框标题  
directory参数设置打开目录  
filter设置文件类型过滤器，多个过滤器之间用空格隔开  
```
QFileDialog dialog(this, "QFileDialog测试", "D:/1", "*.pdf *.xlsx");
```

2. QFileDialog::QFileDialog(QWidget \*parent, Qt::WindowFlags flags)


## 常用成员变量
1. acceptMode : AcceptMode
这个属性定义对话框的模式：打开文件或者保存文件，默认为打开文件  
1.1 QFileDialog::AcceptMode acceptMode() const
1.2 void setAcceptMode(QFileDialog::AcceptMode mode)

2. options : Options
这个属性设置很多选项，可以用来影响对话框的显示和使用，默认所有的选项都是禁用的  
备注：如果要设置这些选项，应该在对话框显示之前设置  
2.1 QFileDialog::Options options() const
2.2 void setOptions(QFileDialog::Options options)

3. defaultSuffix : QString
这个属性定义添加到文件名后面的后缀，通常用来设置文件的类型，例如".txt"  
3.1 QString defaultSuffix() const
3.2 void setDefaultSuffix(const QString &suffix)

4. supportedSchemes : QStringList
文件对话框应允许导航到的URL方案  
4.1 QStringList supportedSchemes() const
4.2 void setSupportedSchemes(const QStringList &schemes)

5. fileMode : FileMode
这个属性定义了对话框中的文件模式，默认值为QFileDialog::AnyFile  
文件模式是指显示在对话框中供用户选择的文件的类型和数量  
5.1 QFileDialog::FileMode fileMode() const
5.2 void setFileMode(QFileDialog::FileMode mode)

6. viewMode : ViewMode
这个属性定义对话框中文件和目录的显示方式，默认为QFileDialog::Detail  
6.1 QFileDialog::ViewMode viewMode() const
6.2 void setViewMode(QFileDialog::ViewMode mode)


## 常用公共函数：设置对话框的默认打开目录
1. void QFileDialog::setDirectory(const QString &directory)

2. void QFileDialog::setDirectory(const QDir &directory)

3. void QFileDialog::setDirectoryUrl(const QUrl &directory)

4. QDir QFileDialog::directory() const
返回当前对话框中正在展示的目录路径  

5. QUrl QFileDialog::directoryUrl() const
返回当前对话框中正在展示的目录URL  


## 常用公共函数：设置显示文件的过滤器
1. void QFileDialog::setFilter(QDir::Filters filters)

2. void QFileDialog::setMimeTypeFilters(const QStringList &filters)

3. void QFileDialog::setNameFilter(const QString &filter)
```
dialog.setNameFilter("All C++ files (*.cpp *.cc *.C *.cxx *.c++)");
dialog.setNameFilter("*.cpp *.cc *.C *.cxx *.c++");
```

4. void QFileDialog::setNameFilters(const QStringList &filters)
```
const QStringList filters({"Image files (*.png *.xpm *.jpg)",
                            "Text files (*.txt)",
                            "Any files (*)"
                           });
```

5. QDir::Filters QFileDialog::filter() const

6. QStringList QFileDialog::mimeTypeFilters() const

7. QStringList QFileDialog::nameFilters() const


## 常用公共函数：获取用户选择的文件
1. QStringList QFileDialog::selectedFiles() const
以列表的形式返回用户选择的文件的绝对路径  


## 常用公共函数：其他
1. void QFileDialog::selectFile(const QString &filename)
在文件对话框中选择指定的文件  


## 常用信号函数


## 公共静态函数
1. [static] QString QFileDialog::getExistingDirectory(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &dir = QString(), QFileDialog::Options options = ShowDirsOnly)

2. [static] QUrl QFileDialog::getExistingDirectoryUrl(QWidget \*parent = nullptr, const QString &caption = QString(), const QUrl &dir = QUrl(), QFileDialog::Options options = ShowDirsOnly, const QStringList &supportedSchemes = QStringList())

3. [static] void QFileDialog::getOpenFileContent(const QString &nameFilter, const std::function<void (const QString &, const QByteArray &)> &fileOpenCompleted)

4. [static] QString QFileDialog::getOpenFileName(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &dir = QString(), const QString &filter = QString(), QString \*selectedFilter = nullptr, QFileDialog::Options options = Options())
获取到打开文件的名字
```
QString file_name = QFileDialog::getOpenFileName(this, "选择数据文件", "D:/1/data", "*.data");
```

5. [static] QStringList QFileDialog::getOpenFileNames(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &dir = QString(), const QString &filter = QString(), QString \*selectedFilter = nullptr, QFileDialog::Options options = Options())

6. [static] QUrl QFileDialog::getOpenFileUrl(QWidget \*parent = nullptr, const QString &caption = QString(), const QUrl &dir = QUrl(), const QString &filter = QString(), QString \*selectedFilter = nullptr, QFileDialog::Options options = Options(), const QStringList &supportedSchemes = QStringList())

7. [static] QUrl QFileDialog::getOpenFileUrl(QWidget \*parent = nullptr, const QString &caption = QString(), const QUrl &dir = QUrl(), const QString &filter = QString(), QString \*selectedFilter = nullptr, QFileDialog::Options options = Options(), const QStringList &supportedSchemes = QStringList())

8. [static] QString QFileDialog::getSaveFileName(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &dir = QString(), const QString &filter = QString(), QString \*selectedFilter = nullptr, QFileDialog::Options options = Options())

9. [static] QUrl QFileDialog::getSaveFileUrl(QWidget \*parent = nullptr, const QString &caption = QString(), const QUrl &dir = QUrl(), const QString &filter = QString(), QString \*selectedFilter = nullptr, QFileDialog::Options options = Options(), const QStringList &supportedSchemes = QStringList())

10. [static] void QFileDialog::saveFileContent(const QByteArray &fileContent, const QString &fileNameHint = QString())


## enum QFileDialog::AcceptMode
```
Constant 					Value
QFileDialog::AcceptOpen 	0
QFileDialog::AcceptSave 	1
```


## enum QFileDialog::DialogLabel
```
Constant 					Value
QFileDialog::LookIn 		0
QFileDialog::FileName 		1
QFileDialog::FileType 		2
QFileDialog::Accept 		3
QFileDialog::Reject 		4
```


## enum QFileDialog::FileMode
这个集合中包含了在对话框中显示出的文件的类型  
```
Constant 						Value 	Description
QFileDialog::AnyFile 			0 		实测显示所有目录和文件
The name of a file, whether it exists or not.
QFileDialog::ExistingFile 		1 		实测显示所有目录和文件，用户一次只能选择单个文件
The name of a single existing file.
QFileDialog::Directory 			2 		实测只显示所有目录，不显示文件
The name of a directory. Both files and directories are displayed. However, the native Windows file dialog does not support displaying files in the directory chooser.
QFileDialog::ExistingFiles 		3 		实测显示所有目录和文件，用户一次可以选择多个文件
The names of zero or more existing files.
```


## enum QFileDialog::ViewMode
这个集合中包含了在对话框中显示出的文件的信息  
备注：实际测试，两种模式显示效果好像一样  
```
Constant 				Value 	Description
QFileDialog::Detail 	0 		显示文件的图标、名称、以及详细信息
Displays an icon, a name, and details for each item in the directory.
QFileDialog::List 		1 		只显示文件的图标、名称
```
