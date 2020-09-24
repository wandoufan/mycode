# API(application programming interface)应用程序编程接口

## 基本概念
API是一些已经预先定义好的函数功能，开发人员可以直接调用访问，但无需查看源码或理解内部工作机制细节  

## Windows API
Windows API是一套用来控制Windows的各个部件的外观和行为的预先定义的Windows函数  
用户的每个动作都会引发一个或几个函数的运行以告诉Windows发生了什么  
例如，WIN32 API也就是MicrosoftWindows 32位平台的应用程序编程接口  
凡是在Windows系统中执行的应用程序，都可以调用Windows API，API函数包含在Windows系统目录下的DLL文件中  

## Linux API
在linux中，用户编程接口API遵循了UNIX中最流行的应用编程界面标准，即POSIX标准  
这些系统调用编程接口主要是通过C库（LIBC）来实现的  


# SDK(Software Development Kit)软件开发工具包

## 基本概念
SDK的定义是辅助开发某一类软件的相关文档、范例和工具的集合  
一般可以理解为第三方服务商提供的实现软件产品某项功能的工具包，可以直接购买使用  
有公司开发出某个软件的某个功能，可以直接把它封装成SDK出售给其他公司使用  
例如，要在ERP系统中增加某个功能(自动备份、数据分析、云存储等)，但又不想自己耗费时间精力开发  
此时可以选择购买第三方提供的SDK软件包，把ERP系统连接上API接口，就可以使用SDK的功能  


# API and SDK

## 功能对比
SDK可以看做一个封装了某个功能的程序包，这个程序包几乎是封闭的  
只有通过调用接口可以实现程序包中的功能，这个接口就是API  
SDK可以看做一杯饮料，API可以看做用来喝这杯饮料的吸管  
备注：一个SDK不一定只有一个API接口，也可能有多个API  
一般通过web调用实现的功能采用API，通过本地部署实现的功能采用SDK  
常见SDK：Android SDK、IOS SDK、Linux SDK、Windows SDK、Java SDK

## WebAPI和SDK优缺点对比
1. WebAPI
优点：WebAPI的代码少，开发成本低，可以快速验证我们需要实现的功能  
缺点：API会经过对接平台，厂商可以获取对接平台相关数据信息  
2. SDK
优点：SDK对接后的功能比较稳定，响应速度快，而且对接平台相关数据不会被获取  
缺点：需要开发的代码较多，开发成本高，对接周期长  

如果只是简单功能调用，还是使用API更快速便捷一些  
如果是繁琐复杂的功能，多数情况下还是使用SDK更稳妥一些  