# Qt的界面编码

## 完全用纯代码方式实现UI界面
1. 通过UI方式实现窗口的设计更加简单，让用户省去了繁琐的界面设计工作  
采用代码设计实现 UI 时，需要对组件的布局有个完整的规划，不如可视化设计直观，且编写代码工作量大  
但用纯代码方式可以在底层实现更加强大和灵活的设计功能  

2. 要采用纯代码方式，在创建项目时要将'Generate form'取消勾选，创建完成后项目目录下没有.ui文件  

3. 用UI方式和纯代码方式实现同一个功能，二者的底层代码并不相同  
UI方式的底层代码是自动生成的(也可以有自定义的部分)，并不包含组件定义  
代码方式需要在头文件中将所有用到的组件都定义出来  

4. 代码方式实现时，在头文件的类定义中没有指向界面的指针ui  
在cpp主文件中也不再去调用指针ui  

5. 对于用纯代码插入的组件，在UI界面的编辑器里是不可见的，只有程序运行之后才能看见  
因此，不能通过UI编辑器来拖动这些组件的位置，只能用代码参数设置  


## 用.ui文件 + 代码的方式实现UI界面
备注：这种方法是在项目代码中看到的，还没有实际用过
1. 情况说明
有一个mywidget.ui，负责添加和布局UI界面的各种控件  
另外还有一组MyWidget.h/cpp，里面使用的命名控件为MyNameSpace，定义了一个QWidget的子类MyWidget  
代码负责对.ui中各种控件设置字体等属性、设置默认值、添加下拉菜单选项、添加信号与槽关系等等  

2. 在代码中调用.ui文件中的控件
和正常的用法一样，直接通过指针ui来调用各种控件  

3. 在.ui文件中调用代码中定义的控件(重点)
在界面中添加一个QWidet作为整个界面最底层的大控件，命名为MyNameSpace::MyWidget  
然后其他控件都放在这个大控件上面  


## 代码示例：用代码来批量创建控件
1. 情况说明
有时候需要在UI界面上创建几十个甚至更多的控件，如QLabel、QPushButton等
如果在Qt designer上逐个手动创建，实现起来会很麻烦，可以使用代码来进行批量创建
在代码中，如果每个控件的对象名都手写出来也会很麻烦，可以把控件对象指针批量添加到QVector或QList等容器类中
备注：在代码中并没有具体定义出每个控件的对象名称
注意：容器类的数据项不支持QObject类及其子类(包括所有的Qt控件类)，因此添加到容器类的是对象指针，而不是对象

2. 具体代码
在界面中创建80个QCheckBox，来让用户勾选通道
```
QVector<QCheckBox *> input_channels_list;
for(int i = 0; i < 80; i++)
{
    QString checkbox_name = QString("channel_%1").arg(i);
    input_channels_list.append(new QCheckBox(checkbox_name));
}
QGridLayout *gridlayout = new QGridLayout;
int row = 0;
int column = 0;
for(int i = 0; i < 80; i++)
{
    //布局：每行10个通道，共8行
    qDebug() << i << ": " <<  row << ", " << column;
    gridlayout -> addWidget(input_channels_list[i], row, column);
    if(column < 9)
        column += 1;
    else
        column = 0;
    if(column == 0)
        row += 1;
}
ui -> groupBox_input_channels -> setLayout(gridlayout);
```
