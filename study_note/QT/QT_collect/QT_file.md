# Qt中的文件系统

## 继承关系
```
                                              |- QSctpSocket
QIODevice -|- QAbstractSocket -|- QTcpSocket -|- QSslSocket
                               |- QUdpSocket

           |- QFileDevice -|- QFile -|- QTemporaryFile
                           |- QSaveFile
```


## QIODevice及其子类
QIODevice
所有 I/O 设备类的父类，提供了字节块读写的通用操作以及基本接口

QFileDevice
Qt5新增加的类，提供了有关文件操作的通用实现

QFlie
访问本地文件或者嵌入资源

QTemporaryFile
创建和访问本地文件系统的临时文件

QBuffer
读写QbyteArray, 内存文件

QProcess
运行外部程序，处理进程间通讯

QAbstractSocket
所有套接字类的父类

QTcpSocket
TCP协议网络数据传输

QUdpSocket
传输 UDP 报文

QSslSocket
使用 SSL/TLS 传输数据


## 与文件系统相关的其他类(不是QIODevice的子类)
QFileInfo
获取文件的详细信息

QDir
实现文件目录相关的功能



-------------------------------------------------

## 代码示例：使用QFile读写文本文件
备注：如果写入的是文本数据，则文件可以直接用各种文本编辑器打开查看内容  
1. 写入数据
```
//写入一行文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    file.write("this is a QIODevice test");
}
file.close();

//写入多行文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    file.write("this is line 1\n");
    file.write("this is line 2\n");
    file.write("this is line 3\n");
    file.write("this is line 4\n");
    file.write("this is line 5\n");
}
file.close();
```
2. 读取数据
```
//读出所有文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    QByteArray array = file.readAll();
    QString content = QString::fromLatin1(array);
}
file.close();

//逐行读出文本内容
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite | QIODevice::Text))
{
    while(!file.atEnd())
    {
        QByteArray array = file.readLine();
        QString content = QString::fromLatin1(array);
        qDebug() << content;
    }
}
file.close();
```


## 代码示例：单独使用QFile读写二进制文件
备注：这种方式也能实现，但非常麻烦，不推荐
```
//写入二进制文件
qint32 nums[5] = {1,2,3,4,5};
//写入文件之前，要将数据以二进制方式存储到字节数组中
QByteArray array;
array.resize(sizeof(nums));
for(int i=0;i<5;i++)
{
    //借助指针，将每个整数拷贝到字节数组中
    memcpy(array.data()+i*sizeof(qint32),&(nums[i]),sizeof(qint32));
}
QFile file("D:/test.data");
if(file.open(QIODevice::ReadWrite))
{
    file.write(array);
}
file.close();
```


## 代码示例：使用QDataStream + QFile读写二进制文件
1. 读写C++的基本数据类型，如int、double、char[]
```
//要存入二进制文件的数据
int i = 10;
double d = 3.1415;
char str[10] = "abcde";
//写入二进制文件
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadWrite))
{
    datastream << i << d << str;
}
file.close();
```
```
//要从二进制文件中读取的数据
int i;
double d;
char *str = new char[10];//字符数组需要用new出来的指针
//读取二进制文件
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadOnly))
{
    datastream >> i >> d >> str;
    qDebug() << i;
    qDebug() << d;
    qDebug() << str;
}
file.close();
delete [] str;//使用之后要delete
```

2. 读写Qt容器类，如QList
备注：二进制文件打开后是乱码，无法直接查看  
```
//要写入文件中的数据
QList<int> list1, list2;
for(int i = 0; i < 20; i++)
{
    list1.append(i);
    list2.append(2 * i);
}
//写入二进制文件
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadWrite))
{
    datastream << list1 << list2;
}
file.close();
```
```
//定义数据
QList<int> list1, list2;
//读取二进制文件
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadOnly))
{
    datastream >> list1 >> list2;
    //输出数据
    qDebug() << list1;
    qDebug() << list2;
}
file.close();
```

