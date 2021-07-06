# QT中的类

----------------------------/*QT常用类*/-------------------------------



## QChar
QChar类提供了一个16位编码的字符  
QChar是16位的，因此可以用来存储汉字，一个字符存储一个汉字  


## QFont
QFont类是专门用于管理文本的字体  
```
QFont font = ui -> textEdit -> font();
font.setUnderline(checked);
ui -> textEdit -> setFont(font);
```
**QFont常用函数**
setFamily() 设置字体  
setBold() 字体加粗  
setItalic() 斜体  
setOverline() 上划线  
setUnderline() 下划线  
setStrikeOut() 删除线  
setPointSize() 设置字体肉眼看到的实际大小，在不同设备上显示大小相同  
setPixelSize() 设置字体像素单位的大小，在不同设备上显示大小可能不同  



## QFileDevice
QFileDevice类提供了接口用来从打开文件中读文件和写文件，其父类是QIODevice  



