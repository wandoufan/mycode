# QLibrary

## 基本功能
QLibrary可以在运行时加载共享库
QLibrary属于显式调用方式，即在程序执行到某个函数时才去加载对应的动态库  
父类：QObject  


## 动态库调用方式
显式调用方式：只需要dll文件  
隐式调用方式：需要dll文件、lib文件、h文件  


## 构造函数
1. QLibrary::QLibrary(const QString &fileName, const QString &version, QObject \*parent = nullptr)

2. QLibrary::QLibrary(const QString &fileName, int verNum, QObject \*parent = nullptr)

3. QLibrary::QLibrary(const QString &fileName, QObject \*parent = nullptr)
fileName参数为dll文件的路径和名字  
```
QLibrary *aoso_reader;
aoso_reader = new QLibrary("function.dll");
```

4. QLibrary::QLibrary(QObject \*parent = nullptr)


## 常用成员变量
1. fileName : QString
这个属性设置要加载的dll文件的路径和名字  
1.1 QString fileName() const
1.2 void setFileName(const QString &fileName)

2. loadHints : LoadHints
这个属性用来给load()一些执行相关的提示  
2.1 QLibrary::LoadHints loadHints() const
2.2 void setLoadHints(QLibrary::LoadHints hints)


## 常用公共函数
1. bool QLibrary::load()
加载库文件，返回是否加载成功  
resolve()函数每次都会在内部先调用load()函数，因此一般没必要手动调用load()函数  
在一些场景下可能需要提前加载库文件，这时可以使用这个函数  

2. bool QLibrary::isLoaded() const
判断库文件是否已经加载  

3. bool QLibrary::unload()
卸载库文件  

4. QString QLibrary::errorString() const
返回最新一次报错的具体内容  
备注：只有在调用load()、unload()、resolve()函数失败之后，才会有报错内容

5. QFunctionPointer QLibrary::resolve(const char \*symbol)
返回扩展接口的地址  
当调用函数失败或库文件没有加载时，返回一个空指针  
备注：这是QLibrary最重要的函数，用来调用库中的接口函数  
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
typedef int (*ControlLED_Func)(int freq, int duration, unsigned char *buffer);//定义函数指针
if(aoso_reader -> isLoaded())
{
	//第一个ControlLED是函数指针的名字，第二个ControlLED是dll中接口函数的名字
	//这两个名字可以相同，也可以不一样
    ControlLED_Func ControlLED = (ControlLED_Func)aoso_reader -> resolve("ControlLED");
    if(ControlLED)//判断函数指针是否为空
    {
        int result = ControlLED(5, 2, &buffer);
    }
}
```


## 公共静态函数
1. [static] bool QLibrary::isLibrary(const QString &fileName)
判断指定的库文件是否是合法的文件格式  

2. [static] QFunctionPointer QLibrary::resolve(const QString &fileName, const char \*symbol)

3. [static] QFunctionPointer QLibrary::resolve(const QString &fileName, int verNum, const char \*symbol)

4. [static] QFunctionPointer QLibrary::resolve(const QString &fileName, int verNum, const char \*symbol)