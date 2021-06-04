# QNetworkReply

## 基本功能
QNetworkReply提供了一个request对应的网络响应对象，包含了具体的数据和请求头  
QNetworkReply提供了很多信号函数可以检测网络响应的执行情况，并执行相应的操作  
备注：QNetworkReply是继承于QIODevice的子类，因此支持数据流读写功能，也支持异步或同步工作模式  
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
注意：QT帮助文档中没有提供任何构造函数，reply对象一般都是通过QNetworkAccessManager对象的各种请求方法获得的返回值  


## 常用公共函数
1. QNetworkAccessManager \*QNetworkReply::manager() const
返回对应的QNetworkAccessManager对象  

2. QNetworkRequest QNetworkReply::request() const
返回对应的QNetworkRequest对象  

3.  QUrl url() const
返回对应的QUrl对象  

4. bool QNetworkReply::isFinished() const
当reply已经完成或者被中断时，返回true  

5. bool QNetworkReply::isRunning() const
当request正在运行，reply还没有完成时返回true  

6. qint64 QNetworkReply::readBufferSize() const
返回读入的缓冲区大小，单位字节  

7. [virtual] void QNetworkReply::setReadBufferSize(qint64 size)
设置读入缓冲区大小，单位字节  


## 信号函数
备注：另外还有一些继承于QIODevice的信号函数，如readyRead()等  
1. [signal] void QNetworkReply::finished()
当响应完成时发出该信号  
在该信号发出之后，QNetworkReply对象中的数据不会再有更新  
除非调用了close()或abort()函数，否则QNetworkReply对象中的数据还可以用read()或readAll()去读取  
备注：这个信号会和QNetworkAccessManager::finished()信号一起发出  
注意：不要在该信号关联的槽函数中去删除reply对象，使用deleteLater()函数去删除  

2. [signal] void QNetworkReply::downloadProgress(qint64 bytesReceived, qint64 bytesTotal)
这个信号是用来指示网络请求的下载进度，函数参数经常在progressBar控件进行显示  
如果在网络请求中没有进行下载，则该信号只会被发出一次，且两个参数值都为0  
bytesReceived参数为已经下载的数据量  
bytesTotal参数为总共需要下载的数据量，如果要下载的数据量未知，该参数值为-1  
备注：当bytesReceived等于bytesTotal时，下载完成，此时bytesTotal值不会是-1  
```
void MainWindow::on_downloadProgress(qint64 bytesReceived, qint64 bytesTotal)
{
    //downloadProgress()信号的响应函数, 显示下载进度
    ui -> progressBar -> setMaximum(bytesTotal);
    ui -> progressBar -> setValue(bytesReceived);
}
```




