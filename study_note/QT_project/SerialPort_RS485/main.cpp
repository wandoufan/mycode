#include "serialport485.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SerialPort485 w;
    w.show();
    return a.exec();
}
