# XML

## 基本概念
可扩展标记语言(XML)是一种用于标记电子文件使其具有结构性的标记语言  
XML没有预定义的标签，标签需要进行自己定义  


## 示例
```
<?xml version="1.0" encoding="utf-8"?>
<!--this is a XML test -->

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


## XML和HTML的对比
二者都是一种标记语言，但XML不是HTML的替代品，二者除了名字接近之外没有太多关系  
1. XML被设计用来传输和存储数据，重点是数据的内容  
HTML被设计用来显示数据，重点是数据的外观  
2. HTML的标签都是预定义好的，而XML的标签都是自定义的
3. HTML中有的标签不必有对应的关闭标签，XML中所有的标签都必须有关闭标签


## 用途
1. 做配置文件
2. 做数据交换
类似于json或二进制文件，但xml可以直接打开查看，可读性更强  


## xml文件打开方式
可以直接用记事本等文本工具打开，也可以用浏览器去打开  


## 文件后缀
xml文件不一定是.xml格式，也可以是其他任意格式，只要内容符合xml语法即可  


------------------------------------------------

## 应用例子
boards.xml
Qt中的.qrc文件，.ui文件
.cfg文件


## XML验证器DTD


## 通过代码去读写XML
1. 直接用C++中去读写XML
用第三方的库tinyXml.h
2. 在Qt框架下去读写XML
QXmlStreamWriter、QXmlStreamReader、QXmlDefaultHandler

QXmlSimpleReader、QXmlInputSource、QXmlAttributes、

QXmlStreamAttributes

QXmlContentHandler
