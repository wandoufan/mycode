import ftplib
import os

# 1.传递之前要检查目标目录是否是空的
# 2.传递结束之后要检查传输是否成功(检查文件个数？？)
# 3.考虑目录内容列表为空，即空目录的情况-->建一个空目录，然后回退到上一级

class MyFtp(object):
	"""
	实现ftp传输复杂文件目录的功能,
	递归的判断目标数据是文件还是目录，
	然后执行不同的操作
	"""
	ftp = ftplib.FTP()

	def __init__(self, host, port, username, password):
		'''
		初始化连接登录ftp
        param host:ftp主机
        param port:ftp端口
        param username:用户名
        param password:密码
		'''
		self.ftp.set_debuglevel(2)
		self.ftp.connect(host, port)
		self.ftp.login(username, password)

	def check_is_empty(self,dir):
		'''
		上传下载之前检查目标目录是否为空，不为空就报错
		'''
		pass

	def upload_file(self, localfile, remotepath):
		'''
		上传单个文件
		:param localfiel:要上传的本地文件(path1/path2/filename)
		:param remotefile:要上传到ftp上的目标路径(path1/path2)
		:return:code,msg
		'''
		if os.path.isfile(localfile) == False:
			code = -1
			msg = 'not a file'
			return code, msg
		filename = os.path.basename(localfile)
		remotefile = os.path.join(remotepath, filename)
		upload_file = open(localfile, 'rb')
		self.ftp.storbinary('STOR %s' % remotefile, upload_file)
		upload_file.close()
		return 0, 'OK'

	def upload_directory(self, localdir, remotepath):
		'''
		上传目录
		:param localdir:要上传的本地目录
		:param remotedir:要上传到ftp上的目标路径
		return:code,msg
		'''
		# 在ftp上创建对应的目录并设置为工作目录
		self.ftp.cwd(remotepath)
		dirname = os.path.basename(localdir)
		self.ftp.mkd(dirname)
		remotepath = os.path.join(remotepath,dirname)
		self.ftp.cwd(remotepath)

		file_list = os.listdir(localdir)
		if len(file_list) == 0:
			return 0, 'directory is empty'

		for file in file_list:
			if os.path.isfile(os.path.join(localdir, file)):
				localfile = os.path.join(localdir, file)
				code, msg = self.upload_file(localfile, remotepath)
				if code == -1:
					return code, msg
				if code == 0:
					continue
			else:
				localdir = os.path.join(localdir, file)
				code, msg = self.upload_directory(localdir, remotepath)
				# 遍历结束把路径改回上一层目录
				localdir = os.path.dirname(localdir)
				if code == -1:
					return code, msg
				if code == 0:
					continue
		return 0, 'OK'

	def start_upload(self, localdir, remotepath):
		'''
		开始上传，首先判断要上传的数据是文件还是目录
		:param localdir:要上传的本地目录
		:param remotedir:要上传到ftp上的目标路径
		return:code,msg
		'''
		# 如果localdir是文件直接上传，否则调用目录上传函数
		if os.path.isfile(localdir):
			code, msg = self.upload_file(localdir, remotepath)
			if code == -1:
				return code, msg
		else:
			code, msg = self.upload_directory(localdir, remotepath)
			if code == -1:
				return code, msg
		return 0, 'OK'

if __name__ == '__main__':
    host = '192.168.109.133'
    port = 21
    user = 'user'
    password = '123456'

    myftp = MyFtp(host,port,user,password)
    
    localdir = '/root/ftptest/abc'
    remotepath = '/home/user/ftptest'
    myftp.start_upload(localdir,remotepath)
