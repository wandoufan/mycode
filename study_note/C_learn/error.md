# 主要记录C语言中遇到的常见错误

## 写代码时的错误
1. main函数容易写错为mian


## warning
1. warning: return type of 'main' is not 'int'
定义main函数时类型设为void会有此类警告，不影响运行  
如果想消除编译器的警告，将void改为int并且在main函数最后 return 0;  
