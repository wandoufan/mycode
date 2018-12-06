# coding:utf-8
# 关于assert断言的用法
# 当断言的条件为假时会产生一个AssertionError报错，一般用作测试程序的检查点

# 常见用法如下：
condition = False
# assert condition
# 逻辑上等同于：
# if not condition:
#     raise AssertionError('assert用法测试')

# 在断言表达式后可以直接添加字符串信息来说明出错原因，相当于在错误类型中写说明
a = 2
# assert a < 1, '参数超出范围'