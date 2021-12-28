# 类中的友元friend

## 基本概念
一般情况下，类中的protected和private类型成员只能由内部函数访问，外部无法访问  
友元机制允许在类的外部，对类中的rotected和private成员变量进行读写操作  
如果将一个类或一个函数声明为类A的友元，则它们可以访问类A中的成员变量  


## 关于友元机制的说明
如果把类的封装比喻成一堵墙，那么友元机制就像是在墙上开了一扇门  
友元类和友元函数可以通过这扇门来访问墙内的protected和private类型成员  
也就是说，友元机制会一定程度破坏类的封装性，因此使用时一定要慎重  


## 友元机制的特点
1. 友元关系不能被继承
A类与B类具有友元关系，A类的子类C类与B类不一定具有友元关系  
2. 友元关系是单向的，不具有交换性
A类是B类的友元，B类不一定是A类的友元  
3. 友元关系不具有传递性
A类是B类的友元，B类是C类的友元，A类不一定是C类的友元  


## 全局函数作为友元函数
1. 基本概念
在类A外部进行声明和定义的全局函数，可以通过friend声明成为类A的友元函数  
注意：类A的友元函数func虽然出现在类A的定义中，但func不是类A的成员函数  
2. 友元函数的参数
友元函数的形参中必须包含该类的对象形参，友元函数就是通过对象形参来访问类的成员变量  
友元函数中的对象形参可以是对象本身，也可以是对象指针  
友元函数的参数中可以只有对象形参，也可以包含其他参数  
3. 声明格式
```
class A
{
...
public:
    //声明func是A的友元函数，注意func不是A的成员函数
    friend void func1(A *a)//对象指针作为形参
    friend void func2(A a)//对象本身作为形参
...
}

//func函数的声明和定义，注意不用加上friend
void func1(A *a)
{...}

void func2(A a)
{...}
```
4. 代码示例
```
class Student
{
public:
    Student(char *name, int age, float score);
public:
    friend void show(Student *pstu);  //将show()声明为友元函数
private:
    char *m_name;
    int m_age;
    float m_score;
};

Student::Student(char *name, int age, float score): m_name(name), m_age(age), m_score(score){ }

//全局函数的声明和定义，注意不用加上friend
void show(Student *pstu)
{
    cout << "name:" << stu -> m_name << endl;
    cout << "age:" << stu -> m_age << endl;
    cout << "score:" << stu -> m_score << endl;
}

int main(){
    char name1[10] = "小明";
    Student stu(name1, 15, 90.6);
    show(&stu);  //调用友元函数
    char name2[10] = "小白";
    Student *pstu = new Student(name2, 16, 80.5);
    show(pstu);  //调用友元函数
    return 0;
}
```


## 类的成员方法作为友元函数
1. 基本概念
在类A外部进行声明和定义的其他类中的成员方法，可以通过friend声明成为类A的友元函数  
注意：类A的友元函数func虽然出现在类A的定义中，但func不是类A的成员函数  
2. 友元函数的参数
友元函数的形参中必须包含该类的对象形参，友元函数就是通过对象形参来访问类的成员变量  
友元函数中的对象形参可以是对象本身，也可以是对象指针  
友元函数的参数中可以只有对象形参，也可以包含其他参数  
3. 注意事项
由于类A和类B存在相互引用，所以必须按照下面的方法写，友元函数的声明和定义必须分开  
4. 代码示例
```
class A;//由于在B的成员方法中引用了A，所以必须先对A声明

class B
{
public:
    void print_number(A a);//友元函数的声明，注意不用加上friend
};

class A
{
public:
    A(int number = 0)
    {
        m_number = number;
    }
    //将类B中的print_number方法声明为类A的友元函数
    friend void B::print_number(A a);
private:
    int m_number;
};

void B::print_number(A a)//友元函数的定义
{
    cout << a.m_number << endl;
}

int main()
{
    A a(10);
    B b;
    b.print_number(a);
    return 0;
}
```


