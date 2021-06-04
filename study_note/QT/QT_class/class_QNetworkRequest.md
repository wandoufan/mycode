# QNetworkRequest

## 基本功能
QNetworkRequest提供了一个request对象，可以被QNetworkAccessManager发送出去  
它包含了一个URL以及一些可以用来修改请求的辅助信息，支持HTTP、FTP和局部文件URLs的下载或上传  
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


## 构造函数
1. QNetworkRequest::QNetworkRequest(const QNetworkRequest &other)
根据其他request对象拷贝一个新的request对象  

2. QNetworkRequest::QNetworkRequest(const QUrl &url)
根据给定的url创建一个request对象  
```
QUrl url = QUrl::fromUserInput(url_string);
QNetworkRequest request; //网络请求
request = QNetworkRequest(url);
```

3. QNetworkRequest::QNetworkRequest()
创建一个空的request对象  


## 常用公共函数
1. QUrl url() const
返回url  

2. void setUrl(const QUrl &url)
设置url  

3. int QNetworkRequest::transferTimeout() const
返回传输的超时时间，单位毫秒  
如果之前没有调用过setTransferTimeout()函数，则timeout为0，即没有设置timeout  

4. void QNetworkRequest::setTransferTimeout(int timeout = DefaultTransferTimeoutConstant)
设置传输的超时时间，单位毫秒  
timeout参数默认值为DefaultTransferTimeoutConstant，即30000毫秒  

5. void QNetworkRequest::swap(QNetworkRequest &other)
把当前request对象和另一个request对象互换  