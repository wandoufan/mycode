# QDesignerContainerExtension

## 基本功能
当执行一个自定义的多页面容器类型控件时，必须使用QDesignerContainerExtension类  
这个类提供了扩展功能：允许你在QT designer中对一个多页面容器类型控件添加或删除页面  


## QT designer中的功能扩展
QT designer支持以下四种功能的自定义扩展  
1. QDesignerTaskMenuExtension
选中控件点击右键时显示的菜单  
2. QDesignerPropertySheetExtension
UI界面右下角的属性编辑器  
3. QDesignerMemberSheetExtension
给控件连接信号与槽函数时，显示的相关的信号与槽函数  
4. QDesignerContainerExtension
自定义的多页面容器类型控件  