# QT中的foreach关键字

## 基本用法
foreach实际是<QtGlobal>里定义的一个宏，用来遍历容器中所有的项  
使用foreach比使用迭代器代码会更加简洁  
备注：标准C++中并没有foreach，只是QT中增加了这一关键字，而C#和Java中有foreach  
注意：foreach遍历容器是通过创建一个容器的副本，所以不能修改原容器中元素的值  
foreach和for一样，当只有一句时'{}'可以省略，有多行代码时必须加上'{}'  
基本格式为：  
```
foreach(<loop_var> <items>)
  <commands>
endforeach()
```
例子：  
```
void test1() //使用for循环遍历容器
{
    QStringList list1;
    list1 << "a" << "bb" << "ccc" << "dddd" ;
    QByteArray byte1;
    cout << list1.size() << endl;
    for(int i = 0; i < list1.size(); i++)
    {
        byte1 = list1[i].toLatin1();
        cout << i + 1 << byte1.data() << endl;
    }
}

void test2() //使用foreach遍历容器
{
//使用foreach去遍历一个QStringList时，不必对QString类型的元素转换为QByteArray类型就能直接输出
    QStringList list1;
    list1 << "a" << "bb" << "ccc" << "dddd" ;
    QString str1;
    foreach(str1, list1)
        qDebug() << str1;
}

void test3() //在foreach循环中可以加入continue或break
{
    QStringList list1;
    list1 << "a" << "bb" << "ccc" << "dddd" ;
    QString str1;
    foreach(str1, list1)
    {
        if(str1 == "ccc")
            continue;
        qDebug() << str1;
    }
}
```


## foreach遍历顺序类容器

## foreach遍历关联类容器