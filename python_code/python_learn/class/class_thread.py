import threading
import os
import time

# 调用线程Train和Readlog,两个线程交替执行

class Train(threading.Thread):
    # 负责生成日志文件，不断向日志中写入数据
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.train()

    def train(self):
        count = 1
        while True:
            with open('C:/b.log','w') as file:
	            if count<10:
	                count +=1
	                print('count is %d' %count)
	                file.write(str(count)+'\n')
	                file.close()
	                time.sleep(1)
	            else:
	                file.write('x'+'\n')
	                file.write('abc')
	                file.close()
	                print('train finish!')
	                break

class Readlog(threading.Thread):
    # 负责读日志文件中的数据
    def __init__(self):
        threading.Thread.__init__(self)
        self.continue_ = True

    def run(self):
        self.readlog()


# 备注：readlog中的while循环是双层循环，所以只能在循环过程中不断去判断标志位的值
# 如果是单层循环，可以直接写成 ‘while self.continue_:’
    def readlog(self):
        while True:
            if not os.path.isfile('C:/b.log'):
                print('waiting for log file.......')
                time.sleep(2)
            else:
                with open('C:/b.log','r') as log:
                    for eachline in log:
                        if self.continue_ == False:
                        	break
                        else:
	                        #time.sleep(1)
	                        print('this is log file:',eachline)
	                        if eachline == 'x'+'\n':
	                            print('readlog finish!')
	                            break
                    break

    def terminate(self):
    	#方法一：修改标志位退出线程
    	self.continue_ = False
    	print('stop readlog')
    	#方法二：强制退出线程任务
    	#os._exit(0)
    	

#文件不能同时读写？？t1,t2不能同时运行？？
#尝试修改写一个数据就关闭文件,也不行？？
class Start():

	def begin(self):
		t1 = Train()
		t2 = Readlog()

		t1.start()
		t2.start()
		t1.join()
		time.sleep(6)

		if t2.isAlive():
		 	t2.terminate()


if __name__ == '__main__':
    task = Start()
    task.begin()



