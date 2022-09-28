# Qt中的.qrc文件

## 基本功能
icons.qrc文件是一个资源集合文件，即Qt Resource File  
qrc文件常用于在应用程序中嵌入图片等各种类型的资源  
详见Qt帮助手册"The Qt Resource System"  


## Qt资源系统
Qt的资源系统是一个不依赖于平台的机制，用来在exe中存储二进制文件  
当程序需要用到icon或图片等资源时，可以使用qrc来避免丢失这些文件  
qrc文件可以将资源编译成二进制文件，并添加到最终生成的可执行程序中  
而且在编译时会将资源进行压缩，生成的可执行文件比直接添加资源要小  


## RCC
即resource compiler，资源文件编译器  
RCC在项目构建过程中编译.qrc资源文件，并将资源文件链接到最终的QT程序中  


## 直接添加资源时的问题
如果直接在程序里添加一张图片，需要在代码里写出图片的绝对路径或相对路径  
而且在发布exe程序时，还需要把图片放入到相同的目录下，使用过程比较麻烦  
如果图片丢失，就可能造成程序执行报错  
```
label=QLabel()
label.setPixmap(QPixmap("./picture.jpg")) #相对路径
label.show()
```


## qrc文件内容
根节点为RCC，里面可以包含若干qresource节点  
每个qresource有自己的prefix（路径前缀）属性  
qresource节点包含了若干file节点，描述了各个文件相对于.qrc的路径  
内容是XML文档，如下示例：  
```
<!DOCTYPE RCC><RCC version="1.0">
<qresource>
	<file>images/copy.png</file>
	<file>images/cut.png</file>
	<file>images/new.png</file>
	<file>images/open.png</file>
	<file>images/paste.png</file>
	<file>images/save.png</file>
</qresource>
</RCC>
```


## qrc文件的打开方式
一般qrc在Qt Creator中打开，可以通过UI界面来直接管理图片资源  
在Qt creator项目中找到.qrc文件，右键 - open with:
1. 资源编辑器(最常用)
2. 普通文本编辑器
3. 二进制编辑器
4. System Editor


## 在Qt程序中添加图片资源的方法
备注：先创建.qrc文件，再在.qrc文件中添加图片，如果已经有.qrc文件，直接在里面添加图片就行

1. 把图片文件放到Qt项目目录中
如果图片比较多，可以单独建一个images目录存放图片  

2. 项目 - 右键 - Add New - Qt - Qt Resource File
填写.qrc文件的名字和保存路径(一般放在Qt项目目录中)  
注意：这里添加的是.qrc文件，不是图片文件

3. 在项目中找到刚才创建的.qrc文件
右键 - open with - 资源编辑器  

4. 在资源编辑器界面中，点击'Add Prefix'
写入一个前缀名，如'/MyImage'，也可以使用默认前缀名  
语言栏不用填，然后保存  

5. 在资源编辑器界面中，点击'Add Files'
通过文件目录查找添加图片，然后保存  

6. 添加完成的图片会显示在前缀名下面
正常情况下，图片双击后是可以打开并显示在Qt Creator界面里  
如果打开报错，则说明添加的图片资源有问题  

7. 如果后面需要继续添加图片，选择左侧的'/MyImage'，右键'添加现有文件...'


## 注意事项
在向.qrc文件中添加图片等资源之后，一定要先对项目执行qmake和重新构建
否则虽然图片本身可以在Qt中正常打开显示，但是在代码中读取到的图片就是一个空白的QImage


## 在代码中使用图片资源
读取.qrc中的某个图片，然后转换为QImage  
```
QImage image_logo(":/MyImage/image/avic.jpeg");
```
'/MyImage'为前缀名  
'/image'为图片文件所在的目录名  
'/avic.jpeg'为图片名字  
备注：为了获取正确的路径，最好选择图片文件，右键 - copy path  


## 关于图片格式的说明
Qt资源中最常见的是png格式，但好像其他格式图片如jpeg也能支持  
实际测试中发现，微信截图的png格式图片可以添加到.qrc中，但打开报错：  
```
image format not supported
```
这个报错的原因没有找到  

