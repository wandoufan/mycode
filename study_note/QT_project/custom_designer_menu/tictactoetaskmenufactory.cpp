#include "tictactoetaskmenufactory.h"

TicTacToeTaskMenuFactory::TicTacToeTaskMenuFactory(QExtensionManager *parent)
     : QExtensionFactory(parent)
{

}

//对createExtension()函数进行重写
QObject *TicTacToeTaskMenuFactory::createExtension(QObject *object,
                         const QString &iid, QObject *parent) const
{
     if (iid != Q_TYPEID(QDesignerTaskMenuExtension))
         return nullptr;

     if (TicTacToe *tic = qobject_cast<TicTacToe*>(object))
         return new TicTacToeTaskMenu(tic, parent);

     return nullptr;
}
