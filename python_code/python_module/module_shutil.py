# coding: utf-8

# shutil模块主要对文件进行处理，和OS模块的功能类似

import shutil

# shutil.copyfileobj(文件1，文件2)：将文件1的数据覆盖copy给文件2
f1 = open("1.txt", encoding="utf-8")
f2 = open("2.txt", "w", encoding="utf-8")
shutil.copyfileobj(f1, f2)

# shutil.copyfile(文件1，文件2)：不用打开文件，直接用文件名进行覆盖copy。
shutil.copyfile("1.txt", "2.txt")

# shutil.copy(文件1，文件2)：拷贝文件和权限都进行copy
shutil.copy("1.txt", "2.txt")

# shutil.copystat(文件1，文件2)：仅拷贝状态的信息，即文件属性，包括：mode bits, atime, mtime, flags
shutil.copystat("1.txt", "2.txt")

# shutil.copymode(文件1，文件2)：仅拷贝权限。内容、组、用户均不变
shutil.copymode("1.txt", "2.txt")

# shutil.copy2(文件1，文件2)：拷贝了文件和状态信息
shutil.copy2("1.txt", "2.txt")

# shutil.copytree(源目录，目标目录)：可以递归copy多个目录到指定目录下
shutil.copytree('dir1', 'dir2')

# shutil.rmtree(目标目录)：可以递归删除目录下的目录及文件(目录可以不为空)
shutil.rmtree('dir1')

# shutil.move(源文件，指定路径)：递归移动一个文件
shutil.move('1.txt', 'dir1')

#shutil.make_archive(base_name, format,root_dir,owner,group,logger)创建压缩包并返回文件路径，例如：zip、tar
# base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径
# format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# root_dir： 要压缩的文件夹路径（默认当前目录）
# owner： 用户，默认当前用户
# group： 组，默认当前组
# logger： 用于记录日志，通常是logging.Logger对象
# shutil对压缩包的处理实际是通过调用 ZipFile 和 TarFile 两个模块来进行的
shutil.make_archive('1.txt','zip')


# shutil模块和os模块删除文件的区别：
# 1、os.unlink(path)将删除path处的文件，成功删除后没有任何返回。path是一个文件的完整路径
# 2、os.rmdir(path)将删除path处的文件夹，该文件夹必须为空。其中没有任何文件和文件夹
# 3、shutil.rmtree(path)将删除path处的文件夹，它包含的所有文件和文件夹都将被删除
