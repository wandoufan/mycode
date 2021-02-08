#ifndef TICTACTOE_H
#define TICTACTOE_H

#include <QWidget>
#include <QPushButton>
#include <QAction>
#include <QExtensionManager>
#include <QMessageBox>

class TicTacToe : public QWidget
{
    Q_OBJECT

public:
    TicTacToe(QWidget *parent = 0);

private:
    QPushButton *mybutton;
};

#endif // TICTACTOE_H
