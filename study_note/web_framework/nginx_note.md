# 主要介绍nginx


## 相关基本概念
* 1.正向代理
* 正向代理一般作用在客户端，客户端的浏览器通过代理将http请求转发到目标web服务器上
* 客户端上需要配置正向代理服务器的ip和端口，才能实现请求转发
* 例如，在客户端上安装的翻墙软件就是正向代理服务器
* 2.反向代理
* 反向代理一般作用在服务端，代理接收客户端的请求，将请求分发给具体的服务器进行处理
* 然后将服务器的响应报文再反馈给客户端，客户端不知道反向代理的存在，也不需要做特别设置
* 例如，nginx服务器就是反向代理服务器


## 反向代理的作用
* 1.安全
* 客户端对web服务器的访问需要经过反向代理服务器，可以防止外部程序对web服务器的直接攻击
* 2.负载均衡
* 在有多个web服务器的情况下，反向代理可以根据各个服务器的负载情况动态的转发http请求给负载低的服务器
* 3.提升web服务器的I/O性能
* http请求报文直接从客户端发送到web服务器，会让web服务器专门花费时间来接收I/O请求
* 反向代理服务器可以完整的接收整个http请求后，再转发给web服务器


## nginx简介
* nginx是一个高性能的web服务器和反向代理服务器，也是一个IMAP/POP3/SMTP代理服务器
* nginx上可以放置静态文件，客户端可以直接访问nginx上的静态文件
* nginx和apache类似，但在高并发的情况下性能更好
* nginx代理和后端Web服务器间无需长连接
* nginx可以一边接收来自服务器的响应报文，一边向客户端转发响应报文
* nginx是跨平台的，可以在大多数类UNIX系统和windows系统下运行
* nginx还具有内存消耗小，稳定性高的特点


## nginx与uWSGI工作过程
* 客户端(浏览器) —http协议—> 反向代理(nginx) —uwsgi协议—> uWSGI ——> 应用程序(flask/django/tornado)
* 如果是静态文件请求就根据nginx配置的静态文件目录，返回请求的资源
* 如果是动态请求，nginx会把http协议的请求转换为uwsgi协议传递给uWSGI
* uWSGI通过WSGI和web程序通信并获取到响应结果，通过uwsgi协议发给nginx，最后nginx以http协议响应给用户


## nginx的安装配置
* 参考资料
> http://www.runoob.com/linux/nginx-install-setup.html
> https://blog.csdn.net/eightbrother888/article/details/79503716