3. 读写其他Qt类，如QFont、QColor、QImage
备注：二进制文件打开后是乱码，无法直接查看  
```
//要存入二进制文件的数据
QColor color = QColor(255, 0, 0, 255);
QFont font = QFont("Calibri", 10, 50);
QImage image(50, 50, QImage::Format_RGB32);
image.fill(Qt::blue);
ui -> label -> setPixmap(QPixmap::fromImage(image));
//写入二进制文件
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadWrite))
{
    datastream << color << font << image;
}
file.close();
```
```
//要从二进制文件中读取的数据
QColor color;
QFont font;
QImage image;
//读取二进制文件
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadOnly))
{
    datastream >> color >> font >> image;
}
file.close();
```

4. 读写复杂的数据类型(结构体)，不能用操作符，只能用读写函数
注意：实际测试，结构体中的成员变量如果包含字符串，只能使用字符数组char[]，不能用QString，否则读取报错  
不管是用readRawData()还是readBytes()，都会读取报错，只能用char[]来存储字符串  
```
//要写入文件中的结构体数据
struct Student
{
    char name[10];
    int age;
    double score;
};
struct Student student1, student2;
strcpy(student1.name, "zhang");
strcpy(student2.name, "li");
student1.age = 10;
student2.age = 11;
student1.score = 88.88;
student2.score = 77.77;
//使用memcpy()方法把结构体数据放入指定内存中
char temp1[sizeof(Student)];
char temp2[sizeof(Student)];
memcpy(temp1, &student1, sizeof(Student));
memcpy(temp2, &student2, sizeof(Student));
//写入二进制文件
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadWrite))
{
    datastream.writeRawData(temp1, sizeof(Student));
    datastream.writeRawData(temp2, sizeof(Student));
}
file.close();
```
```
//定义结构体数据
struct Student
{
    char name[10];
    int age;
    double score;
};
struct Student student1, student2;
//读取二进制文件
uint length = sizeof(Student);
char *temp1 = new char[length];
char *temp2 = new char[length];
QFile file("D:/test.data");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadOnly))
{
    datastream.readRawData(temp1, length);
    datastream.readRawData(temp2, length);
    memcpy(&student1, temp1, length);
    memcpy(&student2, temp2, length);
    //输出数据
    qDebug() << student1.name;
    qDebug() << student1.age;
    qDebug() << student1.score;
    qDebug() << student2.name;
    qDebug() << student2.age;
    qDebug() << student2.score;
}
file.close();
delete[] temp1;
delete[] temp2;
```


## 代码示例：在Qt代码中读取用C语言写入的二进制文件
在Wincc中用C语言的fwrite()方法把数据写入二进制文件
```
int GearBoxConfig[10];
int GearBox_Parameter[50][4];
char CommandInfo[25][200];
...
FILE* fp;
fp = fopen(file_path, "wb");
fwrite(GearBoxConfig, sizeof(int), 10, fp);
fwrite(GearBox_Parameter, sizeof(int), 200, fp);
fwrite(CommandInfo, sizeof(char), 5000, fp);
```
方法一：直接用C语言的fread()方法读取二进制文件
备注：实际测试，在Qt中也可以使用C语言中读写文件的函数，但会提醒函数已过时
```
int GearBoxConfig[10];
int GearBox_Parameter[50][4];
char CommandInfo[25][200];
...
FILE* fp;
fp = fopen(file_path, "rb");
fread(GearBoxConfig, sizeof(int), 10, fp);
fread(GearBox_Parameter, sizeof(int), 200, fp);
fread(CommandInfo, sizeof(char), 5000, fp);
```
方法二：使用QDataStream + QFile读取C语言写的二进制文件
```
//要从二进制文件中读取的数据
int GearBoxConfig[10];
int GearBox_Parameter[50][4];
char CommandInfo[25][200];
//读取二进制文件
uint length1 = sizeof(int) * 10;
uint length2 = sizeof(int) * 200;
uint length3 = sizeof(char) * 5000;
char *temp1 = new char[length1];
char *temp2 = new char[length2];
char *temp3 = new char[length3];
QFile file("D:/test.cfg");
QDataStream datastream(&file);
if(file.open(QIODevice::ReadOnly))
{
    datastream.readRawData(temp1, static_cast<int>(length1));
    datastream.readRawData(temp2, static_cast<int>(length2));
    datastream.readRawData(temp3, static_cast<int>(length3));
    memcpy(GearBoxConfig, temp1, length1);
    memcpy(GearBox_Parameter, temp2, length2);
    memcpy(CommandInfo, temp3, length3);
}
file.close();
delete [] temp1;
delete [] temp2;
delete [] temp3;
```


