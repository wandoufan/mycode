# mysql的数据类型

## 数字类型
包括整型和浮点型,最常用的包括：int,float,double

## 字符串类型
1. 普通的文本字符串类型(固定长度0 - 255的char型和变长的varchar型)
注意：在定义char和varchar时都要声明长度，否则默认长度只有1  
char和varchar的最大长度为8000  
如果需要快速的性能，选择char型  
如果需要节省空间，选择varchar型  
2. 可选类型(存储长文本的text型和存储声音图像等二进制数据的blob型)
如果搜索的内容不区分大小写，可以使用text型  
如果搜索的内容区分大小写，可以blob型  
3. 特殊类型(set型和enum型)
enum('value1','value2',.....)只允许选择一个值或者为Null，如性别字段  
set('value1','value2',.....)允许选多个值或者为Null，如兴趣字段  

## 时间日期类型
date 格式为2018-07-09  
time 格式为08:10:30  
datetime 格式为2018-07-09 08:10:30  
year 格式为2018或18  
timestamp 时间标签  
注意：time字段间可以直接比较大小，也可以通过相减得到两个日期的差值，类似datediff函数
```
select a.id, a.date - b.date from time_info a, time_info b where a.id > b.id and a.date < b.date;
```