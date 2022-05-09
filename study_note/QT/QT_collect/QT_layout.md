# Qt中的界面布局

## 基本信息
使用layout相关的类需要在.pro文件中添加：  
```
QT += widgets
```
备注：Qt中没有layout模块，只是一些相关的类  


## Layout相关类的继承关系
1. Vertical Layout：垂直方向布局，组件自动在垂直方向上分布  
2. Horizontal Layout：水平方向布局，组件自动在水平方向上分布  
3. Grid Layout：网格状布局，网状布局大小改变时，每个网格的大小都改变  
4. Form Layout：窗体布局，与网格状布局类似，但是只有最右侧的一列网格会改变大小  
```
QLayout
	├─QBoxLayout
	│  ├─QHBoxLayout 将所有Widget组件水平排列
	│  └─QVBoxLayout 将所有Widget组件垂直排列
	├─QFormLayout 管理Input Widget组件和与它们关联的labels
	├─QGridLayout 将所有Widget组件以网格状排列
	└─QStackedLayout 一次显示一个组件(组件堆叠在一起，只显示最上面组件)
```
其中，QGridLayout是最常用的，优先使用这个  


