# QXmlStreamReader

## 基本功能
QXmlStreamReader提供了快速读取解析XML文档的流式API  
reader就像是一个指针，从头到尾对xml中的元素进行逐个遍历  
父类：无  
子类：无  


## 代码示例
```
//打开hlgx文件读取记录信息和通道信息
QString hlgx_file_path = "hlgx.xml";
QFile hlgx_file(hlgx_file_path);
if(hlgx_file.open(QFile::ReadOnly | QFile::Text))
{
    QXmlStreamReader reader(&hlgx_file);
    while(!reader.atEnd())
    {
        if(reader.isStartElement())//判断当前元素是否为StartElement
        {
        	//跳过<Project> </Project>这一组元素及其子元素
        	if(reader.name() == "Project")
            {
                reader.skipCurrentElement();
            }
            //读出元素中包含的内容
            if(reader.name() == "StartDateTime")
            {
                ui -> textBrowser -> append(QString("StartDateTime=%1").arg(reader.readElementText()));
            }
            if(reader.name() == "StopDateTime")
            {
                ui -> textBrowser -> append(QString("StopDateTime=%1").arg(reader.readElementText()));
            }
            //如果元素中有属性，则读出属性值
            QXmlStreamAttributes attributes = reader.attributes();
            if(attributes.hasAttribute("Index"))
            {
                ui -> textBrowser -> append(QString("Index=%1").arg(attributes.value("Index").toString()));
            }
        }
        reader.readNext();
    }
    hlgx_file.close();
}
else
{
    ui -> textBrowser -> setText("hlgx文件打开失败");
}
```


## 关于元素类型的说明
```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE hlgx>
<!--this is a XML test -->
<person id="1">
	<sex>male</sex>
	<name>Tom</name>
	<birthday>
		<year>1999</year>
		<month>10</month>
		<day>1</day>
	</birthday>
</person>
```
1. StartDocument
```
<?xml version='1.0' encoding='UTF-8'?>
```
2. EndDocument
目前还没见过
3. StartElement
```
<sex>
<name>
```
4. EndElement
```
</sex>
</name>
```
5. Characters
```
male
Tom
```
6. 属性
```
id
```
7. 属性值
```
1
```
8. DTD
```
<!DOCTYPE hlgx>
```


## 构造函数
1. QXmlStreamReader::QXmlStreamReader(const char \*data)

2. QXmlStreamReader::QXmlStreamReader(const QString &data)

3. QXmlStreamReader::QXmlStreamReader(const QByteArray &data)

4. QXmlStreamReader::QXmlStreamReader(QIODevice \*device)
打开一个xml文件，然后把文件句柄传递给QXmlStreamReader的构造函数，获得一个实例化对象  

5. QXmlStreamReader::QXmlStreamReader()


## 常用公共函数：读取xml基本信息
1. QStringRef QXmlStreamReader::documentEncoding() const
当前元素为StartDocument时，返回元素中声明的编码格式，否则返回空字符串  

2. QStringRef QXmlStreamReader::documentVersion() const
当前元素为StartDocument时，返回元素中声明的版本，否则返回空字符串  


## 常用公共函数：判断元素类型
1. QXmlStreamReader::TokenType QXmlStreamReader::tokenType() const
获取当前元素的类型  

2. QString QXmlStreamReader::tokenString() const
以字符串的格式获取当前元素的类型  

3. bool QXmlStreamReader::isCDATA() const

4. bool QXmlStreamReader::isCharacters() const

5. bool QXmlStreamReader::isComment() const

6. bool QXmlStreamReader::isDTD() const

7. bool QXmlStreamReader::isEndDocument() const

8. bool QXmlStreamReader::isEndElement() const

9. bool QXmlStreamReader::isEntityReference() const

10. bool QXmlStreamReader::isProcessingInstruction() const

11. bool QXmlStreamReader::isStandaloneDocument() const

12. bool QXmlStreamReader::isStartDocument() const

13. bool QXmlStreamReader::isStartElement() const

14. bool QXmlStreamReader::isWhitespace() const


