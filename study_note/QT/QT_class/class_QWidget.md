# QWidget

## 基本功能
QWidget是所有用户接口对象(具有可视界面组件)的基类  
QWidget在没有指定父容器时可以作为独立的窗口，指定父容器之后可以作为父容器的内部组件  
选择QWidget创建的界面对各种界面组件都可以支持  
QWidget窗口可以被其父窗口或其他窗口挡住一部分  
父类：QObject、QPaintdevice  
子类：  
```
QAbstractButton, QAbstractSlider, QAbstractSpinBox, QCalendarWidget, QComboBox, QDesignerActionEditorInterface, QDesignerFormWindowInterface, QDesignerObjectInspectorInterface, QDesignerPropertyEditorInterface, QDesignerWidgetBoxInterface, QDesktopWidget, QDialog, QDialogButtonBox, QDockWidget, QFocusFrame, QFrame, QGroupBox, QKeySequenceEdit, QLineEdit, QMacCocoaViewContainer, QMacNativeWidget, QMainWindow, QMdiSubWindow, QMenu, QMenuBar, QOpenGLWidget, QProgressBar, QQuickWidget, QRubberBand, QSizeGrip, QSplashScreen, QSplitterHandle, QStatusBar, QSvgWidget, QTabBar, QTabWidget, QToolBar, and QWizardPage
```


## todo_list
整理QWidget中的函数
尤其是结合PluginDetailsView中记录的函数，如show()


## 常用成员变量
1. acceptDrops : bool

2. accessibleDescription : QString

3. accessibleName : QString

4. autoFillBackground : bool

5. baseSize : QSize
这个属性用来设置widget的base size，对于新创建的widget，宽高默认都是0  
当widget定义了sizeIncrement()时，base size用来计算一个合适的widget尺寸  
5.1 QSize baseSize() const
5.2 void setBaseSize(const QSize &)
5.3 void setBaseSize(int basew, int baseh)

6. childrenRect : const QRect

7. childrenRegion : const QRegion

8. contextMenuPolicy : Qt::ContextMenuPolicy
这个属性设置widget显示菜单栏的方式，默认值为Qt::DefaultContextMenu  
属性取值详见namespace中的enum Qt::ContextMenuPolicy  
8.1 Qt::ContextMenuPolicy contextMenuPolicy() const
8.2 void setContextMenuPolicy(Qt::ContextMenuPolicy policy)

9. cursor : QCursor

10. enabled : bool
这个属性设置widget是否使能  
enabled的widget可以处理键盘和鼠标的事件，disabled的widget则不能
备注：QAbstractButton除外  
有的widget在变成disabled之后外观会发生变化，例如变成灰色  
对一个父widget进行使能设置时，同样会影响到其子widget  
10.1 bool isEnabled() const
10.2 void setEnabled(bool)

11. focus : const bool
这个属性设置widget是否能够获得键盘的输入焦点，默认为false  
备注：这个属性等同于检查QApplication::focusWidget()  
11.1 bool hasFocus() const

12. focusPolicy : Qt::FocusPolicy

13. font : QFont

14. frameGeometry : const QRect

15. frameSize : const QSize

16. fullScreen : const bool

17. geometry : QRect

18. height : const int

19. inputMethodHints : Qt::InputMethodHints

20. isActiveWindow : const bool

21. layoutDirection : Qt::LayoutDirection

22. locale : QLocale

23. maximized : const bool

24. maximumHeight : int

25. maximumSize : QSize

26. maximumWidth : int

27. minimized : const bool

28. minimumHeight : int

29. minimumSize : QSize

30. minimumSizeHint : const QSize

31. minimumWidth : int

32. modal : const bool

33. mouseTracking : bool

34. normalGeometry : const QRect

35. palette : QPalette

36. pos : QPoint

37. rect : const QRect

38. size : QSize

39. sizeHint : const QSize

40. sizeIncrement : QSize

41. sizePolicy : QSizePolicy

42. statusTip : QString

43. styleSheet : QString

44. tabletTracking : bool

45. toolTip : QString

46. toolTipDuration : int

47. updatesEnabled : bool

48. visible : bool

49. whatsThis : QString

50. width : const int

51. windowFilePath : QString

52. windowFlags : Qt::WindowFlags

53. windowIcon : QIcon

54. windowModality : Qt::WindowModality
这个属性用来设置哪个windows窗口会被模态的widget锁住  
这个属性只对windows窗口有意义，默认值为Qt::NonModal  
属性的取值详见namespace中的enum Qt::WindowModality  
一个模态的widget会阻止其他窗口的widget获取到输入  
把QWidget::windowModality设置为Qt::ApplicationModal等同于把Qialog::modal属性设置为true  
54.1 Qt::WindowModality windowModality() const
54.2 void setWindowModality(Qt::WindowModality windowModality)

55. windowModified : bool

56. windowOpacity : double

57. windowTitle : QString

58. x : const int

59. y : const int



-------------------
[slot] void QWidget::setFocus()
void QWidget::clearFocus()