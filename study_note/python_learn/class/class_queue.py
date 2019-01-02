class Queue:
    list1 = []

    def push(self, data):
        self.list1.append(str(data))

    def pop(self):
        while len(self.list1) == 0:
            print('cannot pop from a empty queue')
        else:
            self.list1.pop(0)

    def show(self):
        print(self.list1)

queue1 = Queue()
queue1.push('a')
queue1.push('b')
queue1.push('c')
queue1.pop()
queue1.show()
