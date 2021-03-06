# pip

## 简介
pip是用来安装python包的一款工具  

## pip的安装
* 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
* 'python get-pip.py'
在linux中还可以通过下载安装包的方式来安装  
```
git clone https://github.com/liu946/goo.git
cd goo
(sudo) ./install.sh
```

## pip本身的更新
On Linux or macOS:  
* 'pip install -U pip'
On Windows:  
* 'python -m pip install -U pip'

## pip常用命令
备注：以下命令在windows和Linux平台下都可以使用  
* 'pip install package' 安装指定的python包
* 'pip uninstall package' 卸载指定的python包
* 'pip show package' 查看指定python包的详细信息
* 'pip list' 查看当前环境中的python包列表
注意：查看到的都是安装的第三方包，不包含python内置的库  
* 'pip list --outdated'或'pip list -o'查看可以进行更新的包

## pip一次安装多个包
把项目需要的依赖包都写入一个requirements.txt的文本中，然后一次性安装  
* 'pip install -r C:\requirements.txt'
requirements.txt文本中格式为package_name==version  
```
cffi==1.12.3
gevent==1.4.0
greenlet==0.4.15
pycparser==2.19
six==1.12.0
websocket==0.2.1
websocket-client==0.56.0
```

## pip安装超时
安装包时可能存在网络状况不好导致time out，可以手动延长超时时间  
* 'pip --default-timeout=100 install pandas'