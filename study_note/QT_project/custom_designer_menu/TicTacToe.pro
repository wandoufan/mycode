CONFIG      += plugin debug_and_release
TARGET      = $$qtLibraryTarget(tictactoeplugin)
TEMPLATE    = lib

HEADERS     = tictactoeplugin.h \
    tictactoetaskmenu.h \
    tictactoetaskmenufactory.h
SOURCES     = tictactoeplugin.cpp \
    tictactoetaskmenu.cpp \
    tictactoetaskmenufactory.cpp
RESOURCES   = icons.qrc
LIBS        += -L. 

QT      += widgets

greaterThan(QT_MAJOR_VERSION, 4) {
    QT += designer
} else {
    CONFIG += designer
}

target.path = $$[QT_INSTALL_PLUGINS]/designer
INSTALLS    += target

include(tictactoe.pri)
