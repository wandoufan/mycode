# QUrl

## 基本功能
QUrl提供了一个url对象，可以进行解析和构造  
关于URL的介绍详见http_protocol.md  


## 构造函数
1. QUrl::QUrl(const QUrl &other)
根据其他url对象拷贝出一个新的url对象  

2. QUrl::QUrl()
构造一个空的url对象  

3. QUrl::QUrl(const QString &url, QUrl::ParsingMode parsingMode = TolerantMode)
根据url字符串构造出一个url对象  


## 常用公共函数
1. bool QUrl::isValid() const
判断url对象是否合法  

2. QString QUrl::errorString() const
返回url对象的报错信息，如果没有错误，返回一个空的字符串  

3. QString QUrl::fileName(QUrl::ComponentFormattingOptions options = FullyDecoded) const
返回url中的文件名部分  
注意：如果url路径以\结尾，则文件名会被认为是空；如果url路径中不包含任何\，则整个url路径会被当做文件名返回  

4. QString QUrl::path(QUrl::ComponentFormattingOptions options = FullyDecoded) const
返回url中的路径部分  


## 公共静态函数
1. [static] QUrl QUrl::fromUserInput(const QString &userInput)
根据url字符串返回一个url对象  
```
QString url_string = "http://pic37.nipic.com/20140113/8800276_184927469000_2.png"
QUrl url = QUrl::fromUserInput(url_string);
```