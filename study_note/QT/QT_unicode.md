# QT中的编码问题

## 中文显示乱码问题
步骤1：  
QTcreator界面点击工具–选项，选择文本编辑器—行为一栏，找到文件编码格式模块  
默认编码选择utf-8，下面的utf-8 BOM选项更改为如果编码是utf-8则添加  
步骤2：  
在头文件中加入以下代码  
```
#if _MSC_VER >= 1600
#pragma execution_character_set("utf-8")
#endif
```
步骤3：  
对项目进行清理，然后重新构建  
