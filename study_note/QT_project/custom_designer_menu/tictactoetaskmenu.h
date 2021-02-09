#ifndef TICTACTOETASKMENU_H
#define TICTACTOETASKMENU_H

#include <QDesignerTaskMenuExtension>
#include "tictactoe.h"

//扩展菜单类必须继承自QObject和QDesignerTaskMenuExtension
class TicTacToeTaskMenu : public QObject, public QDesignerTaskMenuExtension
{
    Q_OBJECT
    //这里必须要用Q_INTERFACES宏进行声明
    Q_INTERFACES(QDesignerTaskMenuExtension)
public:
    explicit TicTacToeTaskMenu(TicTacToe *tic, QObject *parent);

    QAction *preferredEditAction() const override;
    QList<QAction *> taskActions() const override;

private slots:
    void menuTest();

private:
    QAction *custom_action;
    TicTacToe *tictactoe1;
};

#endif // TICTACTOETASKMENU_H
