# 主要记录C语言中遇到的常见错误

## main函数容易写错为mian

## warning: return type of 'main' is not 'int'
* 定义main函数时类型设为void会有此类警告，不影响运行
* 如果想消除编译器的警告，将void改为int并且在main函数最后 return 0;

## waring:variable set but not used
* 定义了变量但是却没有使用