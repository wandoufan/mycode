# QUuid

## 基本功能
QUuid用来生成和存储一个全球唯一码(Universally Unique Identifier)UUID  
父类：无  
子类：无  


## 代码示例：最常用来生成一个id字符串
QUuid::createUuid()为随机生成模式，生成的id每次都不一样
```
QUuid uuid = QUuid::createUuid();
QString id = uuid.toString();
qDebug() << id;
```
输出结果示例：
```
"{57a5d3dc-c761-47eb-9ac1-216fa91362cc}"
"{d75c0470-2c2b-49cc-b757-60c09dfa3576}"
"{31016acc-5e60-4e03-8c17-29d16daaa02a}"
"{927502bd-555a-47f1-9b41-755c88d1fdb6}"
...
```


## 构造函数
1. QUuid::QUuid()
转换一个空的UUID，空的UUID转换为字符串格式输出结果为：
```
{00000000-0000-0000-0000-000000000000}
```

2. QUuid::QUuid(uint l, ushort w1, ushort w2, uchar b1, uchar b2, uchar b3, uchar b4, uchar b5, uchar b6, uchar b7, uchar b8)
使用指定的参数来创建一个UUID
```
QUuid IID_MyInterface(0x67c8770b, 0x44f1, 0x410a, 0xab, 0x9a, 0xf9, 0xb5, 0x44, 0x6f, 0x13, 0xee);
// 输出结果：{67C8770B-44F1-410A-AB9A-F9B5446F13EE}
```

3. QUuid::QUuid(const QString &text)
使用QString创建UUID，QString必须是UUID的格式

4. QUuid::QUuid(const QByteArray &text)
使用QByteArray创建UUID，QByteArray必须是UUID的格式

5. QUuid::QUuid(const GUID &guid)
把一个Windows的GUID转换为QUuid


## 常用公共函数：把UUID转换为各种格式
1. QString QUuid::toString() const

2. QString QUuid::toString(QUuid::StringFormat mode) const

3. QByteArray QUuid::toByteArray(QUuid::StringFormat mode) const

4. QByteArray QUuid::toByteArray() const

5. CFUUIDRef QUuid::toCFUUID() const

6. NSUUID \*QUuid::toNSUUID() const

7. QByteArray QUuid::toRfc4122() const


## 常用公共函数：读取属性
备注：属性只有读取函数，没有设置函数
1. QUuid::Variant QUuid::variant() const

2. QUuid::Version QUuid::version() const

3. bool QUuid::isNull() const


## 常用公共函数：判断是否为空
1. bool QUuid::isNull() const


## 常用公共函数：各种操作符
1. bool operator!=(const QUuid &other) const
2. bool operator!=(const GUID &guid) const
3. bool operator<(const QUuid &other) const
4. QUuid &operator=(const GUID &guid)
5. bool operator==(const QUuid &other) const
6. bool operator==(const GUID &guid) const
7. bool operator>(const QUuid &other) const


## 常用静态公共函数：生成UUID
1. [static] QUuid QUuid::createUuid()
variant取值QUuid::DCE，version取值QUuid::Random

2. [static] QUuid QUuid::createUuidV3(const QUuid &ns, const QByteArray &baseData)
variant取值QUuid::DCE，version取值QUuid::Md5

3. [static] QUuid QUuid::createUuidV3(const QUuid &ns, const QString &baseData)
variant取值QUuid::DCE，version取值QUuid::Md5

4. [static] QUuid QUuid::createUuidV5(const QUuid &ns, const QByteArray &baseData)
variant取值QUuid::DCE，version取值QUuid::Sha1

5. [static] QUuid QUuid::createUuidV5(const QUuid &ns, const QString &baseData)
variant取值QUuid::DCE，version取值QUuid::Sha1


## 常用静态公共函数：转换为UUID
1. [static] QUuid QUuid::fromCFUUID(CFUUIDRef uuid)

2. [static] QUuid QUuid::fromNSUUID(const NSUUID \*uuid)

3. [static] QUuid QUuid::fromRfc4122(const QByteArray &bytes)

4. [static] QUuid QUuid::fromRfc4122(const QByteArray &bytes)

5. [static] QUuid QUuid::fromString(QLatin1String text)


## enum QUuid::StringFormat
这个集合包含了UUID的字符串格式
备注：这个集合在Qt 5.11中增加
```
Constant 				Value 			Description
QUuid::WithBraces 		0 				默认值，包含5个16进制字段、分隔符、大括号
QUuid::WithoutBraces 	1 				包含5个16进制字段、分隔符
QUuid::Id128 			3 				只有5个16进制字段，这种字符串格式不能再被解析回去
```


## enum QUuid::Variant
这个集合包含了UUID的数值字段，最常用是QUuid::DCE
```
Constant 				Value 			Description
QUuid::VarUnknown 		-1 				Variant is unknown
QUuid::NCS 				0 				兼容网络计算系统NCS (Network Computing System)
QUuid::DCE 				2 				兼容分布式计算环境DCE(Distributed Computing Environment)
QUuid::Microsoft 		6 				兼容微软的GUID
QUuid::Reserved 		7 				Reserved for future definition
```


## enum QUuid::Version
这个集合包含了UUID的生成方式，只有当UUID为QUuid::DCE时，这个集合中的取值才有意义
```
Constant 				Value 		Description
QUuid::VerUnknown 		-1 			Version is unknown
QUuid::Time 			1 			基于时间生成
QUuid::EmbeddedPOSIX 	2 			DCE Security version, with embedded POSIX UUIDs
QUuid::Name 			Md5 		基于名字生成
QUuid::Md5 				3 			相当于QUuid::Name
QUuid::Random 			4 			随机生成
QUuid::Sha1 			5
```