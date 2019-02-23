#用两个栈实现一个队列
#注意，python中没有栈类型，用列表类型代替，二者属性相同
class Queue_by_two_stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,data):
        self.stack1.append(data)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return None

queue=Queue_by_two_stack()
queue.push('a')
queue.push('b')
queue.push('c')
#print(queue.pop())

#用两个队列实现一个栈

class Stack_by_two_queue:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]
    def push(self,data):
        self.queue1.append(data)
    def pop(self):
        if self.queue1:
            while len(self.queue1)>1:
                self.queue2.append(self.queue1.pop(0))
            if len(self.queue1)==1:
                return self.queue1.pop()
        elif self.queue2:
            while len(self.queue2)>1:
                self.queue1.append(self.queue2.pop(0))
            if len(self.queue2)==1:
                return self.queue2.pop()
        else:
            return None

stack=Stack_by_two_queue()
stack.push('a')
stack.push('b')
stack.push('c')
stack.pop()
stack.push('d')
stack.push('e')
stack.pop()
print(stack.pop())

