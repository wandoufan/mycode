# Qt中的.qrc文件


## 基本功能
icons.qrc文件是一个资源集合文件，即Qt Resource File  
qrc文件常用于在应用程序中嵌入图片等各种类型的资源  

## 直接添加资源的问题
如果直接在程序里添加一张图片，需要在代码里写出图片的绝对路径或相对路径  
而且在发布exe程序时，还需要把图片放入到相同的目录下，使用过程比较麻烦  
```
label=QLabel()
label.setPixmap(QPixmap("./picture.jpg")) #相对路径
label.show()
```

## qrc添加资源的优点
qrc文件可以将资源编译成二进制文件，并添加到最终生成的可执行程序中  
而且在编译时会将资源进行压缩，生成的可执行文件比直接添加资源要小  

## 文件内容
icons.qrc无法在QT里直接打开，可以用txt文本打开  
根节点为RCC，里面可以包含若干qresource节点  
每个qresource有自己的prefix（路径前缀）属性  
qresource节点包含了若干file节点，描述了各个文件相对于.qrc的路径  
内容是XML文档，如下示例：  
```
<RCC>
    <qresource prefix="/" >
        <file>button.png</file>
    </qresource>
</RCC>
```