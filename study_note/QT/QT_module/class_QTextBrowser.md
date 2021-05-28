# QTextBrowser

## 基本功能
QTextBrowser提供了一个富文本浏览器，可以用来显示各种文本信息  
QTextBrowser类继承于QTextEdit类  


## 使用技巧
textBrowser等显示类的组件可以通过setText(str)方法把内容显示输出出来  
但使用setText()方法会清空原有数据  
如果是显示日志等内容，需要采用追加模式，不清空原有数据，则使用append()方法  
备注：append()方法不是QTextBrowser类中的方法，而是QTextEdit类中的方法  
另外，当内容增多，显示不完时，textBrowser会自动出现一个上下滑动块  
如果内容是中文的，需要加上QString::fromLocal8Bit，否则显示乱码
```
ui -> message_column -> setText(QString::fromLocal8Bit("这是测试"));
```