# 关于windows系统的知识

## C盘下的syswow64和system32目录
参考资料：  
> https://blog.csdn.net/oncealong/article/details/50477997
对于64位的Windows操作系统，C：\Windows下有syswow64和system32两个目录  
两个目录都是存放系统文件的，但和目录名称刚好相反：  
System32的文件夹装的是64位的系统文件，而SysWow64文件夹装的是32位的系统文件  
WOW64 (Windows-on-Windows 64-bit)是一个Windows操作系统的子系统  
它为现有的 32 位应用程序提供了 32 位的模拟，可以使大多数 32 位应用程序在无需修改的情况下运行在 Windows 64 位版本上  


## windows server backup
windows server backup是windows系统自带的免费备份软件  
在windows server系统上可以直接添加安装该功能  
windows server backup功能上具有非常多的局限性：  
1. 默认只能设置一个定期备份计划，无法对多个目录的数据分别进行备份
2. 默认是增量备份，数据恢复时需要所有的备份文件都完整，无法设置为全量备份
windows server backup的备份文件不是按每次备份单独存为一个文件  
而是把所有备份都叠加为一个文件，文件名显示为最新备份的版本号  
因此无法通过删除文件夹来删除多余备份，只能用wbadmin命令去删除  
3. 设置备份路径时只能指定到磁盘，无法具体到指定文件夹内
4. 备份周期只能选择一天一次或一天几次，无法设置一周一次备份
这个可以通过计划任务想办法修改  
在任务计划程序（本地）-任务计划程序库 –Microsoft-Windows-Backup中进行设置  
5. 无法设置备份副本的个数，多余的备份副本会一直存在直到占满磁盘空间
但增量备份的好处是不会每次都产生一个完整的备份文件，从而占用过多磁盘空间  
这个可以通过命令'wbadmin delete backup -keepVersions:3'来自动删除多余的备份  