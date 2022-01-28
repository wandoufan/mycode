# enum

## 基本说明
Qt中包含很多enum，有的属于某个类，以类名开头，如`enum QChart::ChartTheme`
有的属于整个Qt，相当于公共enum，以Qt开头，如`enum Qt::AlignmentFlag`
备注：使用这些enum，需要在.pro文件中添加
```
QT += core
```


## enum Qt::AlignmentFlag
这个参数用来设置组件的对齐方式，如左对齐  
```
Constant				Value		Description
//水平参数
Qt::AlignLeft			0x0001		水平方向靠左
Qt::AlignRight			0x0002		水平方向靠右
Qt::AlignHCenter		0x0004		水平方向居中
Qt::AlignJustify		0x0008		水平方向调整间距两端对齐
//垂直参数
Qt::AlignTop			0x0020		垂直方向靠上
Qt::AlignBottom			0x0040		垂直方向靠下
Qt::AlignVCenter		0x0080		垂直方向居中
Qt::AlignBaseline		0x0100		垂直方向靠基准线
//双维度参数
Qt::AlignCenter			AlignVCenter | AlignHCenter
等价于Qt::AlignHCenter | Qt::AlignVCenter
```
注意：水平参数和垂直参数可以同时设置，中间用|隔开，如`Qt::AlignLeft | Qt::AlignVCenter`  


## enum Qt::GlobalColor
颜色也可以用下面的参数进行赋值  
使用方式：QColor(Qt::lightGray)  
```
Constant 			Value 		Description
Qt::white 			3 			White (#ffffff)
Qt::black 			2 			Black (#000000)
Qt::red 			7 			Red (#ff0000)
Qt::darkRed 		13 			Dark red (#800000)
Qt::green 			8 			Green (#00ff00) 
Qt::darkGreen 		14 			Dark green (#008000) 
Qt::blue 			9 			Blue (#0000ff) 
Qt::darkBlue 		15 			Dark blue (#000080) 
Qt::cyan 			10 			Cyan (#00ffff) 
Qt::darkCyan 		16 			Dark cyan (#008080) 
Qt::magenta 		11 			Magenta (#ff00ff) 
Qt::darkMagenta 	17 			Dark magenta (#800080) 
Qt::yellow 			12 			Yellow (#ffff00) 
Qt::darkYellow 		18 			Dark yellow (#808000) 
Qt::gray 			5 			Gray (#a0a0a4) 
Qt::darkGray 		4 			Dark gray (#808080) 
Qt::lightGray 		6 			Light gray (#c0c0c0) 
```


## enum Qt::WindowModality
这个集合描述了窗口的模态特性  
```
Constant 				Value 	Description
Qt::NonModal 			0 		这个窗口是非模态的，不会封锁其他窗口获得输入
Qt::WindowModal 		1 		这个窗口是模态的，只会封锁其父类窗口、父类的父类窗口等获得输入
Qt::ApplicationModal 	2 		这个窗口是模态的，会封锁其他所有窗口获得输入
```


## enum Qt::ItemDataRole
常用role的取值：  
```
Constant   Value   Description  
//通用角色及相关类型
Qt::DisplayRole   0   用文本形式展示的关键数据(QString)
备注：默认会把Qt::EditRole 和 Qt::DisplayRole当做相同的设置
Qt::DecorationRole   1   用图标的形式显示数据(QColor, QIcon or QPixmap)
备注：显示的颜色在单元格中是一个小方块，不能填满整个单元格
Qt::EditRole   2   可编辑修改的文本数据(QString)
Qt::ToolTipRole   3   实现当鼠标处于选中的数据时，显示出数据的相关提示(QString)
Qt::StatusTipRole   4   在状态栏显示提示的数据(QString)
Qt::WhatsThisRole   5   在"What's This?"模式下会显示出来的数据(QString)
Qt::SizeHintRole   13   可以提示相应大小(QSize)

//描述外观和元数据的角色及相关类型
Qt::FontRole   6   可以改变数据的字体(QFont)
Qt::TextAlignmentRole   7   可以将文本的位置进行居中、居左居右调整(Qt::Alignment)
Qt::BackgroundRole   8   可以改变背景色(QBrush)
备注：显示的颜色会填满整个单元格
Qt::ForegroundRole   9   可以改变前景色(QBrush)
Qt::CheckStateRole   10   设置的列则可以显示出一个CheckBox(Qt::CheckState)
Qt::InitialSortOrderRole   14

//可访问性角色及相关类型
Qt::AccessibleTextRole   11   用于辅助功能和插件扩展的文本(如屏幕阅读器)(QString)
Qt::AccessibleDescriptionRole   12   用于无障碍项目的描述(QString)

//用户角色
Qt::UserRole   0x0100   用于应用程序的特定目的(自己定义用途).用户自己决定使用什么数据,如何处理数据
```


## enum Qt::ItemFlag
常用flag的取值  
```
Constant 					Value 			Description
Qt::NoItemFlags 			0 				没有任何属性设置
Qt::ItemIsSelectable 		1 				可以被选中
Qt::ItemIsEditable 			2 				可以被编辑（实际测试是不可被编辑）
Qt::ItemIsDragEnabled 		4 				
Qt::ItemIsDropEnabled 		8 				
Qt::ItemIsUserCheckable 	16 				
Qt::ItemIsEnabled 			32 				
Qt::ItemIsAutoTristate 		64 				
Qt::ItemNeverHasChildren 	128 			
Qt::ItemIsUserTristate 		256 			
```


## enum Qt::ContextMenuPolicy
这个集合定义了widget组件显示上下文菜单的不同形式  
```
Constant					Value	Description
Qt::NoContextMenu			0		
widget没有上下文菜单，上下文菜单的处理遵从与widget的parent
Qt::PreventContextMenu		4		
widget没有上下文菜单，但是和Qt::NoContextMenu相反，widget对上下文菜单的处理与parent无关
所有的鼠标事件都会通过QWidget::mousePressEvent()和QWidget::mouseReleaseEvent()传递给widget自己进行处理
Qt::DefaultContextMenu 		1		
调用QWidget::contextMenuEvent()函数
Qt::ActionsContextMenu 		2		
widget会展示其QWidget::actions()来作为上下文菜单
Qt::CustomContextMenu 		3		
widget会发出QWidget::customContextMenuRequested()信号  
```
