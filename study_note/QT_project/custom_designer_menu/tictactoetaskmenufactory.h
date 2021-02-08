#ifndef TICTACTOETASKMENUFACTORY_H
#define TICTACTOETASKMENUFACTORY_H


#include <QExtensionFactory>
#include "tictactoe.h"
#include "tictactoetaskmenu.h"

class TicTacToeTaskMenuFactory : public QExtensionFactory
{
    Q_OBJECT
public:
    explicit TicTacToeTaskMenuFactory(QExtensionManager *parent = nullptr);

protected:
    QObject *createExtension(QObject *object, const QString &iid, QObject *parent) const override;
};

#endif // TICTACTOETASKMENUFACTORY_H