## 常用公共函数：读取元素字段
1. QStringRef QXmlStreamReader::name() const
如果当前元素类型为StartElement或EndDocument，返回元素本身的名称  
如果当前元素类型为Characters，返回空字符串  
<名称></名称>  
返回值示例：  
```
sex
name
```

2. QStringRef QXmlStreamReader::text() const
如果当前元素类型为StartElement或EndDocument，返回空字符串 
如果当前元素类型为Characters、Comment、DTD、EntityReference，返回文本内容  
返回值示例：  
```
male
Tom
```

3. QString QXmlStreamReader::readElementText(QXmlStreamReader::ReadElementTextBehaviour behaviour = ErrorOnUnexpectedElement)
如果当前元素类型为StartElement，则会一直往下读取到对应的EndDocument，然后返回二者中间包含的文本内容  
如果当前元素类型不是StartElement，返回空字符串  
注意：调用了readElementText()函数之后，当前读取元素会跳转到对应的EndDocument  
behaviour参数用来指定读取时如果遇到子元素的行为，具体参见enum QXmlStreamReader::ReadElementTextBehaviour  
返回值示例：  
```
male
Tom
```

4. QXmlStreamAttributes QXmlStreamReader::attributes() const
如果当前元素类型为StartElement，返回其属性，之后可以进一步读取到其属性值  


## 常用公共函数：判断/移动reader指针位置
1. bool QXmlStreamReader::atEnd() const
当reader已经读取到xml文档的末尾，或者读取过程中出错导致读取中断，则返回true，否则返回false  

2. qint64 QXmlStreamReader::lineNumber() const
返回当前reader所在的行号，从1开始  

3. qint64 QXmlStreamReader::columnNumber() const
返回当前reader所在的列号，从0开始  
备注：这里不是一个元素算一列，而是一个字符就算一列  

4. QXmlStreamReader::TokenType QXmlStreamReader::readNext()
读取下一个元素，并返回其元素类型

5. bool QXmlStreamReader::readNextStartElement()
读取下一个StartElement类型的元素  
当读取到了下一个StartElement类型的元素时，返回true  
当读取到了xml文档末尾，或读取过程中发送错误，返回false  

6. void QXmlStreamReader::skipCurrentElement()
往下一直读到当前元素的末尾，跳过遇到的所有子元素  
如果当前元素类型为StartElement，则会跳转到对应的EndDocument元素  
如果当前元素类型为EndDocument，则会一直跳转到xml文档末尾  


## 常用公共函数：报错信息
1. bool QXmlStreamReader::hasError() const

2. QXmlStreamReader::Error QXmlStreamReader::error() const
返回当前错误类型，没有报错时返回QXmlStreamReader::NoError  

3. void QXmlStreamReader::raiseError(const QString &message = QString())
设置自定义报错信息  

4. QString QXmlStreamReader::errorString() const
返回raiseError()中设置的报错信息  


## enum QXmlStreamReader::ReadElementTextBehaviour
这个集合定义了执行readElementText()函数时如果读到子元素的具体行为  
```
Constant 										Value 		Description
QXmlStreamReader::ErrorOnUnexpectedElement		0 			当读取到子元素时报错
QXmlStreamReader::IncludeChildElements			1 			递归的把子元素中包含的文本内容也返回回来
QXmlStreamReader::SkipChildElements				2 			跳过子元素
```


## enum QXmlStreamReader::TokenType
这个集合中包含所有的xml元素类型  
```
Constant								Value	Description
QXmlStreamReader::NoToken				0 		reader还没有读到任何元素
QXmlStreamReader::Invalid				1 		读取时发生了错误
QXmlStreamReader::StartDocument			2 		开始文档
QXmlStreamReader::EndDocument			3 		结束文档
QXmlStreamReader::StartElement			4 		开始元素
QXmlStreamReader::EndElement			5 		结束元素
QXmlStreamReader::Characters			6 		元素内容
QXmlStreamReader::Comment				7 		
QXmlStreamReader::DTD 					8 		
QXmlStreamReader::EntityReference 		9 		
QXmlStreamReader::ProcessingInstruction 10 		
```


