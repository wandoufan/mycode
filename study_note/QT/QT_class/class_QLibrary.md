# QLibrary

## 基本功能
QLibrary可以在运行时加载共享库，使用前要'include <QLibrary>'  
QLibrary属于显式调用方式，即在程序执行到某个函数时才去加载对应的动态库  


## 常用函数
1. QLibrary(const QString &fileName, const QString &version, QObject \*parent = nullptr)
构造函数QLibrary，根据指定的dll文件路径初始化获得一个对象  
```
QLibrary *aoso_reader;
aoso_reader = new QLibrary("function.dll");
```
2. bool QLibrary::load()
load函数加载库文件，然后根据dll文件是否加载成功，成功返回1，失败返回0  
```
if(aoso_reader.load())
```
3. bool QLibrary::isLoaded() const
isLoaded函数判断库文件是否已经加载，已经加载返回1，未加载返回0  
一般要先使用load函数，之后再用isLoaded函数去判断  
```
if(aoso_reader.isLoaded())
```
4. QString fileName() const
fileName函数查看当前的dll文件名  
```
cout << aoso_reader.fileName().toLatin1().data() << endl;
```
5. QFunctionPointer QLibrary::resolve(const char \*symbol)
这是QLibrary最重要的函数，用来调用库中的接口函数  
当调用接口函数成功时，返回一个函数指针  
当调用函数失败或库文件没有加载时，返回一个空指针  
```
例1 调用接口函数avg
typedef int (*AvgFunction)(int, int);
AvgFunction avg = (AvgFunction) library->resolve("avg");
if(avg)
  return avg(5, 8);
else
  return -1;
```
```
例2 调用接口函数ControlLED
unsigned char buffer;
typedef int (*ControlLED_Func)(int freq, int duration, unsigned char *buffer);
if(aoso_reader -> load())
{
    ControlLED_Func ControlLED = (ControlLED_Func)aoso_reader -> resolve("ControlLED");
    if(ControlLED)
    {
        int result = ControlLED(5, 2, &buffer);
    }
}
```
