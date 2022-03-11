# QStackedWidget

## 基本功能
QStackedWidget像栈一样把widget组件存储起来，并且一次只显示一个  
QStackedWidget和QTabWidget功能类似，但它的成员只能是widget组件  
QStackedWidget是一个便捷的布局控件，基于QStackedLayout控件构建  


## 代码示例
```
QWidget *firstPageWidget = new QWidget;
QWidget *secondPageWidget = new QWidget;
QWidget *thirdPageWidget = new QWidget;

QStackedWidget *stackedWidget = new QStackedWidget;
stackedWidget->addWidget(firstPageWidget);
stackedWidget->addWidget(secondPageWidget);
stackedWidget->addWidget(thirdPageWidget);

stackedWidget->setCurrentIndex(0);
stackedWidget->setCurrentIndex(1);
stackedWidget->setCurrentIndex(2);
```