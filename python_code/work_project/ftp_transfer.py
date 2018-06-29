#!/bin/env python
# -*- encoding: utf8 -*-


import ftplib
import os

class FtpTransfer(object):
	"""
	实现训练数据目录下载
	和训练结果/评估结果上传的功能
	"""
	ftp = ftplib.FTP()

	# 目前ftp的地址、端口、账号、密码已经写入代码，如果后续这些信息成为变量，
	# 需要每次在run.py中调用ftp功能模块时传入新的信息
	def __init__(self, host='10.145.84.178', port=8881, username='ftpuser', password='yeying123'):
		'''
		初始化连接登录ftp
		:param host:ftp主机
		:param port:ftp端口
		:param username:用户名
		:param password:密码
		'''
		self.ftp.set_debuglevel(2)
		self.ftp.connect(host, port)
		self.ftp.login(username, password)

	# create_zipfile函数仅用于ftp模块内部，被上传函数调用
	def create_zipfile(self, zip_file_path, data_type):
		'''
		创建zip格式的压缩包 
		:param zip_file_path：要进行压缩的文件所在目录的路径
		:data_type：要进行压缩的数据类型，train-data或evaluation-data
		:return:code,msg
		'''
		os.chdir(zip_file_path)
		# 对于训练结果打包，仅要求压缩/home/work/workdir/model-data/V0.85/output/release目录下的network文件夹，
		# 和network同级的其他几个文件不需要打包
		if data_type == 'train-data':
			cmd = 'zip -r release.zip network'
		# 对于评估结果打包，要求压缩/home/work/workdir/assessment-data/V0.85/2/output/release目录下的所有内容
		if data_type == 'evaluation-data':
			cmd = 'zip -r release.zip *'
		os.system(cmd)
		if os.path.isfile(os.path.join(zip_file_path, 'release.zip')):
			return 0, 'OK'
		else:
			code = -1
			msg = 'create zip file failed'
			return code, msg

	# unzip_file函数仅用于ftp模块内部，被下载函数调用
	def unzip_file(self, localpath, zip_file_path):
		'''
		对zip格式的压缩包进行解压
		:param localpath：要进行解压缩的文件所在目录的路径
		:param zip_file_path：要进行解压缩的文件的路径
		:return:code,msg
		'''
		if not os.path.isfile(zip_file_path):
			code = -1
			msg = 'local release.zip not exist'
			return code, msg
		else:
			cmd = 'unzip %s -d %s' %(zip_file_path, localpath)
			os.system(cmd)
			if not os.path.isdir(os.path.join(localpath, 'network')):
				code = -1
				msg = 'unzip release.zip failed'
				return code, msg				
			else:
				return 0, 'OK'

	def download_train_data(self, version, user='ftpuser', password='yeying123'):
		'''
		wget方式从ftp下载执行训练任务需要的train-data数据
		ftp上训练数据路径：train-data/V0.01
		:param user:用户名
		:param password:密码
		:param version:版本名，例如V0.01
		return code,msg
		'''
		localpath = '/home/work/workdir/train-data'
		remotepath = 'train-data/%s' %version
		# 下载前检查ftp服务器上对应的数据是否存在
		self.ftp.cwd('train-data')
		data_list = self.ftp.nlst()
		if version not in data_list:
			code = -1
			msg = 'ftp train-data %s not found' %version
			return code, msg

		# 下载前检查本地目标路径中是否已经存在数据,如果已存在就以ftp为基准覆盖本地数据
		local_train_data = os.path.join(localpath,version)
		if os.path.isdir(local_train_data):
			os.chdir(localpath)
			cmd4 = 'rm -rf %s' %version
			os.system(cmd4)

		cmd1 = 'wget -nH -r -l inf -P %s --ftp-user=%s --ftp-password=%s ftp://10.145.84.178:8881/%s' %(localpath, user, password, remotepath)
		os.system(cmd1)
		# 下载到本地后要把目标数据从上层目录中挪出来，之后再删除上层目录
		# 下载到本地目录：/home/work/workdir/train-data/train-data/V0.01
		cmd2 = 'mv %s/train-data/%s %s/%s' %(localpath, version, localpath, version)
		os.system(cmd2)
		cmd3 = 'rmdir %s/train-data' %localpath
		os.system(cmd3)

		# 检查数据是否下载成功
		if os.path.isdir(local_train_data):
			return 0, 'OK'
		else:
			code = -1
			msg = 'download ftp train-data failed'
			return code, msg

	def download_test_data(self, version, dataset_id, user='ftpuser', password='yeying123'):
		'''
		wget方式从ftp下载执行评估任务需要的test-data数据
		ftp上测试数据路径：test-data/V0.01
		:param user:用户名
		:param password:密码
		:param version:版本名，例如V0.01
		return code,msg
		'''
		localpath = '/home/work/workdir/test-data'
		# 下载测试数据只需要下载test-data/version下具体某一个data_setid,
		# test-data中一个version目录下可能存在多个data_setid,不需要下载整个version
		remotepath = '/test-data/%s/%s' %(version, dataset_id)
		# 下载前检查ftp服务器上对应的数据是否存在
		self.ftp.cwd('test-data')
		data_list = self.ftp.nlst()
		if version not in data_list:
			code = -1
			msg = 'ftp test-data %s not found' %version
			return code, msg

		# 下载前检查本地目标路径中是否已经存在数据,如果已存在就以ftp为基准覆盖本地数据
		local_test_data = os.path.join(localpath,version)
		if os.path.isdir(local_test_data):
			os.chdir(localpath)
			cmd4 = 'rm -rf %s' %version
			os.system(cmd4)

		cmd1 = 'wget -nH -r -l inf -P %s --ftp-user=%s --ftp-password=%s ftp://10.145.84.178:8881/%s' %(localpath, user, password, remotepath)
		os.system(cmd1)
		# 下载到本地后要把目标数据从上层目录中挪出来，之后再删除上层目录
		# 下载到本地目录：/home/work/workdir/test-data/test-data/V0.01
		cmd2 = 'mv %s/test-data/%s %s/%s' %(localpath, version, localpath, version)
		os.system(cmd2)
		cmd3 = 'rmdir %s/test-data' %localpath
		os.system(cmd3)

		# 检查数据是否下载成功
		if os.path.isdir(local_test_data):
			return 0, 'OK'
		else:
			code = -1
			msg = 'download ftp test-data failed'
			return code, msg

	def download_model_data(self, version, user='ftpuser', password='yeying123'):
		'''
		wget方式从ftp下载执行评估任务需要的model-data数据
		ftp上的训练结果数据路径：model-data/V0.01/output/release
		:param user:用户名
		:param password:密码
		:param version:版本名，例如V0.01
		return code,msg
		'''
		# 从ftp上/model-data/%s/output/release目录中下载的数据包括两部分：
		# 一部分是由network文件夹打包成的release.zip，压缩包一般是之前执行训练任务后自动上传到ftp的；
		# 另一部分是和release.zip同级的几个文件，例如intent_id_mapping.dict、intent_template.dict、
		# word_intent_mapping.dict等，这几个文件姜健在调用执行评估任务前会由他上传到ftp上
		localpath = '/home/work/workdir/model-data/%s/output/release' %version
		remotepath = '/model-data/%s/output/release' %version
		remotepath_2 = 'model-data/%s/output/release' %version
		# 下载前检查ftp服务器上对应的release目录下是否有数据
		self.ftp.cwd(remotepath)
		data_list = self.ftp.nlst()
		if len(data_list) == 0:
			code = -1
			msg = 'ftp path %s is empty' %remotepath
			return code, msg

		# 下载前检查本地目标路径中是否已经存在数据,如果已存在就以ftp为基准覆盖本地数据
		# 下载前先清空本地release目录下的数据
		if os.path.isdir(localpath):
			os.chdir(localpath)
			cmd1 = 'rm -rf *'
			os.system(cmd1)

		cmd2 = 'wget -nH -r -l inf -P %s --ftp-user=%s --ftp-password=%s ftp://10.145.84.178:8881/%s' %(localpath, user, password, remotepath)
		os.system(cmd2)
		# 下载到本地后要把目标数据从上层目录中挪出来，之后再删除上层目录
		# 下载到本地目录：/home/work/workdir/model-data/V0.01/output/release/model-data/V0.01/output/release
		# 把上层的release目录改名为release-1，把目标目录release挪到和release-1同层级，再把release-1目录删掉
		newpath = '%s-1' %localpath
		realpath = os.path.join(newpath, remotepath_2)
		cmd3 = 'mv %s %s' %(localpath, newpath)
		cmd4 = 'mv %s %s' %(realpath, localpath)
		cmd5 = 'rm -rf %s' %newpath
		os.system(cmd3)
		os.system(cmd4)
		os.system(cmd5)

		# 检查数据是否下载成功
		if len(os.listdir(localpath)) == 0:
			code = -1
			msg = 'download ftp model-data failed'
			return code, msg
		else:
			zip_file_path = os.path.join(localpath, 'release.zip')
			code, msg = self.unzip_file(localpath, zip_file_path)
			if code == -1:
				return code, msg
			else:
				return 0, 'OK'

	def upload_train_data(self, version):
		'''
		向ftp上传压缩包格式的训练结果
		本地训练结果:/home/work/workdir/model-data/V0.01/output/release/network 
		ftp上训练结果路径: model-data/V0.01/output/release
		:param version: 版本名，例如V0.01
		:return:code,msg
		'''
		localpath = '/home/work/workdir/model-data/%s/output/release' %version
		remotepath = '/model-data/%s/output/release' %version
		# 上传前检查要上传的数据在本地是否存在
		if not os.path.isdir(localpath):
			code = -1
			msg = 'local model-data not exist'
			return code, msg
		# 上传前检查ftp上对应路径是否存在，如果不存在，需要先逐层建立目录
		self.ftp.cwd('/')
		if 'model-data' not in self.ftp.nlst():
			self.ftp.mkd('model-data')
		self.ftp.cwd('model-data')
		if version not in self.ftp.nlst():
			self.ftp.mkd(version)
		self.ftp.cwd(version)
		if 'output' not in self.ftp.nlst():
			self.ftp.mkd('output')
		self.ftp.cwd('output')
		if 'release' not in self.ftp.nlst():
			self.ftp.mkd('release')
		self.ftp.cwd('release')
		# 开始上传文件
		data_type = 'train-data'
		code, msg = self.create_zipfile(localpath, data_type)
		if code == -1:
			return code, msg
		zipfile = os.path.join(localpath, 'release.zip')
		upload_file = open(zipfile,'rb')
		self.ftp.storbinary('STOR %s/release.zip' %remotepath, upload_file)
		upload_file.close()
		# 检查文件是否上传成功
		self.ftp.cwd(remotepath)
		if 'release.zip' not in self.ftp.nlst():
			code = -1
			msg = 'upload model-data failed'
			return code, msg
		else:
			return 0, 'OK'

	def upload_evaluation_data(self, version, dataset_id):
		'''
		向ftp上传压缩包格式的评估结果
		本地评估结果:/home/work/workdir/assessment-data/V0.01/2/output/release/release.zip
		ftp上评估结果路径：assessment-data/V0.01/2/output/release 
		:param version: 版本名，例如V0.01
		:return:code,msg
		'''
		localpath = '/home/work/workdir/assessment-data/%s/%s/output/release' %(version, dataset_id)
		remotepath = '/assessment-data/%s/%s/output/release' %(version, dataset_id)
		# 上传前检查要上传的数据在本地是否存在
		if not os.path.isdir(localpath):
			code = -1
			msg = 'local assessment-data not exist'
			return code, msg
		# 上传前检查ftp上对应路径是否存在，如果不存在，需要先逐层建立目录
		self.ftp.cwd('/')
		if 'assessment-data' not in self.ftp.nlst():
			self.ftp.mkd('assessment-data')
		self.ftp.cwd('assessment-data')
		if version not in self.ftp.nlst():
			self.ftp.mkd(version)
		self.ftp.cwd(version)
		if dataset_id not in self.ftp.nlst():
			self.ftp.mkd(dataset_id)
		self.ftp.cwd(dataset_id)
		if 'output' not in self.ftp.nlst():
			self.ftp.mkd('output')
		self.ftp.cwd('output')
		if 'release' not in self.ftp.nlst():
			self.ftp.mkd('release')
		self.ftp.cwd('release')
		# 开始上传文件
		data_type = 'evaluation-data'
		code, msg = self.create_zipfile(localpath, data_type)
		if code == -1:
			return code, msg
		zipfile = os.path.join(localpath, 'release.zip')
		upload_file = open(zipfile,'rb')
		self.ftp.storbinary('STOR %s/release.zip' %remotepath, upload_file)
		upload_file.close()

		# 检查文件是否上传成功
		self.ftp.cwd(remotepath)
		if 'release.zip' not in self.ftp.nlst():
			code = -1
			msg = 'upload assessment-data failed'
			return code, msg
		else:
			return 0, 'OK'


#if __name__ == '__main__':
	# ftptransfer=FtpTransfer()
	# ftptransfer.create_zipfile('/home/work/workdir/model-data/V0.71/output/release')
	# 	host = '10.145.84.178'
	# 	port = 8881
	# 	user = 'ftpuser'
	# 	password = 'yeying123'

	# 	version = 'V0.61'

	# 	download_localpath = '/home/work/workdir/train-data'
	# 	download_localpath = '/home/work/workdir/ftp-test'
	# 	download_remotepath = 'train-data/%s' %version

	# 	upload_train_localpath = '/home/work/workdir/model-data/%s/output/release' %version
	# 	upload_train_remotepath = '/model-data/%s/output' %version

	# 	upload_evaluation_localpath = '/home/work/workdir/assessment-data/%s/2/output/release' %version
	# 	upload_evaluation_remotepath = '/assessment-data/%s/2/output' %version

	# 	code, msg = ftptransfer.download(version)
	# 	print('!!!!!',code,msg)
	# 	code, msg = ftptransfer.upload_train_data(version)
	# 	print('!!!!!',code,msg)
	# 	code, msg = ftptransfer.upload_evaluation_data(version)
	# 	print('!!!!!',code,msg)




