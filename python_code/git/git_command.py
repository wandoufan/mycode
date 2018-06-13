# git的基本概念：
# git是分布式的代码管理工具，svn是集中式的
# git是基于Linux的，所以可以直接在git bash中运行linux的命令
# repository 是git的资源库/版本库/仓库，这个目录里面的所有文件都可以被Git管理起来
# 每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”
# 版本控制系统只能追踪文本文件的详细改动，图片视频等二进制文件无法追踪
# git和其他版本控制系统如SVN的区别之一就是有暂存区
# 创建git版本库时，git自动创建出第一个分支，即master分支
# 第一次修改->git add->第二次修改->git commit，则第二次修改不会被提交，除非第一次修改->git add->第二次修改->git add->git commit
# 即每次修改都要往暂存区添加一次，否则不会被提交


# git相关的名词概念：
# 工作区(working directory)-电脑中指定的存放代码的目录就是一个工作区
# 资源库/版本库/仓库(repository)-工作区有一个.git隐藏目录的就是git的版本库，存放了暂存区,master分支和HEAD指针等重要内容
# 暂存区(stage/index)-用来临时存放要提交的文件，最后再由暂存区一次性把所有内容提交到分支
# 分支(branch)-分支就是每次提交组成的时间线，HEAD指向分支例如master,分支再指向当前最新一次的提交


# git相关的使用命令
# 'git init'初始化一个仓库，把当前所在的目录变成git可以管理的仓库，并且会在目录下创建一个.git隐藏目录用来管理
# 'git add filename'把指定文件添加到仓库(把修改的文件添加到暂存区),注意文件一定要放在刚才指定的仓库目录下，与下面的命令一起配合使用
# 'git commit -m"message"'把文件提交到仓库(把暂存区的所有文件提交到当前分支)，添加文件可以多次，添加完之后提交一次就行
# 'git status'显示仓库当前的状态
# 'git diff filname'查看文件被修改的内容，比较当前目录的文件与之前提交到仓库的版本的不同之处
# 'git log'查看每次提交的历史记录和每次提交的说明，显示顺序由近到远
# 'git reset'命令用来回退版本，在git中用HEAD表示当前版本，上一个版本就是HEAD^,上上个版本就是HEAD^^,上第一百个版本可以写成HEAD~100
# 'git reset --hard HEAD^'回退到上一个版本
# 'git reset --hard ID'回退到指定ID对于的版本，每个版本都有一个唯一的ID，ID只需要写出前几位即可
# 'git reflog'查看所有版本的历史记录和版本回退的历史记录，包括每个版本的ID
# 'git checkout -- filename'把文件在工作区的修改全部撤销，例如改乱了文件时放弃所有修改，包含两种情况：
# 1.文件被修改后还没有被放到暂存区，撤销修改后就回到版本库一模一样的状态
# 2.文件被添加到暂存区之后又做了修改，撤销修改就回到刚添加暂存区的状态
# 'git checkout -- filename'把在工作区中删除或修改的文件从版本库里恢复出来
# 'git reset HEAD filename'把已经添加到暂存区的文件回退回去，相当于'git add'的逆操作
# 'git rm filename'删除资源库里的文件，执行完后还要用'git commit'提交


# 拷贝本地库到远程库：
# 除了本地仓库还可以把本地的代码提交到远程仓库，例如github上
# 'git config --global user.name myname'设置用户名
# 'git config --global user.name'查看用户名
# 'git config --global user.email myemail'设置邮箱
# 'git config --global user.email'查看邮箱
# --global参数表示本设备上的所有仓库都连接这个远程仓库
# 'git config --list'查看所有的配置列表
# 'git remote add origin git@github.com:wandoufan/git_test.git'ssh方式连接github添加远程库，远程库的默认名字origin(起源)
# 'git remote add origin https://github.com/wandoufan/git_test.git'https方式连接远程库
# 备注：https方式需要每次输入账户密码且速度较慢，推荐使用ssh方式
# 'git remote rm origin'删除远程库
# 'git remote'查看远程库名字，-v参数查看详细信息
# 'git push -u origin master'把当前master分支的所有内容推送到远程库上，推送前需要add和commit
# -u参数不但会把本地master分支推送到远程上新建的master分支，还会把本地和远程的master分支关联起来，方便后边再推送/拉取
# 'git push origin master'建立连接后可以不加-u参数就直接推送


# ssh方式登录权限问题相关：
# 使用ssh方式连接远程库之前需要在本地生成公钥文件并在github上登记
# 'cd ~/.ssh'打开C:\Users\Administrator\.ssh路径
# 'ssh-keygen'在上面的路径中生成公钥文件id_rsa.pub和秘钥文件id_rsa，passphrase口令可以设置为空
# 拷贝公钥文件的内容，打开https://github.com/settings/profile，在SSH key那栏选择New SSH Key，并将复制内容拷贝到其中
# https://blog.csdn.net/mengmengz07/article/details/70157018
# 备注：ssh passphrase设置为空


# 从远程库克隆库到本地：
# 适用于本地没有库时，直接从网上下载一个库到本地
# 'git clone git@github.com:wandoufan/git_test.git'ssh方式从远程库上克隆库到当前工作目录，会在工作目录里新建一个git_test文件夹
# 'git clone https://github.com/wandoufan/git_test.git'https方式克隆库到当前工作目录
# 'git clone -b branch_name git@github.com:wandoufan/git_test.git'克隆指定分支到本地，-b参数指定分支


# 从远程库更新库到本地：
# 适用于本地有库时，从远程库抓取更新版本的分支并与本地的分支合并
# git pull = git fetch + git merge
# 'git pull'从远程抓取分支并与当前工作目录中的分支合并
# 远程的代码可能和本地的代码会修改同一个地方，此时就会产生冲突，git客户端会提示冲突的文件，需要进入文件手动选择


# 本地1             远程              本地2
#  A                  A                 A
#  B                  B                 B
#  C                  C                 C
#--------------------------------------------
#  本地2修改后先向远程commit
#  A                             
#  B1                 B2                B2
#  C                  C     <--push     C
#                     D                 D   
#--------------------------------------------
# 此时本地1就无法向远程commit，只能先pull到本地，手动解决完冲突之后再push上去
# B(手动解决冲突)    B2                B2
# C    <--pull       C                 C
# D                  D                 D   
# -------------------------------------------


# 分支相关的命令：
# 'git branch branch_name'创建新的分支，即HEAD改为指向新的分支，新的分支再指向当前的最新提交
# 'git checkout branch_name'切换分支
# 'git checkout -b branch_name'创建+切换分支
# 'git merge branch_name'合并某分支到当前分支
# 'git branch -d branch_name'删除分支
# 'git branch'查看当前分支，-r参数查看远程分支，-a参数查看所有分支


# 创建git标签：

# 怎么查看每个分支里的内容？本地分支和网站上的关系？