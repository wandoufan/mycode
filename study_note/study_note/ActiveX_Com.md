# ActiveX控件

## 基本概念
ActiveX控件是Microsoft提供的一系列插件程序，例如应用于浏览器的各种插件  
ActiveX控件可以在Windows窗体和Web程序上使用  
ActiveX可以由各种的语言进行开发，同时支持windows、Linux、Mac等多个平台  
其中，ActiveX控件在windows系统中是作为一个DLL动态链接库文件来实现的  
控件文件的后缀名是.ocx，ocx文件属于可执行文件，但不能像exe文件一样直接执行  
```
示例：
UserControl类用来提供一个可用来创建其他控件的空控件
class HWPenSign : public System::Windows::Forms::UserControl
```
备注：一般不直接用c++去调用ocx控件，而是在QT或MFC里去实现调用ocx控件  
详见	QT_activex.md中介绍  


## COM组件
**基本定义**
COM(Component Object Model)即组件对象模型，是基于Windows平台的一套组件对象接口标准  
COM提供跟编程语言无关的方法实现一个软件对象，因此可以在其他环境中运行  
通过COM可以轻松实现一种语言（如C#）调用另一种语言（如C++、VB等）开发的功能模块  
COM可以在多个平台上运行，但windows平台还是最常用COM的，而且某些功能已被.NET平台取代  
组件对象和由类实例化出来的对象相似，但又有很大不同  
组件对象不使用方法而用接口来描述自身，且实现的接口数量没有限制  
接口的实质是一组函数指针表，每个指针必须初始化指向某个具体的函数体  
**组件唯一标识**
对于每个组件都需要使用标识符进行唯一标识，也作为调用该组件时的依据  
COM组件的GUID、UUID、CLSID是一回事，只不过各自代表的意义不同  
1. UUID(Universally Unique Identifier)通用唯一识别码
UUID代表COM组件  
2. CLSID(class identifier)类标识符
CLSID也称为CLASSID代表COM组件中的类对象，可以在注册表里查看  
3. GUID(Globally Unique Identifier)全局唯一标识符


## ActiveX和COM的对比
ActiveX控件是以COM组件为技术基础进行实现的  
二者并没有本质的区别，仅有一些概念上的差异，使用惯例上来说：  
1. ActiveX一般包含一个窗体界面，COM对象一般并没有界面  
2. COM对象一般作为一个可调用的模块来使用，ActiveX一般嵌入在网页中使用  


## COM组件三个基本接口类
> https://blog.csdn.net/weiwangchao_/article/details/6949264
1. IUnknown
2. IClassFactory
3. IDispatch

## COM组件相关的Windows API函数
备注：MFC中可能要用到这几个函数，QT中一般都封装好了，不需要直接调用  
1. OleInitialize
Ole是在Com的基础上作的扩展，是ActiveX运行的基础  
OleInitialize是初始化Ole的运行环境，OleInitialize肯定会调用CoInitialize  
OleInitialize用来初始化Com（其实也是调用CoInitializeEx），支持多线程  
OleInitialize相比CoInitialize多了以下内容：  
A) Clipboard  
B) Drag and drop  
C) Object linking and embedding (OLE)  
D) In-place activation  
如果不需要这些，用CoInitialize就可以  
备注：OleInitialize和OleUninitialize成对使用  
2. CoInitialize和CoInitializeEx
CoInitialize和CoInitializeEx都是windows的API，主要是告诉windows以什么方式为程序创建COM对象  
原因是程序调用com库函数（除CoGetMalloc和内存分配函数）之前必须初始化com库  
CoInitialize指明以单线程方式创建  
CoInitialize仅仅初始化Com，支持多线程，也就是说如果多线程调用Com接口，必须在每个线程中都调用CoInitialize  
CoInitializeEx可以指定COINIT_MULTITHREADED以多线程方式创建  
3. AfxOleInit
AfxOleInit实际上调用了OleInitialize，虽然它在内部也调用了CoInitializeEx，但它只能处理单线程，这是AfxOleInit和CoInitialize主要区别  
MFC程序建议使用AfxOleInit（）  