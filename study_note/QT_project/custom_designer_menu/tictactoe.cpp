#include "tictactoe.h"

TicTacToe::TicTacToe(QWidget *parent) :
    QWidget(parent)
{
   mybutton = new QPushButton("custom button");
   mybutton -> setFixedSize(100, 50);
   mylayout = new QVBoxLayout(this);
   mylayout -> addWidget(mybutton);
   this -> setLayout(mylayout);
   this -> setFixedSize(150, 80);
}

//用于测试在TicTacToeTaskMenu中调用TicTacToe的成员函数
void TicTacToe::showMessage()
{
    QMessageBox::about(this, "show message", "show message test");
}
