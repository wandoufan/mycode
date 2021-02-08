#ifndef TICTACTOETASKMENU_H
#define TICTACTOETASKMENU_H

#include <QDesignerTaskMenuExtension>
#include "tictactoe.h"

class TicTacToeTaskMenu : public QObject, public QDesignerTaskMenuExtension
{
    Q_OBJECT
    Q_INTERFACES(QDesignerTaskMenuExtension)
public:
    TicTacToeTaskMenu();

    explicit TicTacToeTaskMenu(TicTacToe *tic, QObject *parent);

    QAction *preferredEditAction() const override;
    QList<QAction *> taskActions() const override;

private slots:
    void editState();

private:
    QAction *editStateAction;
    TicTacToe *ticTacToe;
};

#endif // TICTACTOETASKMENU_H
