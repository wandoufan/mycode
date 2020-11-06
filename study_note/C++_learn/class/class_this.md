# this指针


## 基本概念
this是C++中的一个关键字，也是一个const指针，它指向当前对象，通过它可以访问当前对象的所有成员  
this指针是所有成员函数的隐含参数，不用自己写这个参数，也看不见这个参数  
当调用一个对象的成员函数时，编译器先将对象地址赋给this指针，然后调用成员函数  
this指针是一个仅能被类的非静态成员函数所访问的特殊指针，即静态成员方法不能使用this指针  
友元函数没有this指针，因为友元不是类的成员，只有成员函数才有this指针  
备注：this指针就相当于python中类的成员方法的self参数  


## this指针的使用
this指针只能在类的非静态成员函数的内部使用，超出这个范围编译器就搞不清this指向谁了  
```
class Student{
public:
    void setage(int age);
    void setscore(float score);
    void show();
private:
    int age;
    float score;
};

void Student::setage(int age){
    this->age = age;
}
void Student::setscore(float score){
    this->score = score;
}
void Student::show(){
    cout << this->age << endl;
    cout << this->score << endl;
}
```