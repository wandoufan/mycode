# QLatin1Char

## 基本功能
QLatin1Char类提供了一个8位的ASCII/Latin-1字符  
这个类只有在使用8位字符构建一个QChar时才有用  

## 构造函数
1. QLatin1Char::QLatin1Char(char c)
使用字符c构造一个Latin-1字符  
备注：只有确定输入字符的编码是Latin-1时，才能使用这个构造函数  


## 公共函数
1. char QLatin1Char::toLatin1() const
把Latin-1字符转换成一个8位的ASCII字符  

2. ushort QLatin1Char::unicode() const
把Latin-1字符转换成一个16位编码的Unicode字符  