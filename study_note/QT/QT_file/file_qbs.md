# Qt中的.qbs文件

## 基本功能
.qbs文件类似于.pro文件，都是写入一些配置参数  


## 产生.qbs文件的方法
在新建Qt项目时，在'Build System'步骤选择qbs(默认是qmake)  
这样产生的项目中就会有.qbs文件，但不再有.pro文件了  


## qbs的概念
QBS（Qt Build Suite）即Qt编译套件，它和qmake、cmake之类一样都是构建工具  
qbs是下一代的构建工具，极有可能会替代qmake成为Qt 6.0的构建系统  


## qbs和qmake的对比
与qmake相比，qbs提供了更快构建速度，以及更多的特性  
qbs没有绑定Qt版本，它从项目文件的高级项目描述中生成一个正确的编译表（依赖表）  
传统的MakeFile生成工具比如qmake和CMake生成了makefile文件，然后将实际的命令留给make或者ninja这样的工具去执行  
Qbs的另一方面就是充当了并行生成与直接调用编译器、连接器以及其他工具的角色，非常像SCons和Ant做的事情  


## qbs的语法
qbs的语法是一个简化版本的qml，提供了对IDE友好的软件项目的展示  
它同样提供了自由使用任何JavaScript表达式进行属性绑定的支持  
项目文件编辑器能够理解如何对纯字符串数组文字进行处理  
对于更复杂的结构，项目文件编辑器能够“回滚”，使用文本编辑器打开项目文件  


## .qbs文件示例
```
import qbs.FileInfo

QtApplication {
    Depends { name: "Qt.widgets" }

    cpp.defines: [
        // You can make your code fail to compile if it uses deprecated APIs.
        // In order to do so, uncomment the following line.
        //"QT_DISABLE_DEPRECATED_BEFORE=0x060000" // disables all the APIs deprecated before Qt 6.0.0
    ]

    files: [
        "main.cpp",
        "mainwindow.cpp",
        "mainwindow.h",
        "mainwindow.ui",
    ]

    install: true
    installDir: qbs.targetOS.contains("qnx") ? FileInfo.joinPaths("/tmp", name, "bin") : base
}
```


