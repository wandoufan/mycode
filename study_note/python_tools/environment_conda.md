# conda

## 简介
conda是开源的包管理工具和环境管理工具，可以创建多个环境，在环境之间方便实现切换  
在不同的conda环境中的python的package和package的版本都可以不一样  
conda分为Anaconda和miniconda  
1. Anaconda
Anaconda是各种包的集合，包含某个版本的python和众多的conda包，占用的空间很大(约460M)  
备注：如果是进行数据计算或机器学习，建议使用Anaconda  
下载：https://www.anaconda.com/products/individual
2. miniconda
miniconda是精简版，只包含python和最基本的conda包，占用的空间比较小(约50M)  
下载：https://docs.conda.io/en/latest/miniconda.html


## conda和pip的对比
二者都是包管理器，可以实现包的安装、更新、卸载，但二者还有很多不同点  
1. 支持的语言
pip只能用来安装python的包，不支持python语言以外的依赖项  
conda虽然大部分包也都是python的，但还支持一些其他语言，如cuda这种C++写的包  
2. 安装的包
pip安装的是python wheel或者源代码的包，需要有编译器的支持，系统中没有编译器时可能会安装失败  
conda安装的是已经编译好的二进制包，不需要编译器，但conda安装的包一般比较大，可能几百M甚至1G多  
3. 管理环境
pip只能实现包的管理功能，如果想要实现环境管理，还需要额外安装virtualenv  
conda带有管理环境的功能，可以轻松管理多个版本的python  
4. python解释器
pip必须在安装好python解释器之后才能使用  
conda不需要实现安装python解释器，甚至可以用conda来下载安装python解释器  
5. 依赖检查
pip依赖检查不严格  
conda具有严格的依赖检查  
6. 包资源
pip的包资源为PyPI，Python的包会被优先发布到PyPI上  
conda的包资源为Anaconda，包数量远少于PyPI  
7. 总结
建议优先用conda来管理，如果conda没有再使用pip安装  
如果使用GPU进行机器学习，用到了CUDA、TensorFlow、PyTorch等库，建议使用conda  
备注：pip的包跟conda不完全重叠，有些包只能通过其中一个装  


## Windows下安装conda


## 国内的conda镜像


-------------------- conda常用命令 -----------------------
备注：在Linux或者Windows平台上的命令行终端运行的conda指令都是一样的  
命令官网： https://conda.io/docs/user-guide/tasks/manage-environments.html

## yml文件
1. 把当前环境导出为一个yml文件
```
conda env export > myenv.yml
```
1. 导入yml文件来创建conda环境
```
conda env create -f environment.yml
```
2. yml文件示例
备注：yml文件不需要用命令特意导出，创建环境之后就出现在环境目录中  
```
name: stats2
channels:
  - javascript
dependencies:
  - python=3.6   # or 2.7
  - bokeh=0.9.2
  - numpy=1.9.*
  - nodejs=0.10.*
  - flask
  - pip:
    - Flask-Testing
```


## 关于conda环境的说明
1. 安装conda后默认会有一个名为base的环境，但一般不用这个环境，而是额外创建环境
2. 'conda env list'可以看到所有conda环境及其目录位置  


## 查看conda环境信息
1. 查看所有的conda环境
备注：conda会创建一个默认的base环境  
```
conda env list
```
2. 查看conda版本
```
conda -V
或
conda --version
```
3. 查看conda的详细信息，包括conda版本，Python版本等等
```
conda info
```


## 用命令创建conda环境
1. 创建一个环境，并指定环境名
```
conda create --name myenv
```
2. 创建一个环境，并指定python版本
注意：上面命令指定python版本不仅是往conda环境中添加python，而是直接利用conda安装Python程序
```
conda create -n myenv python=3.6
```
3. 用特定的包创建一个环境
```
conda create -n myenv scipy
或
conda create -n myenv python
conda install -n myenv scipy
```
4. 用特定的包的指定版本创建一个环境
```
conda create -n myenv scipy=0.15.0
或
conda create -n myenv python
conda install -n myenv scipy=0.15.0
```
5. 用特定版本的Python和多个包创建一个环境
```
conda create -n myenv python=3.6 scipy=0.15.0 astroid babel
```
6. 查看conda create的更多信息
```
conda create --help
```


## 创建conda环境时指定环境的目录位置
1. 在当前目录中创建一个子目录envs，然后在子目录中创建环境
```
conda create --prefix ./envs jupyterlab=0.35 matplotlib=3.1 numpy=1.16
```
2. 切换到指定目录的环境
```
conda activate ./envs
```
3. 创建特定目录的好处
一般情况下，环境的名字不能重复，如果环境位于不同的目录中，则环境的名字可以相同


## 更新conda环境
1. 需要更新conda环境的情况：
依赖库发布了新版本  
需要添加新的依赖库  
添加了新的依赖库，同时删除旧的依赖库  
2. 更新步骤
先更新yml文件，然后执行下面的命令  
```
conda env update --prefix ./env --file environment.yml  --prune
```
注意：加上--prune选项后，conda会删除环境中所有多余的依赖库(环境中已经存在，但yml中没有要求)  


## 复制conda环境
1. 将myenv环境复制，新环境命名为myclone
```
conda create --name myclone --clone myenv
```


## 激活(切换)conda环境
1. 切换到myenv环境
备注：切换成功之后，命令行前面会有新的环境名  
```
conda activate myenv
```


## 取消激活conda环境
1. 取消激活当前conda环境
```
conda deactivate
```


## 更新conda本身的版本
1. 更新conda本身的版本
```
conda update conda
```


## 删除conda环境
1. 删除conda环境
```
conda remove --name myenv --all
或
conda env remove --name myenv
```


## conda环境中管理包
1. 查看当前conda环境中安装的包，包的版本，以及包的来源
```
conda list
或
conda list --explicit
```
2. 查看指定conda环境中安装的包
```
conda list -n python36
```
3. 在myenv环境中安装scipy包
```
conda install --name myenv scipy
```
4. 如果安装包的时候不指定环境，会默认安装在当前环境下
```
conda install scipy
```
5. 安装包的时候指定环境
```
conda install scipy=0.15.0
```
6. 一次安装多个包
```
conda install scipy curl
```
7. 更新conda环境中包的版本
```
conda update scipy
```
8. 删除myenv环境中的scipy包
```
conda remove -n myenv scipy
```
9. 删除当前环境中的scipy包
```
conda remove scipy
```
如果用命令删除有问题，也可以尝试直接去存放包的路径中删除文件夹
```
..\envs\myenv\Lib\site-packages
```


## 管理conda的镜像源
1. 查看当前的镜像源(查看里面的channel URLs字段)
```
conda info
```
2. 添加镜像源
```
//清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
//中科大源
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
```
注意添加之后，再输入以下命令
```
conda config --set show_channel_urls yes
```
3. 删除国内的镜像源
```
conda config --remove channels
```


## 在conda环境中使用jupyter notebook
1. 安装jupyter notebook
默认会有？
2. 进入jupyter notebook
```
jupyter notebook
```
