# QNetworkAccessManager

## 基本功能
QNetworkAccessManager用于协调网络操作，允许程序发送网络请求(QNetworkRequest)，以及接收响应(QNetworkReply)  
注意：要在项目中使用Qt网络模块，需要先在.pro文件中加入'QT += network'  


## 工作过程(以HTTP网络文件下载为例)
先根据url构造一个QNetworkRequest对象，通过QNetworkAccessManager对象的get方法获取到一个QNetworkReply响应对象，然后再将响应中的数据内容写入到本地文件中  
```
//构造url和file
QUrl url = QUrl::fromUserInput(url_string);
download_file =new QFile(full_file_path);
download_file -> open(QIODevice::WriteOnly);
//发起网络请求，获取网络响应
request = QNetworkRequest(url);
reply = manage.get(request);
//当有readyRead()信号时
download_file -> write(reply -> readAll());
//当有finished()信号时
download_file -> close();
delete download_file;
download_file = Q_NULLPTR;
reply -> deleteLater();
reply = Q_NULLPTR;
//当有downloadProgress()信号时，显示下载进度
ui -> progressBar -> setMaximum(bytesTotal);
ui -> progressBar -> setValue(bytesReceived);
```


## HTTP请求方法(详见http_protocol.md)
HTTP协议中指定了八种方法/动作来表明对指定URL资源的不同操作方式：  
1. POST(改)：向指定的资源提交数据进行处理请求（例如提交表单或者上传文件），数据被包含在请求数据中，post请求可能会导致新资源的创建或者已有资源的修改
2. GET(查)：向特定的资源发出请求，并返回资源实体
3. PUT(增)：向指定的资源位置上传数据
4. DELETE(删)：请求服务器删除request_url所标识的资源
5. HEAD：和GET一样向服务器请求资源，不过只返回响应头部，不返回具体的信息
6. TRACE：追踪服务器收到的请求，主要用于测试或诊断
7. OPTIONS：返回服务器对特定资源所支持的HTTP请求方法，也可以利用向web服务器发送'\*'的请求来测试服务器的功能性
8. CONNECT：HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器


## 构造函数
1. QNetworkAccessManager::QNetworkAccessManager(QObject \*parent = nullptr)


## 常用公共函数
1. void QNetworkAccessManager::connectToHost(const QString &hostName, quint16 port = 80)
根据给定的主机和端口建立起一个连接  
这个函数一般在HTTP request之前调用，用来和一个主机完成TCP握手  
备注：QAbstractSocket中也有一个connectToHost()函数  

2. QNetworkReply \*QNetworkAccessManager::get(const QNetworkRequest &request)

3. QNetworkReply \*QNetworkAccessManager::deleteResource(const QNetworkRequest &request)

4. QNetworkReply \*QNetworkAccessManager::head(const QNetworkRequest &request)

5. QNetworkReply \*QNetworkAccessManager::post(const QNetworkRequest &request, QIODevice \*data)

6. QNetworkReply \*QNetworkAccessManager::post(const QNetworkRequest &request, const QByteArray &data)

7. QNetworkReply \*QNetworkAccessManager::put(const QNetworkRequest &request, QIODevice \*data)

8. QNetworkReply \*QNetworkAccessManager::put(const QNetworkRequest &request, const QByteArray &data)


## 信号函数
1. [signal] void QNetworkAccessManager::finished(QNetworkReply \*reply)
当网络响应完成时发出该信号，其中reply参数为刚才完成的网络响应的指针  
备注：这个信号是跟随着QNetworkReply::finished()信号发出的  
注意：不要在该信号关联的槽函数中去删除reply对象，使用deleteLater()函数去删除  