# 主要介绍python的主流web框架


## 一些相关概念
* 1.WSGI(Web Server Gateway Interface)
* WSGI不是服务器、python模块、框架、API或任何软件，而是描述web服务端和客户端通信的规范协议
* 要实现WSGI协议，必须同时实现web服务端和客户端，主流的python web框架flask、django、tornado都是基于WSGI规范实现的  

* 2.uwsgi
* uwsgi是一种线路协议而不是通信协议，常用于在uWSGI服务器与其他网络服务器的数据通信，定义传输信息的类型

* 3.uWSGI
* uWSGI是实现了WSGI、uwsgi、http等协议的web服务器
* uWSGI支持的并发量比较低，一般会用nginx等代理做缓冲，避免并发量过大时服务直接挂掉

* 4.Nginx+uWSGI+应用程序的架构
* 客户端(浏览器) ——> 反向代理(nginx) ——> uWSGI ——> 应用程序(flask/django/tornado)


## django(大而全)
* django采用MVC的架构模式，是python最全能的web开发框架，可维护性和开发速度也很好
* 但django在与数据库的交互上相对比较慢，django的同步特性导致吞吐量小的问题，可以通过Celery等解决
* 是否选用django，取决于项目对数据库交互的要求以及各种优化
* django的项目代表：Instagram，Guardian


## flask(小而精)
* flask是微框架的典范，具有很好的的灵活性
* flask可以自由选择自己的数据库交互组件（通常是Flask-SQLAlchemy），
* 加上celery+redis等异步特性以后，flask也会具有很好的性能


## tornado(性能高)
* tornado最大的优点是性能高，但tornado相比django是较为原始的框架，许多功能需要自己去实现 
* tornado项目代表：知乎


## 常见的架构模式

### MVC(Model-View-Controller)
* 1.MVC的组件包括
* view(外层):用于显示给用户的视图页面，即通过浏览器加载的html数据
* controller(中间层):连接model和view，用于控制应用程序的流程和视图页面的业务逻辑
* model(内层):用于封装与应用程序的业务逻辑相关的数据和数据处理方法
* 2.MVC的特点
* MVC可以实现应用程序中的业务模型和视图页面中的展示逻辑分离，更加容易开发、维护
* 3.MVC的流程
* view接收指令，然后传递给controller
* controller完成业务逻辑后，要求model改变相应的状态
* model将新的数据发送给view，view将改动渲染在视图上
* 4.MVC的优点
* 业务层和视图层分离，耦合性更低，修改view代码不用重新编译model和controller的代码
* 重用性高、可维护性高、部署快
* 5.MVC的缺点
* 不适合中小型的应用程序，部署成本过高，得不偿失
* view层访问model层的数据时效果太低，不利于性能

### MVP(Model-View-Presenter)
* 参考资料：
> https://blog.csdn.net/victoryzn/article/details/78392128

### MVVM(Model-View-ViewModel)