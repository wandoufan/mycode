# 主要记录http协议的知识点

* 参考资料：
> https://www.cnblogs.com/ranyonsue/p/5984001.html  
> http://www.runoob.com/http/http-tutorial.html

## http协议简介
* http协议(hyper text tansfer)即超文本传输协议，用于web服务器传输超文本到本地浏览器的传送协议
* http协议工作在应用层，由请求和响应构成，默认HTTP的端口号为80，HTTPS的端口号为443


## http协议特点
* 1.简单快速：客户向服务器请求服务时只需要传送请求方法和协议
* 2.传输灵活：http协议允许传输任意类型的数据对象，正在传输的类型由content-type加以标记
* 3.无连接：每次连接只处理一个请求，处理完请求后就断开连接，采用这种方式可以节省传输时间
* 4.无状态：无状态指协议对事务处理没有记忆能力，缺少状态意味如果后续处理需要前面的信息，则必须重传一次
* 5.支持B/S架构和C/S架构


## http协议工作过程
* 1.客户端连接到web服务器
* 客户端(通常是浏览器)向DNS服务器请求解析URL中域名所对应的IP地址
* 根据IP地址与web服务器的http端口(默认为80)建立一个tcp的套接字连接
* 2.发送http请求
* 客户端通过tcp套接字向web服务器发送一个文本的请求报文request
* 3.服务器接受请求并返回http响应
* web服务器解析请求，定位请求资源并将资源写入到tcp套接字，由客户端读取response
* 4.释放tcp连接
* 如果数据传输完毕，就可以断开tcp连接
* 5.客户端浏览器解析html内容
* 客户端浏览器首先解析状态行查看请求是否成功，如果请求成功则读取响应数据中的html，根据html语法对其格式化，并在浏览器窗口显示


## URL简介
* HTTP使用统一资源标识符uri(Uniform Resource Identifiers)来传输数据和建立连接
* url(uniform resource locator)即统一资源定位符，用来表示网络上某一处资源的地址，是一种具体的uri
* 一个如下示例的url包括以下几个部分：
```
http://www.aspxfans.com:8080/news/index.asp?boardID=5&ID=24618&page=1#name
协议         域名        端口 虚拟   文件名          参数部分           锚部分
```
* 1.协议部分：开头的http表示网页使用的是http协议，http之后用'//'作为分隔符
* 2.域名部分：url中的域名也可以用ip地址来代替
* 3.端口部分：端口和域名之间用':'作为分隔符，端口不是url的必要部分，如果省略端口就采用默认端口
* 4.虚拟目录部分：从第一个'/'到最后一个'/'中间的部分是虚拟目录，虚拟目录也不是一个url的必要部分
* 5.文件名部分：从最后一个'/'到'?'中间的部分是文件名；如果没有'?'，则从最后一个'/'到'#'中间的部分是文件名；如果没有'?'和'#'，则从最后一个'/'到url结束中间的部分是文件名；文件名也不是url的必要部分，如果省略文件名就采用默认文件名
* 6.锚部分：从'#'到url结束中间的部分是锚部分，锚部分也不是url的必要部分
* 7.参数部分：从'?'开始到'#'中间的部分是参数(搜索、查询)部分，参数部分可以包括多个参数，中间用'&'作为分隔符

* 注意：参数部分又称为查询参数、请求参数、请求数据，一般以字典格式传入，其中每个参数可以有多个值，但值不能为None
```
https://www.baidu.com/?key1=value1&key2=value2&key4=value3&key4=value4
```


## 请求消息request
* 一个请求报文包括请求行、请求头部、空行和请求数据4部分
* 1.请求行(request line)
* 请求行主要说明请求类型、需要访问的资源以及使用的http版本
```
GET /chapter1/user.html HTTP/1.1
请求方法     URL         协议版本    
```
* 2.请求头部(header)
* 请求头部中包含多组字段名-字段值，用来说明服务器要使用的附加信息
* 请求头部参考表：http://tools.jb51.net/table/http_header
```
Host    img.mukewang.com
请求的服务器的域名和端口号
User-Agent    Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36
发出请求的用户信息
Accept    image/webp,image/*,*/*;q=0.8
客户端能够接收的内容类型
Referer    http://www.imooc.com/
之前网页的地址
Accept-Encoding    gzip, deflate, sdch
浏览器支持的内容压缩编码类型
Accept-Language    zh-CN,zh;q=0.8
浏览器可以接受的语言
```
* 3.空行
* 请求头部后面必须空一行，即使第四部分请求数据为空，这里也必须是空行
* 4.请求数据
* 请求数据也称为主体，是客户端要提交给服务器的数据，可以添加任意数据