## 友元类
1. 基本概念
将类B声明为类A的友元类，则类B中所有的成员函数都可以访问类A中的成员变量  
必须把类A的对象或对象指针作为类B的成员变量，这样类B才能访问到类A中的成员变量  
2. 代码示例：
```
class A
{
public:
    A(int number1 = 1, int number2 = 2)
    {
        m_number1 = number1;
        m_number2 = number2;
    }

public:
    friend class B;//声明类B为友元类

private:
    int m_number1;
    int m_number2;
};

class B //类B的声明和定义
{
public:
    A m_a; //类B中必须包含类A的对象或对象指针
public:
    void print_number1()
    {
        cout << m_a.m_number1 << endl;
    }
    void print_number2()
    {
        cout << m_a.m_number2 << endl;
    }
};

int main()
{
    A a(3,4);
    B b;
    b.m_a = a;
    b.print_number1();
    b.print_number2();

    return 0;
}
```


## 嵌套友元类
友元类B也可以直接定义在类A内部，与类A形成嵌套+友元的关系  
这种类很难写，经常会看不懂，但项目代码中经常出现这种写法，可以作为参考  
备注：要严格按照代码示例的写法，很多地方稍做改动就会出现错误  
1. 示例1
类B的对象指针作为类A的public成员变量，类A的对象指针作为类B的private成员变量  
需要在对类B实例化的时候，就对类B中的类A对象指针进行赋值  
```
class A
{
public:
    A(int number1 = 1, int number2 = 2)
    {
        m_number1 = number1;
        m_number2 = number2;
    }
    class B //类B的声明和定义
    {
    public:
        B(A *a)
        {
            p_a = a;
        }
        void print_number1()
        {
            cout << p_a -> m_number1 << endl;
        }
        void print_number2()
        {
            cout << p_a -> m_number2 << endl;
        }
    private:
        A *p_a;
    };

public:
    B *b;
    friend class B;//将类B声明为友元类

private:
    int m_number1;
    int m_number2;
};

int main()
{
    //b是a1的成员变量，a1也是b的成员变量，二者相互嵌套
    A a1(3, 4);
    a1.b = new A::B(&a1);
    a1.b -> print_number1();//3
    a1.b -> print_number2();//4

    //b是a1的成员变量，另一个A对象指针p是b的成员变量
    A *p = new A(5, 6);
    a1.b = new A::B(p);
    a1.b -> print_number1();//5
    a1.b -> print_number2();//6

    return 0;
}
```
2. 示例2
类B的对象指针作为类A的public成员变量，类A的对象指针作为类B的public成员变量
可以在对类B实例化之后，再对类B中的类A对象指针单独赋值  
```
class A
{
public:
    A(int number1 = 1, int number2 = 2)
    {
        m_number1 = number1;
        m_number2 = number2;
    }
    class B //类B的声明和定义
    {
    public:
        void print_number1()
        {
            cout << p_a -> m_number1 << endl;
        }
        void print_number2()
        {
            cout << p_a -> m_number2 << endl;
        }
    public:
        A *p_a;
    };

public:
    B *b;
    friend class B;//将类B声明为友元类

private:
    int m_number1;
    int m_number2;
};

int main()
{
    //b是a1的成员变量，a1也是b的成员变量，二者相互嵌套
    A a1(3, 4);
    a1.b = new A::B;
    a1.b -> p_a = &a1;
    a1.b -> print_number1();
    a1.b -> print_number2();
    
    return 0;
}
```
3. 示例3：
类B的对象(不是对象指针)作为类A的public成员变量，类A的对象指针作为类B的private成员变量  
在A构造函数中，可以用this把当前A对象指针直接传递给B对象，不必再专门对A中的B对象赋值  
```
class A
{
public:
    A(int number1 = 1, int number2 = 2):
    m_number1(number1), 
    m_number2(number2), 
    b(this)//用this把当前A对象指针直接传递给B对象
    {}

    class B //类B的声明和定义
    {
    public:
        B(A *a):p_a(a)//B的构造函数接收一个A对象指针
        {}
    public:
        void print_number1()
        {
            cout << p_a -> m_number1 << endl;
        }
        void print_number2()
        {
            cout << p_a -> m_number2 << endl;
        }
    public:
        A *p_a;
    };

public:
    B b;//b是一个对象，不是对象指针
    friend class B;//将类B声明为友元类

private:
    int m_number1;
    int m_number2;
};

int main()
{
    //b是a1的成员变量，a1也是b的成员变量，二者相互嵌套
    A a1(3, 4);
    a1.b.print_number1();//3
    a1.b.print_number2();//4
    
    return 0;
}
```