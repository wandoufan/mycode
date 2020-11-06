#include <iostream>
using namespace std;

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

int main(){
    Student stu1;
    stu1.setage(16);
    stu1.setscore(96.5);
    stu1.show();
    return 0;
}