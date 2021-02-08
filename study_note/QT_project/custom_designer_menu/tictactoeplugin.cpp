#include "tictactoe.h"
#include "tictactoeplugin.h"
#include "tictactoetaskmenufactory.h"

#include <QtPlugin>

TicTacToePlugin::TicTacToePlugin(QObject *parent)
    : QObject(parent)
{
    m_initialized = false;
}

void TicTacToePlugin::initialize(QDesignerFormEditorInterface *formEditor)
{
    if (m_initialized)
        return;

    QExtensionManager *manager = formEditor -> extensionManager();
    Q_ASSERT(manager != 0);

    manager->registerExtensions(new TicTacToeTaskMenuFactory(manager),
                                Q_TYPEID(QDesignerTaskMenuExtension));

    // Add extension registrations, etc. here

    m_initialized = true;
}

bool TicTacToePlugin::isInitialized() const
{
    return m_initialized;
}

QWidget *TicTacToePlugin::createWidget(QWidget *parent)
{
    return new TicTacToe(parent);
}

QString TicTacToePlugin::name() const
{
    return QLatin1String("TicTacToe");
}

QString TicTacToePlugin::group() const
{
    return QLatin1String("custom");
}

QIcon TicTacToePlugin::icon() const
{
    return QIcon();
}

QString TicTacToePlugin::toolTip() const
{
    return QLatin1String("");
}

QString TicTacToePlugin::whatsThis() const
{
    return QLatin1String("");
}

bool TicTacToePlugin::isContainer() const
{
    return false;
}

QString TicTacToePlugin::domXml() const
{
    return QLatin1String("<widget class=\"TicTacToe\" name=\"ticTacToe\">\n</widget>\n");
}

QString TicTacToePlugin::includeFile() const
{
    return QLatin1String("tictactoe.h");
}
#if QT_VERSION < 0x050000
Q_EXPORT_PLUGIN2(tictactoeplugin, TicTacToePlugin)
#endif // QT_VERSION < 0x050000
