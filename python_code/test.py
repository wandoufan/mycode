import ftplib
import os


class MyFtp(object):
    """
    实现训练数据目录下载
    和训练结果/评估结果上传的功能
    """
    ftp = ftplib.FTP()

    def __init__(self, host, port, username, password):
        '''
        初始化连接登录ftp
        :param host:ftp主机
        :param port:ftp端口
        :param username:用户名
        :param password:密码
        '''
        # 连接或登录失败时返回信息？
        self.ftp.set_debuglevel(2)
        self.ftp.connect(host, port)
        self.ftp.login(username, password)

    def create_zipfile(self, zip_file_path):
        '''
        创建zip格式的压缩包 
        :param zip_file_path：要进行压缩的数据的路径
        :return:code,msg
        '''
        os.chdir(zip_file_path)
        cmd = 'zip -r release.zip *'
        os.system(cmd)
        if os.path.isfile(os.path.join(zip_file_path, 'release.zip')):
            return 0, 'OK'
        else:
            code = -1
            msg = 'create zip file failed'
            return code, msg

    def download(self, user, password, localpath, remotepath):
        '''
        wget方式从ftp下载train-data数据
        ftp训练数据路径：train-data/V0.1
        :param user:用户名
        :param password:密码
        :param localpath:要下载数据到本地的路径
        :param download_remotepath:要从ftp上下载数据的路径
        return code,msg
        '''
        # 下载前检查ftp服务器上对应的数据是否存在
        version = os.path.basename(remotepath)
        self.ftp.cwd('train-data')
        data_list = self.ftp.nlst()
        if version not in data_list:
            code = -1
            msg = 'ftp data %s not found' %version
            return code, msg

        # 下载前检查本地目标路径中是否已经存在数据
        local_train_data = os.path.join(localpath,version)
        if os.path.isdir(local_train_data):
            code = -1
            msg = 'local data %s already exist' %version
            return code, msg

        cmd1 = 'wget -nH -r -l inf -P %s --ftp-user=%s --ftp-password=%s ftp://192.168.109.133/%s' %(localpath, user, password, remotepath)
        os.system(cmd1)
        # 下载到本地后要把目标数据从上层目录中挪出来，之后再删除上层目录
        cmd2 = 'mv %s/train-data/%s %s/%s' %(localpath, version, localpath, version)
        os.system(cmd2)
        cmd3 = 'rmdir %s/train-data' %localpath
        os.system(cmd3)

        # 检查数据是否下载成功
        if os.path.isdir(local_train_data):
            return 0, 'OK'
        else:
            code = -1
            msg = 'download file failed'
            return code, msg

    def upload_train_data(self, localpath, remotepath):
        '''
        向ftp上传压缩包格式的训练结果
        本地训练结果:/home/work/workdir/model-data/V0.1/output/release/release.zip 
        ftp训练结果路径: model-data/V0.1/output
        :param localpath：要上传的训练结果的路径
        :param remotepath: 要上传到ftp上的路径
        :return:code,msg
        '''
        # 上传之前先检查要上传的数据是否存在
        if not os.path.isdir(localpath):
            code = -1
            msg = 'local data not exist'
            return code, msg

        # 上传前检查ftp上对应路径是否存在，如果不存在，需要先逐层建立目录
        self.ftp.cwd('/home/user')# 正式服务器上登入ftp后的默认路径为'/',需要修改？
        if 'model-data' not in self.ftp.nlst():
            self.ftp.mkd('model-data')
        self.ftp.cwd('model-data')
        if 'V0.1' not in self.ftp.nlst():
            self.ftp.mkd('V0.1')
        self.ftp.cwd('V0.1')
        if 'output' not in self.ftp.nlst():
            self.ftp.mkd('output')
        self.ftp.cwd('output')

        code, msg = self.create_zipfile(localpath)
        if code == -1:
            return code, msg
        zipfile = os.path.join(localpath, 'release.zip')
        upload_file = open(zipfile,'rb')
        self.ftp.storbinary('STOR %s/release.zip' %remotepath, upload_file)
        upload_file.close()

        # 检查文件是否上传成功
        self.ftp.cwd('/home/user/model-data/V0.1/output')# 需要具体修改？
        if 'release.zip' not in self.ftp.nlst():
            code = -1
            msg = 'upload data failed'
            return code, msg
        else:
            return 0, 'OK'

    def upload_evaluation_data(self, localpath, remotepath):
        '''
        向ftp上传压缩包格式的评估结果
        本地评估结果:/home/work/workdir/assessment-data/V0.1/2/output/release/release.zip
        ftp评估结果路径：assessment-data/V0.1/2/output 
        :param localpath：要上传的评估结果的路径
        :param remotepath: 要上传到ftp上的路径
        :return:code,msg
        '''
        # 上传之前先检查要上传的数据是否存在
        if not os.path.isdir(localpath):
            code = -1
            msg = 'local data not exist'
            return code, msg

        # 上传前检查ftp上对应路径是否存在，如果不存在，需要先逐层建立目录
        self.ftp.cwd('/home/user')# 正式服务器上登入ftp后的默认路径为'/',需要修改？
        if 'assessment-data' not in self.ftp.nlst():
            self.ftp.mkd('assessment-data')
        self.ftp.cwd('assessment-data')
        if 'V0.1' not in self.ftp.nlst():
            self.ftp.mkd('V0.1')
        self.ftp.cwd('V0.1')
        if '2' not in self.ftp.nlst():
            self.ftp.mkd('2')
        self.ftp.cwd('2')
        if 'output' not in self.ftp.nlst():
            self.ftp.mkd('output')
        self.ftp.cwd('output')

        code, msg = self.create_zipfile(localpath)
        if code == -1:
            return code, msg
        zipfile = os.path.join(localpath, 'release.zip')
        upload_file = open(zipfile,'rb')
        self.ftp.storbinary('STOR %s/release.zip' %remotepath, upload_file)
        upload_file.close()

        # 检查文件是否上传成功
        self.ftp.cwd('/home/user/assessment-data/V0.1/2/output')# 需要具体修改？
        if 'release.zip' not in self.ftp.nlst():
            code = -1
            msg = 'upload data failed'
            return code, msg
        else:
            return 0, 'OK'


if __name__ == '__main__':
    host = '192.168.109.133'
    port = 21
    user = 'user'
    password = '123456'

    myftp = MyFtp(host, port, user, password)

    download_localpath = '/root/download'
    download_remotepath = 'train-data/V0.1'
    #code, msg = myftp.download(user, password, download_localpath, download_remotepath)
    #print('!!!!!',code,msg)
    
    upload_train_localpath = '/root/workdir/model-data/V0.2/output/release'
    upload_train_remotepath = '/home/user/model-data/V0.2/output/'

    upload_evaluation_localpath = '/root/workdir/assessment-data/V0.2/2/output/release'
    upload_evaluation_remotepath = '/home/user/assessment-data/V0.2/2/output/'

    code, msg = myftp.upload_train_data(upload_train_localpath, upload_train_remotepath)
    print('!!!!!',code,msg)
    #code, msg = myftp.upload_evaluation_data(upload_evaluation_localpath, upload_evaluation_remotepath)
    #print('!!!!!',code,msg)



