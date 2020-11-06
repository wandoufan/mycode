
## 类的定义
```
class CMeter
{
public:
	double m_nPercent; //声明一个公有成员变量
	void StepIt(); //声明一个公有成员方法
	void SetPos(int nPos); //声明一个公有成员方法
	int GetPos() //声明并定义一个公有成员方法
	{
		return m_nPos;
	}
private:
	int m_nPos; //声明一个私有成员变量
};

void CMeter::StepIt() //在类的外部定义类的成员方法
{
	m_nPos++;
}
void CMeter::SetPos(int nPos) //在类的外部定义类的成员方法
{
	m_nPos = nPos;
}
```


## 对象的定义和初始化
1. 对象定义有三种方式：声明之后定义、声明之时定义、一次性定义  
为实现类的封闭性，尽量在声明之后定义  
```
void class_init()
{
	CMeter myMeter, * Meter, Meters[2]; //对象可以是普通对象、指针对象、数组对象
	myMeter.m_nPercent = 3.14; //普通对象访问成员变量
	myMeter.SetPos(2); //普通对象访问成员方法
	Meters[0].m_nPercent = 1.98; //数组对象访问成员变量
	Meter = &Meters[1]; //将指针指向数组的第二个元素
	Meter -> m_nPercent = 0.98; //通过指针访问成员时只能使用'->'
	cout << Meter -> m_nPercent << endl;
}
```