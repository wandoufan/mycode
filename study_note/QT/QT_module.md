# QT中的组件

----------------------------/*常用的组件*/-------------------------------

1. 实际使用中发现：
如果选择plainTextEdit组件，则设置文本的下划线、斜体、粗体都正常
但如果选择了TextEdit组件，只有设置文本下划线是正常的
文本的斜体和粗体只能在程序运行之后再写入文字才能生效，且生效仅限一次
在编译之前就写好的文字则无法生效
2. checkBox(方块勾选)和radioButton(圆圈勾选)两种组件之间的区别：
多个checkBox可以同时选择，多个radioButton只能选择其中一个


----------------------------/*组件的属性*/-------------------------------

## objectName属性
对于窗体上创建出的每一个组件，都有一个objectName属性作为组件实例的名称  
具体属性值由系统自动创建，一般按照组件创建顺序来命名，例如checkBox、checkBox_2、checkBox_3  
objectName作为组件的唯一标识，每个组件的objectName都不相同  
objectName需要在设计程序之前设置好，设置好后不要再改动，否则代码也要相应改动  


## checkable属性
1. 基本概念
对于继承于QAbstractButton类的Button组件都有一个checkable属性，用来设置按钮状态  
未勾选checkable时，Button为触发按钮(trigger button)，按下去马上弹起来  
勾选checkable后，Button变成切换按钮(toggle button)，可以有两种状态：按下/弹起  
备注：toggle可以理解为开关，可以勾选为开或关的状态；而trigger可以理解为扳机，只点击一次  
2. 大部分Button的checkable默认是不选中的，包括：  
pushButton、toolButton  
3. 少部分Button的checkable默认是选中的，包括： 
radioButton、checkBox  