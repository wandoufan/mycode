# QExtensionFactory

## 基本功能
这个类创建一个factory，可以用来在QT designer中创建自定义扩展的实例  
这个类提供了一个标准的extension factory，也可以被用作自定义extension factory的一个接口  


## 以扩展右键菜单为例的使用方法
1. 方法一
创建一个继承于QExtensionFactory的子类  
创建这个子类的目的就是为了对createExtension函数进行重写  
头文件示例：  
```
#include <QExtensionFactory>
#include "tictactoe.h"
#include "tictactoetaskmenu.h"

class TicTacToeTaskMenuFactory : public QExtensionFactory
{
    Q_OBJECT
public:
    TicTacToeTaskMenuFactory(QExtensionFactory *parent = nullptr);

protected:
    QObject *createExtension(QObject *object, const QString &iid, QObject *parent) const override;
};
```
源文件示例：  
```
QObject *TicTacToeTaskMenuFactory::createExtension(QObject *object,
    const QString &iid, QObject *parent) const
{
     if (iid != Q_TYPEID(QDesignerTaskMenuExtension))
         return nullptr;

     if (TicTacToe *tic = qobject_cast<TicTacToe*>(object))
         return new TicTacToeTaskMenu(tic, parent);

     return nullptr;
}
```

2. 方法二
或者你也可以使用已有的factory，然后扩展QExtensionFactory::createExtension()函数的功能，来使得这个factory能够创建扩展任务菜单  
```
QObject *AGeneralExtensionFactory::createExtension(QObject *object,
         const QString &iid, QObject *parent) const
{
    MyCustomWidget *widget = qobject_cast<MyCustomWidget*>(object);

    if (widget && (iid == Q_TYPEID(QDesignerContainerExtension))) {
        return new MyContainerExtension(widget, parent);

    } else if (widget && (iid == Q_TYPEID(QDesignerTaskMenuExtension))) {
        return new MyTaskMenuExtension(widget, parent);

    } else {
        return 0;
    }
}
```
