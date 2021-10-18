1. Sleep()
程序会被挂起一段时间
2. wait()
一般用在多进程中，等待别人
3. delay()
好像是在单片机中去使用
delay()是循环等待，该进程还在运行，占用处理器。
sleep()不同，它会被挂起，把处理器让给其他的进程。

4. while或for循环
需要知道计算机机器指令的周期，计时不准确，耗费计算机资源，可能造成卡死


## 用Sleep在脚本中进行延时操作
注意：使用Sleep()函数会导致程序被挂起，不可响应，对整个程序的性能会有很大影响，只适合1秒钟以内的延时
当一个脚本在Sleep()时，其他循环脚本还可以正常执行
但对于用户点击按钮的操作，程序会无反应，只能等待运行结束之后(不是脚本中Sleep的部分，而是整个脚本)，才会执行刚才用户点击按钮对应的动作
实际测试，不管是一次性Sleep(1000)，还是循环100次，每次Sleep(10)，都会造成点击按钮无反应
```
	#pragma code("kernel32.dll") 
	void Sleep(int Milliseconds);
	#pragma code();

	SetTagDWord("power_start", 1);
	Sleep(3000);//时间单位为毫秒
	SetTagDWord("power_start", 0);
```
可以将Sleep写成循环，然后在循环中加入某种情况判断，如果符合某种情况就提前break
备注：emergency_stop_flag标志位只能由其他脚本置为1，或者直接通过输入输出域置为1，无法使用按钮来把标志位置为1，点击按钮会没有反应
```
	#pragma code("kernel32.dll") 
	void Sleep(int Milliseconds);
	#pragma code();
	int i;

	SetTagDWord("power_start", 1);
	while(i < 100)
	{
		if(GetTagBit("emergency_stop_flag") == 1)
		{
			printf("收到急停信号！\n");
			break;
		}
		printf("i : %d\n", i);
		i ++;
		Sleep(100);
	}
	SetTagDWord("power_start", 0);
```