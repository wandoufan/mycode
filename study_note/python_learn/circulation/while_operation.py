#if后条件为真，就会执行一次相应的代码；while中代码块会一直执行，直到循环条件不再为真；while循环具有条件性

#while可以用作计数循环
count=0
while count<4:
    print(count)
    count+=1

#while可以用做无限循环，无限循环不一定是坏事，如服务器就是利用它来一直等待客户端的消息
def wait_for_client_connect():
    out_data='connect success!'
while True:
    server_action=wait_for_client_connect()
