# QT程序中的报错


## LNK2019: 无法解析的外部符号
这个是Qt项目中最常见的报错之一，可能的原因有很多  
注意：尝试对报错进行修复之后，要先把产生的debug或release目录删除之后再重新运行  

1. 类内使用了信号与槽，但未包含Q_OBJECT宏，因此需在类内加上Q_OBJECT

2. 添加新的.ui窗体文件时编译器没有为它生成新的.obj文件而报错
先重新执行qmake，再运行项目

3. 项目没有包含需要的QT模块，需要在.pro文件中添加对应的模块

4. 头文件中声明了slot槽函数，但在源文件中没有进行具体的定义实现

5. 项目中引用了lib库，这个lib库是32位的，但项目编译的时候用的是64位的编译配置

6. 项目中引用了库文件，但没有在.pro文件中正确地包含库文件

7. 有时候就是把之前编译的debug或release目录删除就好了


## LNK2019/LNK2001: 无法解析的外部符号
1. 代码示例
```
class LoadPageWidget : public QWidget
{
    Q_OBJECT

public:
    LoadPageWidget()
    {
        qDebug() << "123";
    }
};
```
2. 说明
在类中声明了Q_OBJECT宏，但没有用到信号与槽等相关机制，类中也没有写太多有效内容
在Qt 5.2 + VS2010中编译时会有报错：
```
editorplugin.obj:-1: error: LNK2019: unresolved external symbol "public: __thiscall Editor::Internal::LoadEditPage::LoadEditPage(void)" (??0LoadEditPage@Internal@Editor@@QAE@XZ) referenced in function "public: virtual bool __thiscall Editor::Internal::EditorPlugin::initialize(class QStringList const &,class QString *)" (?initialize@EditorPlugin@Internal@Editor@@UAE_NABVQStringList@@PAVQString@@@Z)
```
在Qt 5.11 + VS2015中编译时会有报错：
```
mainwindow.obj:-1: error: LNK2001: unresolved external symbol "public: virtual struct QMetaObject const * __cdecl LoadPageWidget::metaObject(void)const " (?metaObject@LoadPageWidget@@UEBAPEBUQMetaObject@@XZ)
```
这个报错的原因与Q_OBJECT宏和元对象编译器MOC有关，但没有完全搞明白
3. 解决办法
网上有很多人遇到了类似的问题，给出了很多办法
https://blog.csdn.net/weixin_42255049/article/details/121928834
https://blog.csdn.net/xzq413520903/article/details/79554318
但这些办法实际测试都不行，目前唯一办法就是把Q_OBJECT先注释掉，等真正用到信号与槽等机制时再添加上


## LNK1123: 转换到 COFF 期间失败: 文件无效或损坏
1. 环境描述
使用Qt 5.2.1 + VS 2010环境
创建一个最简单的项目，以debug模式运行时就会产生如上报错，以release模型运行则没有问题
2. 解决办法
在C盘的Windows目录中搜索cvtres.exe，可以找到多个结果
```
C:\Windows\Microsoft.NET\Framework\v4.0.30319
...
```
在VS的目录中也有一个cvtres.exe
```
C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin
```
Windows目录中的cvtres.exe时间日期比VS目录中的cvtres.exe更新
用Windows目录中的cvtres.exe替换VS目录中的cvtres.exe即可
