# QByteArray

## 基本功能
QByteArray类提供了一个字节序列  
QByteArray可以用来存储原始字节(包含'\0'的)，也可以存储传统的8位字符串(以'\0'结尾的)  
一般用QByteArray来替代'const char \*'，因为使用起来更加方便  
QByteArray会自动在序列末尾添加一个终止符'\0'，这个'\0'不会显示出来，也不会计入size中  


## QByteArray和QString的比较
大多数情况下，我们要使用的都是QString  
QString存储的是16位编码字符，因此可以很容易的存储非ASCII/非Latin-1字符  
而QByteArray更多的使用在以下两种情况：  
1. 需要存储原始二进制数据
2. 内存保护是非常重要的场景(如Qt在嵌入式Linux中应用)


## 使用示例
1. 初始化一个QByteArray类型的字节序列
```
QByteArray ba("Hello");
cout << ba.data()[0] << endl; //输出：H
```

2. null字节序列和empty字节序列的区别
null一定是empty，empty不一定是null  
```
QByteArray().isNull();          // returns true
QByteArray().isEmpty();         // returns true

QByteArray("").isNull();        // returns false
QByteArray("").isEmpty();       // returns true

QByteArray("abc").isNull();     // returns false
QByteArray("abc").isEmpty();    // returns false
```

3. QByteArray中元素的类型为class QByteRef
```
cout << typeid(ba[1]).name() << endl; //输出：class QByteRef
```

4. 把一个QByteArray转换为QString
备注：这个方法是由QString提供的，QByteArray本身没有提供相关方法  
```
QByteArray ba("Hello");
QString str = QString::fromLatin1(ba);
```


## 构造函数
1. QByteArray::QByteArray(QByteArray &&other)

2. QByteArray::QByteArray(const QByteArray &other)

3. QByteArray::QByteArray(int size, char ch)
构造一个长度为size的字节序列，序列中的每个字节都是字符ch  

4. QByteArray::QByteArray(const char \*data, int size = -1)

5. QByteArray::QByteArray()
构造一个空字符序列  


## 数据类型转换相关的常用公共函数
1. 重载函数toHex()
将QByteArray对象转换为16进制编码的格式，返回的16进制编码中只有数字0-9和字母a-f  
可以在函数中加上分割符separator，分割符会被插在16进制数之间  
备注：分割符不能是'\0'，否则无效  
```
QByteArray QByteArray::toHex() const
QByteArray QByteArray::toHex(char separator) const
```
示例1：  
```
QByteArray macAddress = QByteArray::fromHex("123456abcdef");
macAddress.toHex(':'); // returns "12:34:56:ab:cd:ef"
macAddress.toHex(0);   // returns "123456abcdef"
```
示例2：  
```
QByteArray ba("hello");
cout << ba.toHex(' ').data() << endl; //输出"68 65 6c 6c 6f"
```
示例3：
注意：16进制格式的字符串和16进制编码格式不是一个概念  
```
QString str = "01 03 00 00 00 01 84 0A";//16进制格式的字符串
QByteArray ba = str.toLatin1();
cout << ba.toHex(' ').data() << endl;//16进制编码格式
//输出:"30 31 20 30 33 20 30 30 20 30 30 20 30 30 20 30 31 20 38 34 20 30 41"
```


## 常用公共函数
1. char \* QByteArray::data()
返回字符序列的指针，通过这个指针修改序列中的字符  
返回的序列中字符的个数是size()+1，其中1是指序列末尾的终止符'\0'  
备注：QByteArray对象要用cout输出出来时，必须使用data()方法  
```
QByteArray ba("Hello");
cout << ba.data() << endl;
```

2. int QByteArray::size() const
返回字节序列的长度，长度不包含末尾的终止符'\0'  

3. void QByteArray::resize(int size)
重新设置字节序列的长度  
如果size比当前实际长度更大，则会把额外的字符添加到末尾，新添加的字符是未经初始化的  
备注：实际测试，新添加的字符是看不见的，但用size()方法可以看到序列长度确实变长了  
如果size比当前实际长度更小，则会把末尾的部分字符删除掉  
```
QByteArray ba("Hello");
ba.resize(10);
cout << ba.data() << endl; //输出：Hello
cout << ba.size() << endl; //输出10
```

4. void QByteArray::clear()
清空字符串，ba会变成NULL  
```
QByteArray ba = "abc";
ba.clear();
qDebug() << ba; \\输出：""
qDebug() << ba.isNull(); \\输出：true
qDebug() << ba.isEmpty(); \\输出：true
```


## 静态公共函数
1. 重载函数number()
把数字转换为QByteArray  
```
[static] QByteArray QByteArray::number(int n, int base = 10)  
[static] QByteArray QByteArray::number(uint n, int base = 10)  
[static] QByteArray QByteArray::number(qlonglong n, int base = 10)  
[static] QByteArray QByteArray::number(qulonglong n, int base = 10)  
[static] QByteArray QByteArray::number(double n, char f = 'g', int prec = 6)  
```
示例：  
```
int n = 63;
QByteArray::number(n);                // returns "63"
QByteArray::number(n, 16);            // returns "3f"
QByteArray::number(n, 16).toUpper();  // returns "3F"
```

2. [static] QByteArray QByteArray::fromHex(const QByteArray &hexEncoded)
将16进制编码的序列hexEncoded进行解码后返回  
输入的hexEncoded不会检查合法性，如果包含非法的字符，会跳过该字符继续往下处理  
示例：  
```
QByteArray text = QByteArray::fromHex("517420697320677265617421");
cout << text.data() << endl;//输出"Qt is great!"

QString str = "01 03 00 00 00 01 84 0A";//16进制格式的字符串
QByteArray ba = str.toLatin1();
cout << QByteArray::fromHex(ba).data() << endl;
//输出： (是一个乱码)
```