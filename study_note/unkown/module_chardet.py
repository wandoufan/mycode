# coding:utf-8

# chardet常用实现编码方面的功能....
# 可以用来设置打开文件时的编码格式

# 参考资料：
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001510905171877ca6fdf08614e446e835ea5d9bce75cf5000


# 使用样例：
if not os.path.isfile(file_name):
    logging.error('there is no file named %s, please check the path and input again!' % file_name)
    return None
else:
    import chardet
    f = open(file_name, 'rb')
    result = chardet.detect(f.readline())
    # print(result)
    file_encodes = 'utf-8'
    if 'utf' not in result['encoding']:
        file_encodes = 'gb18030'
    f.close()
    f = open(file_name, encoding=file_encodes)
    lines = f.readlines()
    f.close()
    text = ' '.join(lines)