# 条件编译



只编译一次
```
#pragma once
```


当预处理器预处理到#error命令时将停止编译并输出用户自定义的错误消息
```
#ifndef __AFXWIN_H__
	#error
#endif
```