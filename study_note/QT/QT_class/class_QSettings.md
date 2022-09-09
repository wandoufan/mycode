# QSettings

## 基本功能
QSettings提供了依赖于操作系统平台的永久的应用程序设置，也就是给程序实现配置文件相关的功能  
备注：QSettings中所有的函数都是可重入的  
备注：QSettings中所有的函数都是线程安全的  
父类：QObject  
子类：无  


## 详细功能
用户通常希望应用程序可以记住它的一些配置信息，如窗口的尺寸、位置等  
在Windows系统中，这些信息通常存储在注册表中  
在MacOS和iOS系统中，这些信息通常存储在属性列表中  
在Unix系统中，由于缺乏标准，很多应用程序都使用ini文件格式  
QSettings可以帮助存储程序配置，同时也支持自定义的存储格式  
QSettings的API是基于QVariant，允许保存大部分基于数值型的数据，例如：QString、QRect、QImage等  
如果只是需要临时把配置存放在内存中，建议使用QMap<QString, QVariant>来替代QSettings  


## 使用方式
当创建一个QSettings对象时，必须提供公司/组织的名称，以及应用程序的名称  
QSettings对象可以使用栈内存，也可以使用堆内存  
如果在应用程序中多次用到QSettings，可以先使用下面方法来指明组织名称和程序名称
```
QCoreApplication::setOrganizationName()
QCoreApplication::setApplicationName()
```
然后再使用默认的QSettings构造函数来获取对象，例如：  
```
QCoreApplication::setOrganizationName("MySoft");
QCoreApplication::setOrganizationDomain("mysoft.com");
QCoreApplication::setApplicationName("Star Runner");
...
QSettings settings;
```


## 关于key和分割符的语法规则
配置中的key可以包含任何Unicode符号  
注意：在windows注册表以及ini文件中的key是不区分大小写的  
注意：基于macOS和iOS的CFPreferences API是区分大小写的  
为了解决这些跨平台的问题，需要遵循以下规则：  
1. 总是把同一个key用相同的大小写表示
例如：一个地方中把key写成了"text fonts"，其他地方就不要用"Text Fonts"来表示这个key  
2. 避免多个key的名字除了大小写都相同
例如：一个key命名为了"MainWindow"，就不要把另一个key命名为"mainwindow"  
3. 不要在key名称的内部中使用'/'或'\'，这个符号是作为key和子key的分割符
在windows系统上，'\'会被QSettings转换为'/'，因此两个符号在windows系统上是相同的  

可以在分层次的key中使用'/'来作为分割符，类似于Unix文件的路径，例如：  
```
settings.setValue("mainwindow/size", win->size());
settings.setValue("mainwindow/fullScreen", win->isFullScreen());
settings.setValue("outputpanel/visible", panel->isVisible());
```


## 代码示例
1. 直接向ini文件中写入配置
在一个txt文本中直接写入配置内容，然后改为ini格式，内容示例如下：
```
[LICENSE]
LIC_MODE=0
[time]
basetime=500
variabletime=1000
[CONTROLOPA]
FORMAT=OPA
```

2. 使用QSettings向ini文件中写入配置
示例1：写入几组简单的key-value
备注：在不设置节名的情况下，实际测试，默认节名为[General]
```
QSettings *my_ini;
my_ini = new QSettings("D:/shake_COM.ini", QSettings::IniFormat);
my_ini -> setValue("shake1", "COM3");
my_ini -> setValue("shake2", "COM4");
my_ini -> setValue("shake3", "COM5");
my_ini -> setValue("shake4", "COM6");
```
```
[General]
shake1=COM3
shake2=COM4
shake3=COM5
shake4=COM6
```
示例2：按不同的节来设置key-value
```
QSettings *my_ini;
my_ini = new QSettings("D:/shake_COM.ini", QSettings::IniFormat);
my_ini -> beginGroup("ID");
my_ini -> setValue("ID1", 123);
my_ini -> setValue("ID2", 234);
my_ini -> endGroup();
my_ini -> beginGroup("Name");
my_ini -> setValue("name1", "zhang");
my_ini -> setValue("name2", "wang");
my_ini -> endGroup();
my_ini -> beginGroup("Score");
my_ini -> setValue("score1", 80.5);
my_ini -> setValue("score2", 90.5);
my_ini -> endGroup();
```
```
[ID]
ID1=123
ID2=234

[Name]
name1=zhang
name2=wang

[Score]
score1=80.5
score2=90.5
```
示例3：实际测试，如果key或value中带有中文，则ini文件打开查看会是一堆编码
```
my_ini -> setValue("振动1", "端口3");
my_ini -> setValue("振动2", "端口4");
my_ini -> setValue("振动3", "端口5");
my_ini -> setValue("振动4", "端口6");
```
```
[General]
%U632F%U52A81=\x7aef\x53e3\x33
%U632F%U52A82=\x7aef\x53e3\x34
%U632F%U52A83=\x7aef\x53e3\x35
%U632F%U52A84=\x7aef\x53e3\x36
```

