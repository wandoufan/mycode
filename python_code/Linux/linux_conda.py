# conda 是为python程序创建的，是目前最流行的python环境管理工具
# Conda 是开源的包管理系统和环境管理系统，可以安装软件包的多个版本和依赖，而且方便切换。
# 在不同的conda环境中的python的package和package的版本都可以不一样
# Conda 包含所有版本的 Anaconda, Anaconda Server 和 Miniconda，而且不会单独提供.
# 在Linux、OS X或者Windows平台上的命令行终端运行的conda指令都是一样的
# 注意：使用时要注意当前所在的环境，在这个环境下安装的python包在另外环境中就无法引用


# miniconda下载地址：
# https://conda.io/miniconda.html
# https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/

	
# conda常用命令:
# 命令官网：https://conda.io/docs/user-guide/tasks/manage-environments.html
# 'conda --version'或'conda -V' 查看conda版本
# 'conda info' 查看conda的详细信息
# 'conda update conda' 更新conda版本
# 'conda env list' 显示已创建所有环境，*标注的为当前所在环境
# 'conda create --name myenv' 创建新的环境，myenv为环境名字
# 'conda create --name python36 python=3.6' 创建python36环境，指定python版本为3.6
# 'source activate python36' 进入python36环境
# 'source deactivate python36' 退出python36环境
# 'conda create -n myenv package' 用一个特殊的包创建新的环境
# 'conda create -n myenv package=0.15.0' 用一个特殊版本的包创建新的环境
# 'conda create --name myclone --clone myenv' 克隆当前的环境
# 'conda remove -n myenv --all' 删除环境
# 'conda remove -name myenv package' 删除环境中的某个包
# 'conda install -n myenv package' 给指定环境安装某个包
# 'conda list' 查看当前环境中已安装包
# 'conda list -n python36' 查看指定环境的已安装包
