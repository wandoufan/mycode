class Stack():
    list1 = []

    def push(self, data):
        self.list1.append(data)

    def pop(self):
        while len(self.list1) == 0:
            print('stack is empty')
        else:
            self.list1.pop(-1)

    def show(self):
        print(self.list1)

s1=Stack()
s1.push('a')
s1.push('b')
s1.push('c')
s1.pop()
s1.show()