3. 使用QSettings从ini文件中读取配置
```
QSettings *my_ini;
my_ini = new QSettings("D:/shake_COM.ini", QSettings::IniFormat);
int ID1 = my_ini -> value("ID/ID1").toInt();
int ID2 = my_ini -> value("ID/ID2").toInt();
QString name1 = my_ini -> value("Name/name1").toString();
QString name2 = my_ini -> value("Name/name2").toString();
float score1 = my_ini -> value("Score/score1").toFloat();
float score2 = my_ini -> value("Score/score2").toFloat();
```


## 构造函数
1. QSettings::QSettings(QSettings::Scope scope, QObject \*parent = nullptr)

2. QSettings::QSettings(QObject \*parent = nullptr)

3. QSettings::QSettings(const QString &fileName, QSettings::Format format, QObject \*parent = nullptr)
这是目前最常用的一个构造函数  
```
my_ini = new QSettings("D:/shake_COM.ini", QSettings::IniFormat);
```

4. QSettings::QSettings(QSettings::Format format, QSettings::Scope scope, const QString &organization, const QString &application = QString(), QObject \*parent = nullptr)

5. QSettings::QSettings(QSettings::Scope scope, const QString &organization, const QString &application = QString(), QObject \*parent = nullptr)

6. QSettings::QSettings(const QString &organization, const QString &application = QString(), QObject \*parent = nullptr)
第一个参数为公司/组织的名称  
第二个参数为应用程序的名称  
```
QSettings settings("MySoft", "Star Runner");
```


## 常用公共函数：获取基本信息
1. QSettings::Scope QSettings::scope() const

2. QString QSettings::applicationName() constQString QSettings::applicationName() const

3. QString QSettings::organizationName() const

4. QString QSettings::fileName() const
返回配置文件的保存路径  
在windows系统上，如果格式是QSettings::NativeFormat，则返回值是系统注册表的路径，不是文件路径  

5. bool QSettings::isWritable() const
判断配置文件是否是可写的  
例如，当配置文件是只读文件时，这个函数就会返回false  
备注：这个函数并不一定准确，因为文件的读写权限随时可能被更改  


## 常用公共函数：对配置组进行设置
关于组的说明：
这里的'组'的概念应该是当前QSettings对象中所有的配置  
默认情况下，没有设置任何组  
组一般用来给所有的配置增加相同的前缀，避免重复写前缀带来的麻烦  
1. QString QSettings::group() const
返回当前的组  

2. void QSettings::beginGroup(const QString &prefix)
给当前的组增加前缀  
```
settings.beginGroup("mainwindow");
settings.setValue("size", win->size());
settings.setValue("fullScreen", win->isFullScreen());
settings.endGroup();

settings.beginGroup("outputpanel");
settings.setValue("visible", panel->isVisible());
settings.endGroup();
```
设置结果如下：  
```
mainwindow/size
mainwindow/fullScreen
outputpanel/visible
```

3. void QSettings::endGroup()
用来对最近一次调用beginGroup()时设置的前缀进行重置  
在调用endGroup()之前，调用beginGroup()时设置的前缀可以嵌套叠加  
```
settings.beginGroup("alpha");
// settings.group() == "alpha"

settings.beginGroup("beta");
// settings.group() == "alpha/beta"

settings.endGroup();
// settings.group() == "alpha"

settings.endGroup();
// settings.group() == ""
```

4. QStringList QSettings::childGroups() const
以字符串列表的形式返回所有配置组中最顶层的key  
```
QSettings settings;
settings.setValue("fridge/color", QColor(Qt::white));
settings.setValue("fridge/size", QSize(32, 96));
settings.setValue("sofa", true);
settings.setValue("tv", false);

QStringList groups = settings.childGroups();
// groups: ["fridge"]
```
如果当前组使用了beginGroup()设置前缀，则只返回组内部最顶层的key，不包含组前缀  
```
settings.beginGroup("fridge");
groups = settings.childGroups();
// groups: []
```


## 常用公共函数：对配置进行增删改查
1. void QSettings::setValue(const QString &key, const QVariant &value)
添加一条key以及对应的value  
如果这个key已经存在，之前的value值会被重写  
备注：在windows注册表以及ini文件中的key是不区分大小写的  
```
QSettings settings;
settings.setValue("interval", 30);
settings.value("interval").toInt();     // returns 30

settings.setValue("interval", 6.55);
settings.value("interval").toDouble();  // returns 6.55
```

2. QVariant QSettings::value(const QString &key, const QVariant &defaultValue = QVariant()) const
返回配置中key对应的value，如果setting不存在，则返回defaultValue  
如果没有设置defaultValue，则返回一个默认的QVariant  
```
QSettings settings;
settings.setValue("animal/snake", 58);
settings.value("animal/snake", 1024).toInt();   // returns 58
settings.value("animal/zebra", 1024).toInt();   // returns 1024
settings.value("animal/zebra").toInt();         // returns 0
```

