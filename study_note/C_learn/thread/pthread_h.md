## pthread.h库

## 基本功能
在C语言和C++中实现多线程相关的功能  
备注：C++在11之后的版本中有了新的线程库`# include <thread.h>`  
备注：在linux环境下的多线程可能与Windows环境下的不同，以下都以windows环境为准  


-----------------------库中提供的函数-------------------------------

## 1. 创建线程的函数
1. 基本功能
根据给定的线程运行函数，创建一个新的线程，并在线程中执行线程运行函数  
当创建一个线程时，可以通过属性来定义线程是可连接的(joinable)还是可分离的(detached)  
只有可连接的线程才可以被连接，如果是可分离的线程，则永远不能被连接  

2. 函数参数
```
int pthread_create(pthread_t *tidp, const pthread_attr_t *attr, 
	(void*)(*start_rtn)(void*), void *arg);
```
第一个参数是指向线程标识符的指针  
第二个参数是用来设置线程属性  
第三个参数是线程运行函数的起始地址  
第四个参数是运行函数的参数  
线程创建成功，则返回0；线程创建失败，则返回非0值  

3. 示例
```
int result = pthread_create(&id_array[i], NULL, say_hello, (void *)(&i));
```



## 2. 退出线程的函数
1. 基本功能
用来显式的退出一个线程，当线程完成工作无需继续存在时，就可以使用该函数  
如果主线程(main函数)在子线程之前就结束，而且是通过pthread_exit()退出的，则子线程将继续执行  
否则，不管子线程是否执行完成，子线程都会随着主线程退出而提前结束  

2. 函数参数
```
void pthread_exit(void *retval);
```
第一个参数是线程结束时的退出状态

3. 示例
```
pthread_exit(NULL);
```


## 3. 指定线程执行顺序的函数
1. 基本功能
使用pthread_create创建新线程之后，新线程和旧线程的执行顺序用户是不知道的，由操作系统的调度机制决定  
如果想要使一个线程等待另一个线程结束之后再执行，就需要使用pthread_join函数  
例如，在A线程中调用pthread_join来操作B线程，则pthread_join会把A线程阻塞，直到B线程退出  
当B线程退出之后，A线程会收到B线程的返回状态，并继续往下执行A线程  


2. 函数参数
```
int pthread_join(pthread_t thread, void **retval);
```
第一个参数是线程的标识符，即线程唯一ID  
第二个参数是一个状态类型指针的指针，指向线程结束时的退出状态指针

3. 示例
```
```


## 4. 实现线程分离的函数
1. 基本功能
用来实现主线程和子线程的分离，子线程结束后，自动回收子线程的资源
备注：一般用来替代pthread_join函数

2. 函数参数
```
pthread_detach
```

3. 示例
```
```

-----------------------库中提供的类型-------------------------------

## 一些对象
1. pthread_t
线程标识符，即线程的唯一ID  
```
pthread_t thread_id;//创建一个线程标识符对象
pthread_t id_array[5];//创建一个数组，数组中的元素都是线程标识符对象
pthread_t *thread_id;//创建一个线程标识符类型的指针
```
2. pthread_attr_t

3. pthread_attr_init

4. pthread_attr_setdetachstate



-----------------------代码示例-----------------------------

1. 最简单的例子，起5个线程，线程运行函数不带任何参数
```
#define THREAD_NUM 5

void *say_hello(void *args)
{
	cout << "hello！" << endl;
	return 0;
}

int main()
{
	pthread_t id_array[THREAD_NUM];
	for(int i = 0; i < THREAD_NUM; i++)
	{
		//创建线程，线程函数参数为NULL
		int result = pthread_create(&id_array[i], NULL, say_hello, NULL);
		cout <<"第" << i << "个线程的返回值：" << result << endl;
		// Sleep(300);
	}
	pthread_exit(NULL);
	return 0;
}
```
2. 起5个线程，线程运行函数接收1个整型参数
```
#define THREAD_NUM 5

void *say_hello(void *index)
{
	//对于传入的参数要进行类型转换，先由无类型指针转换为整型指针，然后再读出指针所指向的变量值
	int i = *((int *)index);
	cout << "线程序号为：" << i << endl;
	return 0;
}

int main()
{
	pthread_t id_array[THREAD_NUM];
	for(int i = 0; i < THREAD_NUM; i++)
	{
		//创建线程，传入线程函数的参数时，必须先转换为(void *)类型，即无类型指针
		int result = pthread_create(&id_array[i], NULL, say_hello, (void *)(&i));
		cout <<"第" << i + 1 << "次执行返回值：" << result << endl;
		// Sleep(300);
	}
	pthread_exit(NULL);
	return 0;
}
```
3. 起5个线程，把多个参数打包成一个结构体，线程运行函数接收1个结构体参数
```
#define THREAD_NUM 5

struct thread_data
{
	int thread_id;
	float number;
	char* message;
};

void *say_hello(void *data)
{
	//对于传入的参数要进行类型转换，先由无类型指针转换为thread_data结构体指针，然后再读出指针所指向的变量值
	struct thread_data mydata;
	mydata = *((struct thread_data *)data);
	cout << "thread_id：" << mydata.thread_id << endl;
	cout << "number：" << mydata.number << endl;
	cout << "message : " << mydata.message << endl;
	return 0;
}

int main()
{
	pthread_t id_array[THREAD_NUM];
	struct thread_data data_array[THREAD_NUM];
	for(int i = 0; i < THREAD_NUM; i++)
	{
		//初始化结构体数组
		data_array[i].thread_id = i;
		data_array[i].number = i + 0.5;
		data_array[i].message = (char*)"this is a message";
		//创建线程，传入线程函数的参数时，必须先转换为(void *)类型，即无类型指针
		int result = pthread_create(&id_array[i], NULL, say_hello, (void *)(&data_array[i]));
		cout <<"第" << i + 1 << "次执行返回值：" << result << endl;
		// Sleep(300);
	}
	pthread_exit(NULL);
	return 0;
}
```
4. 


--------------------待学习-------------------------
C语言通过pthread.h库实现多线程和其他地方的多线程都差不多，都要用到互斥锁等方法
时间关系，不再往下看了，如果后面要用到，具体实现过程参考：
```
https://zhuanlan.zhihu.com/p/97418361
https://www.runoob.com/cplusplus/cpp-multithreading.html
```

