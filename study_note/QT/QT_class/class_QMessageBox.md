# QMessageBox

## 基本功能
QMessageBox类可以弹出一个对话框来通知用户或询问用户并获得回答  
父类：QDialog  


## 注意事项
如果弹窗中的中文变成了乱码，需要进行如下格式转换  
```
 QMessageBox::about(NULL, QString::fromLocal8Bit("警告"), QString::fromLocal8Bit("库文件function.dll加载失败！"));
```


## 公共静态成员方法
备注：以下方法都可以直接使用，不需要实例化对象  
1. information函数用来显示通知信息，对话框为一个感叹号  
```
QMessageBox::StandardButton QMessageBox::information(QWidget \*parent, const QString &title, const QString &text, QMessageBox::StandardButtons buttons = Ok, QMessageBox::StandardButton defaultButton = NoButton)
```
函数会在widget父类前面弹出一个对话框，并显示指定的标题和文本内容  
当用户按下'enter'时会触发一个默认按钮，默认按钮用第五个参数进行设置  
当用户按下'esc'时会退出对话框，相当于调用了'escape button'  
备注：如果QMessageBox的在函数参数中指定了父类，则在对话框运行时不能删除其父类  
第一个参数设置父控件指针，可以设为NULL  
第二个参数设置对话框标题  
第三个参数设置对话框内容  
第四个参数设置窗口中的按钮个数及形式(默认为OK)  
第五个参数设置用户按下'enter'时的触发按钮，默认'NoButton'由QMessageBox自动选择  
```
QMessageBox::information(NULL, "title", "content", QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes);
```

2. critical函数用来显示比较严重的警告信息，对话框为一个叉号  
```
QMessageBox::StandardButton QMessageBox::critical(QWidget \*parent, const QString &title, const QString &text, QMessageBox::StandardButtons buttons = Ok, QMessageBox::StandardButton defaultButton = NoButton)
```

3. question函数用来向用户询问问题并让用户进行选择，对话框为一个问号  
```
QMessageBox::StandardButton QMessageBox::question(QWidget \*parent, const QString &title, const QString &text, QMessageBox::StandardButtons buttons = StandardButtons(Yes | No), QMessageBox::StandardButton defaultButton = NoButton)
```
```
if(QMessageBox::Yes == QMessageBox::question(NULL, "提示", info, QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes))
```

4. about函数用来弹出一个简单的对话框，对话框中没有标识符  
```
void QMessageBox::about(QWidget \*parent, const QString &title, const QString &text)
```
```
QMessageBox::about(NULL, "about", "this is about");
```