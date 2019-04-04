#  用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push

class Stack():

    def __init__(self):
        """
        用列表代表数组结构，用一个指针指向左右两个栈的界限
        """
        self.array = []
        self.pointer = 0

    def l_pop(self):
        if self.pointer > 0:
            self.pointer -= 1
            return self.array.pop(0)
        else:
            return 'left Stack is empty'

    def l_push(self, num):
        self.array.insert(0, num)
        self.pointer += 1

    def r_pop(self):
        if self.pointer < len(self.array):
            return self.array.pop()
        else:
            return 'right Stack is empty'

    def r_push(self, num):
        self.array.append(num)

    def show(self):
        print('数组:', self.array)
        print('左栈:', self.array[:self.pointer])
        print('右栈:', self.array[self.pointer:])
        print('\n')


my_stack = Stack()

print('左栈入栈：')
for i in range(5, 9):
    my_stack.l_push(i)
my_stack.show()

print('右栈入栈：')
for j in range(1, 5):
    my_stack.r_push(j)
my_stack.show()

print('左栈出栈')
for i in range(2):
    print(my_stack.l_pop())
my_stack.show()

print('右栈出栈')
for i in range(6):
    print(my_stack.r_pop())
my_stack.show()
