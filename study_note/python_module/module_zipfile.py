# zipfile模块是python中用来实现zip压缩包功能的模块,常用类是：ZipFile和ZipInfo
# ZipFile类用来创建和读取zip文件,ZipInfo类用来存储的zip文件的每个文件的信息的
# 其他用来处理不同格式压缩包的模块还有：rarfile, tarfile, gzip

# 注意：实际测试时发现使用非常麻烦，创建压缩文件时需要遍历目标目录中每个文件逐个添加
# 建议尽量使用shell命令'zip -r new_filename.zip filename'可以一步完成

import zipfile  
import os


# 创建压缩包：
zip_file_name = '/root/wgettest/ftptest/zip_test.zip'
z = zipfile.ZipFile(zip_file_name, 'w')
#向压缩文件中添加文件内容  
z.write('source_path','goal_path')  
#关闭压缩文件对象  
z.close()  
#假设要把一个叫testdir中的文件全部添加到压缩包里（这里只添加一级子目录中的文件）
if os.path.isdir(testdir):  
     for d in os.listdir(testdir):  
         z.write(testdir+os.sep+d)  
         # close() 是必须调用的！  
         z.close() 



# 解压压缩包：
z = zipfile.ZipFile(filename, 'r')
# z.infolist(), 它返回的就是压缩包内所有文件的信息，就是一个ZipInfo的列表。
# 一个ZipInfo对象中包含了压缩包内一个文件的信息，其中比较常用的是filename, file_size, header_offset, 
# 分别为文件名，文件大小，文件数据在压缩包中的偏移。  
for i in z.infolist():  
    print(i.filename,i.file_size,i.header_offset) 
#打开压缩文件  
zp = zipfile.ZipFile('xxx/xxxx/xx.zip','r')  
#解压压缩文件中的所有文件(解压指定文件 zp.extrat('指定文件','指定目录'))  
zp.extractall('goal_path')  
#关闭压缩文件对象  
zp.close()  

