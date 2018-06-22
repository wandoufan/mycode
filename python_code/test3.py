import os 
import ftplib


host = '192.168.109.133'
port = 21
user = 'user'
password = '123456'

ftp = ftplib.FTP()
ftp.connect(host, port)
ftp.login(user, password)
ftp.cwd('/home/user')
ftp.mkd('/aaa/bbb/ccc')

print('！！！！！！！！！！',ftp.pwd())
print('!!!!!!!!!!!!!!!!!!!',ftp.nlst())