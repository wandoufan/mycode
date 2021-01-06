## QPalette

## 基本功能
Qpalette(调色板)类是专门用于管理组件的外观颜色的类  
每个组件都有一个palette属性，可以用来进行颜色相关的设置  
```
QPalette plet = ui -> plainTextEdit -> palette();
plet.setColor(QPalette::Text, Qt::blue);//设置窗口中文字的颜色
ui -> plainTextEdit -> setPalette(plet);
```

## 常用参数
1. 设置颜色显示区域的参数包括：  
QPalette::Base 设置文本输入窗口部件(如QtextEdit等)的底色  
QPalette::Text 设置文本输入窗口中文字的颜色  
QPalette:WindowText 通常指窗口看不见的前景色  
QPalette::Button 指按钮窗口部件的背景色  
QPalette::ButtonText 指按钮窗口部件的前景色  
QPalette::Background 背景色  
QPalette::Foreground 前景色  
2. 常用设置颜色的参数包括：  
Qt::black 黑色  
Qt::blue 蓝色  
Qt::red 红色  
Qt::yellow 黄色  
QColor(10, 100 , 50, 255) 用数字设置颜色  