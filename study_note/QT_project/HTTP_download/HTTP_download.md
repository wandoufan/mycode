# 通过HTTP实现网络文件下载的demo

## 工作过程
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