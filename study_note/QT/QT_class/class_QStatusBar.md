# QStatusBar

## 基本功能
QStatusBar提供了一个水平的条，非常适合在UI窗口下方显示状态信息  
如果是新建一个MainWindow类型的窗口，会自带QStatusBar  


## 代码示例
```
QLabel *listen_status, *socket_status;
listen_status -> setMinimumWidth(300);
ui -> statusbar -> addWidget(listen_status);

socket_status = new QLabel("socket状态：");
socket_status -> setMinimumWidth(200);
ui -> statusbar -> insertWidget(1, socket_status);
```