3. bool QSettings::contains(const QString &key) const
判断当前配置中是否包含key  
如果一个组之前使用了QSettings::beginGroup()方法进行设置，key就会被关联到这个组上  

4. void QSettings::remove(const QString &key)
删除key对应的配置，以及包含key对应的配置  
```
QSettings settings;
settings.setValue("ape");
settings.setValue("monkey", 1);
settings.setValue("monkey/sea", 2);
settings.setValue("monkey/doe", 4);

settings.remove("monkey");
QStringList keys = settings.allKeys();
// keys: ["ape"]
```
如果key是一个空的字符串，则当前组中所有的配置都会被删除  
```
QSettings settings;
settings.setValue("ape");
settings.setValue("monkey", 1);
settings.setValue("monkey/sea", 2);
settings.setValue("monkey/doe", 4);

settings.beginGroup("monkey");
settings.remove("");
settings.endGroup();

QStringList keys = settings.allKeys();
// keys: ["ape"]
```

5. void QSettings::clear()
清空当前QSettings对象中所有的配置  
如果只想清空当前组中的所有配置，请使用remove("")方法  

6. QStringList QSettings::allKeys() const
以字符串列表的形式返回所有的key，包括子key  
```
QSettings settings;
settings.setValue("fridge/color", QColor(Qt::white));
settings.setValue("fridge/size", QSize(32, 96));
settings.setValue("sofa", true);
settings.setValue("tv", false);

QStringList keys = settings.allKeys();
// keys: ["fridge/color", "fridge/size", "sofa", "tv"]
```
如果当前组使用了beginGroup()设置前缀，则只返回组内部最顶层的key，不包含组前缀  
```
settings.beginGroup("fridge");
keys = settings.allKeys();
// keys: ["color", "size"]
```

7. QStringList QSettings::childKeys() const
以字符串列表的形式返回所有的key，不包括多层次的key  
```
QSettings settings;
settings.setValue("fridge/color", QColor(Qt::white));
settings.setValue("fridge/size", QSize(32, 96));
settings.setValue("sofa", true);
settings.setValue("tv", false);

QStringList keys = settings.childKeys();
// keys: ["sofa", "tv"]
```
如果当前组使用了beginGroup()设置前缀，则只返回组内部的key，不包含组前缀  
```
settings.beginGroup("fridge");
keys = settings.childKeys();
// keys: ["color", "size"]
```


## 常用公共函数：其他
1. void QSettings::sync()
把尚未保存的修改写入到磁盘中，然后在使用该配置文件的程序中重新加载配置  
备注：这个方法会被析构函数自动调用，所以一般不需要手动去调用  


## 静态公共函数
1.  QSettings::Format defaultFormat()

2. QSettings::Format registerFormat(const QString &extension, QSettings::ReadFunc readFunc, QSettings::WriteFunc writeFunc, Qt::CaseSensitivity caseSensitivity = Qt::CaseSensitive)

3. void setDefaultFormat(QSettings::Format format)

4. void setPath(QSettings::Format format, QSettings::Scope scope, const QString &path)


## enum QSettings::Scope
这个集合用来设置配置文件是针对特定用户生效，还是对系统中的所有用户生效  
```
Constant 				Value 	Description
QSettings::UserScope	0		把配置文件保存到当前用户的特定路径(例如用户的home目录)
QSettings::SystemScope	1		把配置文件保存到全局路径中，所有用户都可以访问
```


## enum QSettings::Status
这个集合中包含了错误状态  
```
Constant 				Value 	Description
QSettings::NoError 		0 		无错误
QSettings::AccessError 	1 		访问错误(例如：试图向一个只读文件中写数据)
QSettings::FormatError 	2 		格式错误
```


## enum QSettings::Format
这个集合包含了QSettings提供的所有的存储格式  
```
Constant 						Value 	Description
QSettings::NativeFormat			0 		按照操作系统平台存储最合适的格式
windows系统对应注册表，MacOS和iOS系统对应CFPreferences API，Unix系统对应ini格式文件

QSettings::Registry32Format 	2 		仅针对Windows系统：
在64位系统上运行的64位程序访问32位的系统注册表
另外，在32位系统上运行的程序，或者在64位系统上运行的32位程序，都按照上述的NativeFormat格式处理
备注：这个集合常量是在Qt 5.7版本中新增的

QSettings::Registry64Format 	3 		仅针对Windows系统：
在64位系统上运行的32位程序访问64位的系统注册表
另外，在32位系统上运行的程序，或者在64位系统上运行的64位程序，都按照上述的NativeFormat格式处理
备注：这个集合常量是在Qt 5.7版本中新增的

QSettings::IniFormat 			1 		把配置存储在ini格式的文件中
注意：从ini文件中读取配置时，类型信息不会被保存，所有的数值会以字符串的格式返回

QSettings::InvalidFormat 		16 		由registerFormat()方法返回的特殊值
```