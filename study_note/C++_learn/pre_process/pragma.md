# pragma指令

## 基本说明
1. pragma指令设定编译器的状态或者是指示编译器完成一些特定的动作
在所有的预处理指令中，pragma指令是最复杂的
2. C语言和C++语言都支持pragma指令，但不一定都能执行所有的pragma指令
3. 很多指令只在Wincc的C脚本中使用，和Wincc的关系？
注意：pragma指令后面没有分号;


## pragma once
1. 只要在头文件的最开始加入'#pragma once'这条预处理指令，就能够保证头文件只被编译一次  
2. 由于编译器每次都需要打开头文件才能判定是否有重复定义，因此在编译大型项目时，ifndef会使得编译时间相对较长，因此一些编译器逐渐开始支持'#pragma once'的方式  
3. pragma once方式却不受一些较老版本的编译器支持，所以它的兼容性可能不够好  
备注：一般尽量选择ifdef的方式  
```
#pragma once
```


## pragma message
当编译器遇到这条指令时就可以在编译输出窗口中显示相应的信息
```
#pragma message("这是一条输出信息")
```


## pragma option
1. 使字符串可以包含多字节的字符
备注：这个仅在Wincc的C脚本中使用，不是Wincc7.4自动生成的，没有搞明白具体含义
```
#pragma option(mbcs)
```


## pragma code
1. 在Wincc脚本中调用dll
备注：这个仅在Wincc的C脚本中使用
```
//指定要使用的dll文件
#pragma code ("D:\\work\\UDPSendCC.dll")
//声明dll中提供的函数
void Dout(char* Data, WORD wView);
void DoutArrayDouble10(double* Data, DWORD nNum, WORD wView);
void DoutArrayFloat10(float* Data, DWORD nNum, WORD wView);
//表示结束行，总是和第一行成对出现
#pragma code ()
```

