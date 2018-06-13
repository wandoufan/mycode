#coding:utf-8


#网络编程
#套接字(句柄)socket包含ip地址和端口，可以实现不同计算机或虚拟机之间进程的通信
#套接字两种类型：面向连接的TCP协议，无连接的UDP协议
#套接字之间连接过程可以分为三个步骤：服务器监听、客户端请求、连接确认

#导入套接字模块
import socket

#第一个参数地址，127.0.0.1代表本机，第二个参数端口
server_add=('127.0.0.1',996)

#生成套接字socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
#第一个参数family包括AF_INET(表示服务器间通信)(默认值)和AF_UNIX(用于unix系统内部进程通信)
#第二个参数type包括SOCK_STREAM(表示TCP/IP)(默认值)和SOCK_DGRAM(表示UDP/IP)
#后两个参数一般不写
sk=socket.socket()
#将主机地址和句柄绑定
sk.bind(server_add)
#开始监听
sk.listen()

while True:
    print('server listening...')
    #s.accept返回一对值(conn, address) ,conn是一个新的套接字用于
    #在该用户的连接中发送和接收数据，address是用户的地址
    con,addr=sk.accept()

    while True:
        #s.recv(bufsize)接收TCP套接字的内容，参数表示一次接收数据的最大值
        #返回一个bytes类型的对象，s.recvfrom()接收UDP套接字的内容
        client_data=con.recv(1024)

        if not client_data:
            break

        print(client_data)
        #s.send(bytes)发送bytes类型的数据，返回发送的字节数量，对于大量数据可能要一次发送
        #s.sendall()一次性发送所有数据
        #s.sendto()发送UDP类型数据，上面两个都是TCP
        con.send(client_data)
    #关闭套接字
    con.close()
    
