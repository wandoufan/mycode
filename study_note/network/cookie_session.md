# 主要记录cookie和session的知识点

* 参考资料：
> https://www.cnblogs.com/xdp-gacl/p/3803033.html
> https://www.cnblogs.com/andy-zhou/p/5360107.html


## cookie机制(客户端)
* cookie就是由服务器颁发给客户端的特殊信息，例如用户名等个性信息
* 这些信息以文本形式存放在客户端，客户端每次向服务器发送请求时都会把cookie信息放在http的请求头中一起发给服务器端
* 服务器端会根据收到的cookie信息动态生成和该客户端对应的内容
* 例子：网站登录时的记住账户密码就是根据cookie机制实现的

## cookie的特点
* cookie具有有效期，由其中的maxAge来决定，单位为秒
* cookie不可以跨域名使用，防止非法网站获取其他网站的cookie
* 单个cookie在客户端的限制是3K，即一个站点在客户端存放的cookie不能超过3K

### http协议识别不同的用户
* 网络中的会话跟踪是重要的功能，可以区分出不同用户的请求操作
* 而http协议是无连接的，数据交换完毕后客户端就会和服务器端断开连接，因此服务器无法从连接上追踪会话
* cookie机制可以弥补http协议无连接的缺点，可以看做http协议的扩展


## session机制(服务器端)
* 客户端浏览器访问服务器时，服务器把客户端信息以某种形式记录在服务器上，这就是session
* 客户端浏览器再次访问时，可以从session中查找该客户的状态
* 服务器面会为每一个用户在内存中保存一份seesion，用户较多时会产生内存溢出
* 为节约内存资源，服务器会把长时间为访问的用户的session从内存中删除，即超时时间


## cookie和session的区别
* cookie是客户端技术，而seesion是服务器端的技术
* cookie相对不安全，可能会被cookie欺骗，考虑安全应该使用session
* 较多的session会影响服务器性能，考虑减轻服务器压力应该使用cookie
