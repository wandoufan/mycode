# 基于C++的Qt项目的注释规范

## 基本说明
1. 注释中的标识符可以被代码解析工具Doxygen识别，并将注释内容生成到Html文件里
2. 每个标识符都有两种写法，功能相同
```
\brief
@brief
```

## 示例
1. 函数的注释
```
class Student
{
    Q_OBJECT
public:
    /*!
    \brief
        注释内容

    \param name
        注释内容

    \return
        注释内容
    */
    int GetId(name);
    ...
}
```
2. 类的注释
```
namespace space1{
/*!
\brief
    注释内容
*/
class Student
{
	...
}
}
```
3. 模板类的注释
```
namespace space1{
/*!
\brief
    注释内容

\tparam T
    注释内容
*/
template <typename T>
class TestFactoryClass : public FactoryClass
{
	...
}
}
```


## brief
介绍函数或类的功能作用  
```
/*!
\brief
    注释内容
*/
```


## param
介绍函数参数  
```
/*!
\param 函数参数1
    注释内容
\param 函数参数2
    注释内容
*/
```


## return
介绍函数返回值  
```
/*!
\return
    注释内容
*/
```


## tparam
介绍模板参数  
```
/*!
\tparam 模板类型
    注释内容
*/
```


## version
介绍版本  
```
/*!
\version 1.0
*/
```


## author
介绍作者  
```
/*!
\author zhang
*/
```


## date
介绍日期时间  
```
/*!
\date 2021-10-08 10:30
*/
```


## property
介绍属性  


## exception
介绍可能抛出的异常  

