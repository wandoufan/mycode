# QT中的.qml文件

## 基本功能
.qml文件用来描述UI界面，相当于一个.ui文件  
使用qml时候需要设置资源文件，即.qrc文件，用来添加qml资源，否则无法进行加载qml所显示的图片等内容  
UI界面在文件中也是以代码的形式存在，如果想直接查看UI界面，在Qt creator中'工具-外部-Qt Quick-Qt Quick 2 Preview(qmlscene)'  


## qml的缓存机制
Qt Widget工程，如果修改了cpp代码后，直接构建或者直接运行，编译器都会重新编译最新的代码进而运行展示  
但是qml工程却不是这样，每次修改qml文件后，直接build并不总是加载最新代码，经常需要“清除-构建-运行”  
这是由于qml和前端javascript类似，具有缓存机制，加载的还是上次缓存中的内容  
即.qml文件第一次运行后会生成一个同名的.qmlc文件，详见file_qmlc.md  


## 文件示例
.qml文件  
```
import QtQuick 2.12
import QtQuick.Window 2.12

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
}
```
对应的.cpp文件  
```
#include <QGuiApplication>
#include <QQmlApplicationEngine>

int main(int argc, char *argv[])
{
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif

    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    const QUrl url(QStringLiteral("qrc:/main.qml"));
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
                     &app, [url](QObject *obj, const QUrl &objUrl) {
        if (!obj && url == objUrl)
            QCoreApplication::exit(-1);
    }, Qt::QueuedConnection);
    engine.load(url);

    return app.exec();
}
```