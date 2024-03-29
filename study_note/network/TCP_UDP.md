# TCP协议和UDP协议

## 协议简介
TCP(Transmission Control Protocol)传输控制协议
UDP(User Datagram Protocol)用户数据报协议


## TCP与UDP的比较
1. 连接方式
TCP是有连接的，通信前需要提前建立连接；UDP是无连接的，通信前无需建立连接  
2. 可靠性
TCP可以保证数据可靠，UDP提供不可靠的数据报服务  
3. 传播方式
TCP只能是单播模式，UDP可以实现单播、多播、组播，更加灵活  
一般的即时通讯软件都是基于UDP实现的  
4. C/S架构
TCP是采用C/S架构，要有一个服务端和若干客户端；UDP没有服务端的概念，通信双方是平等的  


## UDP消息传送模式
1. 单播模式(unicast)
一对一数据传输  
2. 组播/多播模式(multicast)
一对多数据传输，只能使用D类IP地址作为组播IP  
3. 广播模式(broadcast)
一对所有数据传输，常用于实现网络发现的协议  


## TCP建立连接的三次握手
1. 客户机的TCP向服务器的TCP发送一个请求报文(不携带应用层的具体数据)
标志位：SYN=1，seq=x
2. 服务器的TCP接收到请求报文后，如果同意连接就像客户机发回确认报文，并为该TCP分配缓存和变量
标志位：SYN=1，ACK=1，seq=y，ack=x+1
3. 客户机收到确认报文后，给服务器也返回确认报文(可以携带应用层数据)，并为该TCP分配缓存和变量
标志位：ACK=1，seq=x+1，ack=y+1


## TCP断开连接的四次挥手
1. 客户机需要关闭连接时，向服务器发送连接释放报文，并停止发送数据，关闭TCP连接
TCP是双全工的，因此此时客户机就无法向服务器再发送数据了，但服务器仍可以向客户机发送数据
标志位：FIN=1，seq=u
2. 服务器收到连接释放报文后发出确认报文，但如果服务器有剩余数据，可以继续发送给客户机
此时从客户机到服务器方向的连接已经释放，TCP处于半关闭状态
标志位：ACK=1，seq=v，ack=u+1
3. 如果服务器向客户机的数据已经发送完毕，就向客户机发送连接释放报文
标志位：FIN=1，ACK=1，seq=w，ack=u+1
4. 客户机收到连接释放报文后发出确认报文，并等待2MSL(最长报文段寿命)的时间后彻底释放了TCP连接
标志位：ACK=1，seq=u+1，ack=w+1