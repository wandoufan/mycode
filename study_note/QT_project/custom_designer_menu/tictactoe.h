#ifndef TICTACTOE_H
#define TICTACTOE_H

#include <QWidget>
#include <QPushButton>
#include <QAction>
#include <QExtensionManager>
#include <QMessageBox>
#include <QVBoxLayout>

class TicTacToe : public QWidget
{
    Q_OBJECT

public:
    TicTacToe(QWidget *parent = 0);
    void showMessage();

private:
    QPushButton *mybutton;
    QVBoxLayout *mylayout;
};

#endif // TICTACTOE_H
