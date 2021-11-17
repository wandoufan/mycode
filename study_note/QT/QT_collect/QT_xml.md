# Qt中操作XML

## 基本情况
Qt提供了两个API集合来读写XML文档：
1. 基于流(stream)
也就是把XML文档当做数据流来进行处理  
流处理和SAX方法并不相同(具体不同之处没看太懂)  
2. 基于DOM
DOM是W3C官方的标准，定义了用于获取、更改、添加、删除XML元素的标准方法  


## 注意事项
1. 并不是所有xml相关的类都在QtXml模块中，有的也在QtCore模块中


## QtXml模块
QtXml模块包含了很多个处理XML相关的类(主要是基于DOM的)  
要想在项目中使用xml模块，需要先在.pro文件中声明'QT += xml'  
也可以使用'#include <QtXml>'将所有的类都包含进行，但会造成冗余  


## 基于流(stream)来处理XML的类
备注：以下类都来自于QtCore模块，而不是QtXml模块  
1. QXmlStreamReader(常用)
2. QXmlStreamWriter(常用)
3. QXmlStreamAttribute
4. QXmlStreamAttributes
5. QXmlStreamEntityDeclaration
6. QXmlStreamEntityResolver
7. QXmlStreamNamespaceDeclaration
8. QXmlStreamNotationDeclaration


## 基于DOM来处理XML的类
备注：以下类都来自于QtXml模块  
1. QDomAttr
2. QDomCDATASection
3. QDomCharacterData
4. QDomComment
5. QDomDocument
6. QDomDocumentFragment
7. QDomDocumentType
8. QDomElement
9. QDomEntity
10. QDomEntityReference
11. QDomImplementation
12. QDomNamedNodeMap
13. QDomNode
14. QDomNodeList
15. QDomNotation
16. QDomProcessingInstruction
17. QDomText


## 一些过时的XML相关的类
备注：以下类都来自于QtXml模块，而不是QtCore模块  
备注：这些类可能在Qt 5.2.1版本的代码中用过，但在Qt 5.15版本中已经过时  
1. QXmlDefaultHandler(过时)
2. QXmlSimpleReader(过时)
3. QXmlInputSource(过时)
4. QXmlAttributes(过时)
5. QXmlContentHandler(过时)
