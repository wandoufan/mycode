# import threading
import os
# if not os.path.isdir('C:/b.log'):
#     print('yes')
# else:
#     print('no')

print(os.path.isfile('C:/b.log'))

# class Foo():
#     def __init__(self):
#         self.count = 0
#         self.continue_ = True

#     def terminate(self):
#         self.continue_ = False

#     def run(self):
#         while self.continue_:
#             self.count += 1
#             print 'count to %s ****' % self.count
#         print 'Terminated!'


# def bar(i):
#     print 'i am bar %s!' % i

# def main():

#     foo = Foo()
#     t_foo = threading.Thread(target=foo.run)
#     t_foo.start()
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=bar, args=(i,))
#         thread_list.append(t)


#     for t in thread_list:
#         t.start()

#     for t in thread_list:
#         t.join()
#     foo.terminate()
#     t_foo.join()

# if __name__ == '__main__':
#     main()