#include "tictactoetaskmenu.h"

TicTacToeTaskMenu::TicTacToeTaskMenu(TicTacToe *tic, QObject *parent)
     : QObject(parent)
//     , editStateAction(new QAction(tr("Edit State"), this))
//     , ticTacToe(tic)
{
    editStateAction = new QAction("edit state", this);
    connect(editStateAction, &QAction::triggered, this, &TicTacToeTaskMenu::editState);
}

void TicTacToeTaskMenu::editState()
{
    QMessageBox::about(nullptr, "menu test", "this is a menu test");
}

QAction *TicTacToeTaskMenu::preferredEditAction() const
{
    return editStateAction;
}

QList<QAction *> TicTacToeTaskMenu::taskActions() const
{
    return QList<QAction *>{editStateAction};
}

