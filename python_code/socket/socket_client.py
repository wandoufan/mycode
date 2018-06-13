#coding:utf-8

import socket
#服务端地址
server_add=('127.0.0.1',996)
#生成套接字
sk=socket.socket()
#连接到(address,port)
sk.connect(server_add)

for i in range(5):

    send_data=input()

    sk.send(bytes(send_data,'utf8'))

    server_reply=sk.recv(1024)

    print(server_reply)

sk.close()