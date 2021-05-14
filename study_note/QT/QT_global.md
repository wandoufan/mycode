# QT中的全局定义

## QtGlobal.h
QT类库中的全局定义都放在<QtGlobal>头文件中，包括全局变量、全局函数、全局宏等  
一般的Qt类的头文件都会包含该文件，所以不用显式包含这个头文件也可以使用其中的定义  


## 全局变量
1. 基本定义
为了确保在各个平台上各数据类型都有统一确定的长度，Qt为各种常见数据类型定义了类型符号  
2. Qt数据类型--等效定义--字节数
```
qint8	signed char	1
qint16	signed short	2
qint32	signed int	4
qint64	long long int	8
qlonglong	long long int	8
quint8	unsigned char	1
quint16	unsigned short	2
quint32	unsigned int	4
quint64	unsigned long long int	8
qulonglong	unsigned long long int	8
uchar	unsigned char	1
ushort	unsigned short	2
uint	unsigned int	4
ulong	unsigned long	8
qreal	double	8
qfloat16	 	2
```


## 全局函数
1. 基本定义
<QtGlobal>头文件包含一些常用函数的定义，这些函数多以模板类型作为参数，返回相应的模板类型，模板类型可以用任何其他类型替换  
若是以double或float类型数作为参数的，一般有两个参数版本的同名函数，如qFuzzyIsNull(double d)和qFuzzyIsNull(float f)  
一些基础的数学运算函数在<QtMath>头文件中定义，比如三角运算函数、弧度与角度之间的转换函数等  
2. 函数--功能
```
T qAbs(const T &value)	返回变量 value 的绝对值
const T &qBound(const T &min, const T&value, const T &max)	返回 value 限定在 min 至 max 范围之内的値
bool qFuzzyComparc(doublc p1, double p2)	若 p1 和 p2 近似相等，返回 true
bool qFuzzyIsNulI(double d)	如果参数 d 约等于 0，返回 true
double qInf(()	返回无穷大的数
bool qIsFinite(double d) 	若 d 是一个有限的数，返回 true
bool qIsInf(double d) 	若 d 是一个无限大的数，返回 true
bool qIsNaN(double d)	若 d 不是一个数，返回 true
constT&qMax(const T&value1, const T&value2)	返回 value1 和 value2 中较大的值
const T &qMin(const T&value1, const T&value2)	返回 value1 和 value2 中较小的值
qint64 qRound64(double value) 	将 value 近似为最接近的 qint64 整数
int qRound(double value)	将 value 近似为最接近的 int 整数
int qrand()	标准 C++ 中 rand() 函数的线程安全型版本，返回 0 至 RAND_MAX 之间的伪随机数
备注：这个函数已经过时，不再使用了
void qsrand(uint seed)	标准 C++ 中 srand() 函数的线程安全型版本，使用种子 seed 对伪随机数字序列初始化
备注：这个函数已经过时，不再使用了
```


## 常用的全局宏
1. QT_VERSION
这个宏展开为数值形式 0xMMNNPP (MM = major, NN = minor, PP = patch) 表示 Qt 编译器版本  
例如 Qt 编译器版本为 Qt 5.9.1，则 QT_VERSION 为 0x050901  
这个宏常用于条件编译设置，根据 Qt 版本不同，编译不同的代码段  
2. QT_VERSION_CHECK
这个宏展开为 Qt 版本号的一个整数表示  
3. QT_VERSION_STR
这个宏展开为 Qt 版本号的字符串，如'5.9.0'  
4. Q_BYTE_ORDER
这个宏表示系统内存中数据的字节序  
5. Q_BIG_ENDIAN 
这个宏表示大端字节序  
6. Q_LITTLE_ENDIAN
这个宏表示小端字节序  