## http请求方法
* HTTP协议中指定了八种方法/动作来表明对指定URL资源的不同操作方式 ：
* 1.POST(改)：向指定的资源提交数据进行处理请求（例如提交表单或者上传文件），数据被包含在请求数据中，post请求可能会导致新资源的创建或者已有资源的修改
* 2.GET(查)：向特定的资源发出请求，并返回资源实体
* 3.PUT(增)：向指定的资源位置上传数据
* 4.DELETE(删)：请求服务器删除request_url所标识的资源
* 5.HEAD：和GET一样向服务器请求资源，不过只返回响应头部，不返回具体的信息
* 6.TRACE：追踪服务器收到的请求，主要用于测试或诊断
* 7.OPTIONS：返回服务器对特定资源所支持的HTTP请求方法，也可以利用向web服务器发送'\*'的请求来测试服务器的功能性
* 8.CONNECT：HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器


## post请求和get请求的区别
* post请求示例：
```
POST / HTTP/1.1
Host: www.wrox.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6)
Gecko/20050225 Firefox/1.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 40
Connection: Keep-Alive

name=Professional%20Ajax&publisher=Wiley
```

* get请求示例：
```
GET /books/?sex=man&name=Professional HTTP/1.1
Host: www.wrox.com
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.6)
Gecko/20050225 Firefox/1.0.1
Connection: Keep-Alive
```

* 1.get方法提交的数据放在请求行的url之后，url和传输数据以'?'分隔，参数之间以'&'分隔，而post方法提交的数据放在请求数据中
* 即get方法提交的数据会在地址栏中显示出来，而以post方法提交地址栏不会有改变
* 2.get方法提交的数据大小会有限制(因为部分浏览器对url的长度有限制)，post方法提交的数据没有大小限制
* 备注：http协议本身对传输的数据和url的大小没有限制
* 3.get方法提交的数据会明文出现在url上，而post方法提交的数据不会出现在url中，post方法的安全性比get方法要高
* 4.get方式需要使用Request.QueryString来取得变量的值，而post方式通过Request.Form来获取变量的值


## 响应消息response
* 一个响应报文包括状态行、消息报头、空行和响应正文4部分
* 1.状态行
* 状态行主要包括http版本、状态码、状态消息
```
HTTP/1.1 200 OK
```
* 2.消息报头
* 消息报头包含多组字段名-字段值，主要说明客户端要使用的一些附加信息
* 消息报头参考表：http://tools.jb51.net/table/http_header
```
Date: Fri, 22 May 2009 06:07:21 GMT
生成响应的时间
Content-Type: text/html; charset=UTF-8
数据格式和编码类型
```
* 3.空行
* 消息报头之后必须空一行
* 4.响应正文
* 响应正文是服务器返回给客户端的文本信息
```
<html>
      <head></head>
      <body>
            <!--body goes here-->
      </body>
</html>
```


### http状态码
* http的状态码共分为5类：
* 1xx：指示信息--表示请求已接收，继续处理
* 2xx：成功--表示请求已被成功接收、理解、接受
* 3xx：重定向--要完成请求必须进行更进一步的操作
* 4xx：客户端错误--请求有语法错误或请求无法实现
* 5xx：服务器端错误--服务器未能实现合法的请求

* 常见的状态码包括：
```
200 OK                        //客户端请求成功
400 Bad Request               //客户端请求有语法错误，不能被服务器所理解
401 Unauthorized              //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用 
403 Forbidden                 //服务器收到请求，但是拒绝提供服务
404 Not Found                 //请求资源不存在，eg：输入了错误的URL
500 Internal Server Error     //服务器发生不可预期的错误
503 Server Unavailable        //服务器当前不能处理客户端的请求，一段时间后可能恢复正常
```

* 状态码查询表
> http://www.runoob.com/http/http-status-codes.html


## https协议
* 待完善...