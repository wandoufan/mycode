# QXmlStreamAttributes

## 基本功能
QXmlStreamAttributes可以解析出xml文件中元素的属性以及属性值  


## 代码示例
```
<person Index="1">
```
```
//如果元素中有属性，则读出属性值
QXmlStreamAttributes attributes = reader.attributes();
if(attributes.hasAttribute("Index"))
{
    ui -> textBrowser -> append(QString("Index=%1").arg(attributes.value("Index").toString()));
}
```

## 构造函数
备注：通常用QXmlStreamReader::attributes()来获取QXmlStreamAttributes对象
1. QXmlStreamAttributes::QXmlStreamAttributes()


## 常用公共函数
1. bool QXmlStreamAttributes::hasAttribute(const QString &qualifiedName) const
判断元素中是否有指定的属性  

2. bool QXmlStreamAttributes::hasAttribute(QLatin1String qualifiedName) const
这是一个重载函数  

3. bool QXmlStreamAttributes::hasAttribute(const QString &namespaceUri, const QString &name) const
这是一个重载函数  

4. QStringRef QXmlStreamAttributes::value(const QString &namespaceUri, const QString &name) const
返回元素中属性的值  

5. QStringRef QXmlStreamAttributes::value(const QString &namespaceUri, QLatin1String name) const
这是一个重载函数  

6. QStringRef QXmlStreamAttributes::value(QLatin1String namespaceUri, QLatin1String name) const
这是一个重载函数  

7. QStringRef QXmlStreamAttributes::value(const QString &qualifiedName) const
这是一个重载函数  

8. QStringRef QXmlStreamAttributes::value(QLatin1String qualifiedName) const
这是一个重载函数  