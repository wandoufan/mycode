# QDesignerCustomWidgetInterface

## 基本功能
这个类能够使Qt Designer接收并构建自定义的Widget控件  
这个类提供了一个带有接口的自定义Widget控件  
备注：当新建一个自定义控件项目时，外层插件头文件的自定义类是继承于这个类的  
系统会自动生成这个类的成员函数以及函数定义，因此成员函数一般不用自己手动写出来  
另外，对自定义控件类声明时，要加上宏QDESIGNER_WIDGET_EXPORT  


## QDESIGNER_WIDGET_EXPORT宏
1. 基本功能
当声明自定义控件时必须要用这个宏，来确保它们被正确的扩展到qt designer里使用  
这个宏用于将自定义组件类从插件导出给qt designer使用  
2. 使用方法
一般在自定义控件项目的控件头文件中会声明自定义控件的类  
在关键字'class'和类名中间要加上这个宏  
另外，还要加上'#include <QtUiPlugin/QDesignerExportWidget>'  
否则使用该控件的项目运行时会报错无法找到头文件  
3. 使用示例:
custombutton.h  
```
#include <QtUiPlugin/QDesignerExportWidget>

class QDESIGNER_WIDGET_EXPORT CustomButton : public QWidget
{
    Q_OBJECT

public:
    CustomButton(QWidget *parent = 0);
};
```


## 常用函数
1. virtual QString codeTemplate() const
这个函数是未来为Qt Designer预留的  
2. virtual QWidget * createWidget(QWidget * parent)
用给出的父类，返回一个自定义Widget控件的实例  
备注：这是最重要的一个函数，整个自定义控件项目都是自动生成的标准代码  
这是唯一能和我们自定义的控件类产生关联的地方，通过这里返回一个控件类的实例  
```
QWidget *CustomTest2Plugin::createWidget(QWidget *parent)
{
    return new CustomTest2(parent);
}

```
3. virtual QString domXml() const
设置并返回一个用来向Qt Designer描述自定义控件属性的XML  
这个XML其实就是.ui文件的可编辑内容，因此可以用来设置控件的大小位置等属性  
但一般不要在这个地方进行属性设置，应该在控件本身的代码中进行设置  
```
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Widget</class>
 <widget class="QWidget" name="Widget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>727</width>
    <height>338</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Widget</string>
  </property>
  ......
```
4. virtual QString group() const
返回自定义控件所属的组名，这个组名将会显示在UI界面左侧的设计组件中  
备注：常用函数  
5. virtual QIcon icon() const
返回在Qt Designer的widget box中用来表示这个自定义组件的控件  
6. virtual QString includeFile() const
返回用户接口编译器(uic)创建自定义控件的代码时用到的文件的路径  
7. virtual void initialize(QDesignerFormEditorInterface * formEditor)
用特定的formEditor接口来初始化Widget  
8. virtual bool isContainer() const
用来判断这个自定义控件是否是一个容器类型的控件  
9. virtual bool isInitialized() const
用来判断Widget是否已经进行了初始化  
10. virtual QString name() const
默认返回自定义Widget控件的类名，这里返回的名称就是将来在左侧组件列表中显示的名称  
注意：这里的名称一定不能随意改写，必须和自定义控件的类名完全一样  
如果随意写一个名字，如'CWButton1'，过程中不会报错，但将来拖入到设计界面中会是一个空白的组件，什么都显示不出来  
```
QString CustomButtonPlugin::name() const
{
    return QLatin1String("CustomButton");
}
```
11. virtual QString toolTip() const
在Qt Designer的tool tip中返回一个简短的控件的描述  
当鼠标放在UI界面左侧的控件图标上，就会显示出这个描述  
12. virtual QString whatsThis() const
在Qt Designer的"What's This?" help中返回一个详细的描述  

