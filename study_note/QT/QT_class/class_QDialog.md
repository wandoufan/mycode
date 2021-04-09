# QDialog

## 基本功能
QDialog是所有对话窗口的基类  
对话窗口一般用作临时任务或与用户之间进行交互  


## 常用QDialog对话框类
QColorDialog（颜色对话框）  
QFileDialog（文件对话框）  
QFontDialog（字体对话框）  
QInputDialog（输入对话框）  
QMessageBox（消息对话框）  
QProgressDialog（进度对话框）  
QErrorMessage（错误信息对话框）  
QPageSetupDialog（页面设置对话框）  
QPrintDialog（打印对话框）  
QPrintPreviewDialog（打印预览对话框）  


## 常用属性
* modal : bool (模态)
这个属性用来设置show()函数弹出的dialog对话框是模态还非模态  
默认情况下，这个属性为false，即弹出的dialog对话框是非模态的  
把这个属性设置为true等同于把QWidget::windowModality设置为Qt::ApplicationModal  
另外，exec()函数会忽视这个属性，总是以模态来弹出dialog对话框  
1. bool isModal() const
2. void setModal(bool modal)


## 常用函数
* 
