# XML语法

## 基本信息
1. XML文档都是一种树结构，从根部开始扩展到枝叶
2. XML必须包含根元素，它是其他所有元素的父元素


## 元素命名规则
1. 名称可以包括数字、字母和标点符号
2. 名字不能以数字或标点符号开始
3. 名称不能以xml、XML、xML等等开始
4. 名称不能包含空格
5. 名称中最好不要带有'-'、'.'、':'等符号，可能会造成误解


## 语法规则
1. XML文件可以选择进行声明，如果声明就要放在文档的第一行
```
<?xml version="1.0" encoding="utf-8"?>
```
2. 所有的标签都必须有对应的关闭标签，即标签两两一组，一组标签的名称必须完全相同
一组标签称为打开标签和关闭标签，或开始标签或结束标签  
```
<p1>content</p1>
```
3. 多个元素可以使用相同的名字
```
<root>
	<child>this is child1</child>
	<child>this is child2</child>
</root>
```
4. XML是大小写敏感的，一组标签的大小写也必须完全相同
```
<message>这是正确的一组标签</message>
<message>这是错误的一组标签</Message>
```
5. HTML会把多个连续的空格符合并成一个，而XML会保留所有的空格符
```
<p1>这是很多      空格符</p1>
```
6. XML中注释的格式和HTML中类似
```
<!-- this is a comment -->
```


## 实体引用
XML中一些字符具有特殊含义，相当于关键字，不能直接写在XML元素中  
如果要在XML元素中使用这些字符，就必须用实体引用来代替  
XML提供了以下五个预定义的实体引用  
```
特殊字符			实体引用
<				&lt;
>				&gt;
&				&amp;
'				&apos;
"				&quot;
```
备注：在XML中，只有<和&确实是非法的，其他三个直接使用也可以，但建议用实体引用来替代  
错误示例：  
```
<message>if number < 100 then break</message>
```
正确示例：  
```
<message>if number &lt; 100 then break</message>
```


## 元素属性及属性值
XML元素和HTML一样也可以拥有属性，属性提供元素的额外信息  
1. 属性的值必须使用引号括起来，单引号和双引号都可以  
```
<root>
	<child1 name = "abc">content</child1>
	<child2 name = 'bcd'>content</child2>
</root>
```
2. 如果属性值本身包含双引号，可以使用单引号把属性值括起来
```
<child message = ' a"b"c '>content</child>
```
也可以使用实体引用来代替双引号
```
<child message = ' a&quot;b&quot;c '>content</child>
```
3. 可以把属性改成一个子元素，也可以把子元素改成一个属性
关于信息该写成属性还是子元素，没有明确规定，一般写成子元素更方便一点  
以下几个写法包含的信息完全相同：  
写法1：  
```
<person sex="male">
	<name>Tom</name>
	<birthday>1999/10/01</birthday>
</person>
```
写法2：  
```
<person>
	<sex>male</sex>
	<name>Tom</name>
	<birthday>1999/10/01</birthday>
</person>
```
写法3：  
```
<person>
	<sex>male</sex>
	<name>Tom</name>
	<birthday>
		<year>1999</year>
		<month>10</month>
		<day>01</day>
	</birthday>
</person>
```
4. 属性不能包含多个值，也不能包含树结构，以下是错误示例
```
<person sex="male", name="Tom", birthday="1999/10/01">content</person>
```