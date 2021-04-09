#include "tictactoetaskmenu.h"

TicTacToeTaskMenu::TicTacToeTaskMenu(TicTacToe *tictactoe2, QObject *parent)
     : QObject(parent)
     //注意这里的两个参数是不一样的，初始化列表
     , tictactoe1(tictactoe2)
{
    //向菜单中插入的自定义选项
    custom_action = new QAction("custom action", this);
    connect(custom_action, &QAction::triggered, this, &TicTacToeTaskMenu::menuTest);
    //注意：在这里调用控件类的成员时，只能用tictactoe1，不能用tictactoe2，否则程序会卡死
    tictactoe1 -> showMessage();
}

//自定义选项触发后关联的槽函数，在这里定义选项关联的具体操作
void TicTacToeTaskMenu::menuTest()
{    
    QMessageBox::about(nullptr, "menu test", "this is a menu test");
}

//重写preferredEditAction()函数
QAction *TicTacToeTaskMenu::preferredEditAction() const
{
    return custom_action;
}

//重写taskActions()函数
QList<QAction *> TicTacToeTaskMenu::taskActions() const
{
    return QList<QAction *>{custom_action};
}

