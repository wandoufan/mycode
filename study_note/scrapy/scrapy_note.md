# 主要记录爬虫方面的基本知识：
* 参考资料：
> http://www.runoob.com/w3cnote/python-spider-intro.html


## python爬虫的一般流程

### 1.发起请求
* 使用http库向目标站点发送一个request请求，需要构建一个合理的url

### 2.获取相应内容
* 如果服务器正常相应，会通过网页下载器获得一个response，response是一个网页字符串，包含网页中的html、json、图片、视频等
* 常用的库包括：
  * urllib(python自带的库)
  * requests(第三方库)

### 3.网页内容解析
* 通过各种工具从网页字符串中提取出我们需要的内容
* 常用的库包括：
  * 正则表达式re(直观的从网页字符串中提取内容，但当网页比较复杂时使用比较困难)
  * html.parser(python自带的解析工具)
  * beautifulsoup(第三方库，功能强大，可以解析html和xml)
  * lxml(第三方库，可以解析html和xml)
  * pyquery(第三方库，用来解析网页)

### 4.保存数据
* 将从网页中解析出的数据保存起来
* 常用的数据库包括：
  * mysql
  * redis


## 构建url头部信息
* 构建一个合理的头部header才可以伪装成合法的浏览器请求，避免被反爬机制拦截
* 对urllib库和requests库的构建方法进行补充...



## 爬取带有登录机制的网站


## 反爬虫机制
* 参考资料：
> https://blog.csdn.net/offbye/article/details/52235139

* 1.构造合理的HTTP请求头
* 2.设置cookie
* 3.正常的时间访问路径
* 4.注意隐含输入字段值
* 5.避开蜜罐
* 6.使用远程服务器来避免IP封锁