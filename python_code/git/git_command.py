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


# git配置文件：
# windows环境下配置文件在C:\Users\Administrator\.gitconfig文件中，可以设置git提交时的用户邮箱
# 在git bash中可以直接用命令查看'vim ~/.gitconfig'

# git相关的使用命令：
# 'git init'初始化一个仓库，把当前所在的目录变成git可以管理的仓库，并且会在目录下创建一个.git隐藏目录用来管理
# 'git add filename/dirname'把指定文件或目录添加到仓库(把修改的文件添加到暂存区),注意文件一定要放在刚才指定的仓库目录下，与commit命令一起配合使用
# 'git add file1 file2 file3'一次添加多个文件，中间用空格隔开
# 'git add -A .'一次添加所有改动过的文件(包括删除和新增文件)，注意后边有一个小数点
# 'git add .'一次添加所有新增和修改的文件，但不包括删除的文件
# 'git add -u'一次添加所有删除和修改的文件，但不包括新增的文件
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


# 连接远程代码库：
# 首次提交远程库需要设置用户名邮箱
# 'git config --global user.name myname'设置用户名
# 'git config --global user.name'查看用户名
# 'git config --global user.email myemail'设置邮箱
# 'git config --global user.email'查看邮箱
# --global参数表示本设备上的所有仓库都连接这个远程仓库
# 'git config --list'查看所有的配置列表
# 'git remote add origin git@github.com:wandoufan/git_test.git'ssh方式连接github添加远程库
# 备注：远程库/远程主机的默认名字origin(起源)
# 'git remote add origin https://github.com/wandoufan/git_test.git'https方式连接远程库
# 备注：https方式需要每次输入账户密码且速度较慢，推荐使用ssh方式
# 'git remote rm origin'删除远程库
# 'git remote'查看远程库名字，-v参数查看详细信息


# ssh方式登录权限问题相关：
# 使用ssh方式连接远程库之前需要在本地生成公钥文件并在github上登记
# 'cd ~/.ssh'打开C:\Users\Administrator\.ssh路径
# 'ssh-keygen'在上面的路径中生成公钥文件id_rsa.pub和秘钥文件id_rsa，passphrase口令可以设置为空
# 拷贝公钥文件的内容，打开https://github.com/settings/profile，在SSH key那栏选择New SSH Key，并将复制内容拷贝到其中
# https://blog.csdn.net/mengmengz07/article/details/70157018
# 备注：ssh passphrase设置为空


# 提交本地代码到远程库：
# 除了本地仓库还可以把本地的代码提交到远程仓库，例如github上
# push命令可以使远程的代码和本地的代码保持一致
# 'git push -u origin master'把当前master分支的所有内容推送到远程库上，推送前需要add和commit
# -u参数不但会把本地master分支推送到远程上新建的master分支，还会把本地和远程的master分支关联起来，方便后边再推送/拉取
# 'git push origin master'建立连接后可以不加-u参数就直接推送
# 'git push --set-upstream origin branch_new'对于新建立的分支推送之前要先在远程库上建立对应的分支
# 注意：使用git push时如果远程库的版本比本地库更新，即远程节点比本地节点在时间线上更远
# 那么就不能push到远程库，必须先把远程库上更新的版本pull到本地，然后合并完文件(可能需要手动处理冲突)后再push


# 从远程库更新库到本地：
# 适用于本地有库时，从远程库抓取更新版本的分支并与本地的分支合并
# git pull = git fetch + git merge(拉取到本地 + 代码合并)
# 'git pull <远程主机名> <远程分支名>:<本地分支名>'从远程抓取分支并与当前工作目录中的分支合并
# 'git pull origin master'把远程master分支与当前分支合并，本地分支名可以省略
# 'git pull origin master --allow-unrelated-histories'合并两个不同的项目(否则可能会报错：refusing to merge unrelated histories)
# 注意：远程的代码可能和本地的代码会修改同一个地方，此时pull到本地就会产生冲突，git客户端会提示冲突的文件，需要进入文件手动选择修改
# 注意：使用git pull时只有远程库的版本要比本地库更新，即远程节点比本地节点在时间线上更远，远程库才可以覆盖本地，否则不会修改任何文件


# 从远程库克隆库到本地：
# 适用于本地没有库时，直接从网上下载一个库到本地
# 'git clone git@github.com:wandoufan/git_test.git'ssh方式从远程库上克隆库到当前工作目录，会在工作目录里新建一个git_test文件夹
# 'git clone https://github.com/wandoufan/git_test.git'https方式克隆库到当前工作目录
# 'git clone -b branch_name git@github.com:wandoufan/git_test.git'克隆指定分支到本地，-b参数指定分支


# 分支相关的命令：
# 分支的功能是在一个节点把代码一分为二，例如需要对一个正在使用的代码A开发新功能，就可以创建一个属于自己的新分支
# 其他人还可以继续使用旧分支正常工作，在新分支上开发新功能，等功能开发完毕就合并回原来旧分支上
# 注意：不同的分支中文件内容不同，即切换到不同分支后，打开文件夹显示的内容也不同
# 'git branch branch_name'创建新的分支，即HEAD改为指向新的分支dev，新的分支dev再指向当前的最新提交节点
# 'git checkout branch_name'切换分支
# 'git checkout -b branch_name'创建+切换分支
# 'git merge branch_name'合并某分支到当前分支
# 注意：如果要merge的两个分支只有一个修改了内容，就可以快速合并；如果两个都修改了内容，则可能会提示冲突，需要手动修改冲突的地方
# 'git branch -d branch_name'删除分支
# 'git branch'查看本地分支，当前分支前面会标一个*号
# 'git branch -r'查看远程分支
# 'git branch -a'查看所有分支(包括本地和远程)
# 'git log --graph'查看分支合并图
# 注意：一般master分支仅用来发布稳定的版本，平时不在上面工作，所有人工作都在不稳定的dev分支上
# 每个人都从dev分支上再分出自己的分支各自工作，等完成一个版本后，统一从dev分支上合并到master分支上进行发布


# 创建git标签：
# 发布一个新版本时通常在版本库里打上一个标签tag来做标记，
# 一般commit号也可以做唯一标记，但'6704497a1...'这种形式不方便使用，标签的内容可以自定义的更形象
# 标签也是通过指向commit来实现的，因此tag和某个commit是绑定在一起的，创建删除标签都可以很快完成
# 'git tag tag_name' 给当前的commit打上标签
# 'git tag tag_name commit_id' 给之前指定的某次提交打上标签
# 'git tag -a tag_name -m"tag_message" commit_id' 打标签使可以加上标签说明,-a为标签,-m为说明
# 'git tag' 查看所有的标签，注意：标签不是按时间顺序列出，而是按字母顺利排列
# 'git show tag_name' 查看指定标签的详细信息
# 'git tag -d tag_name' 删除本地的指定标签
# 'git push origin tag_name' 推送指定标签到远程
# 'git push origin --tags' 一次推送所有未被推送过的标签到远程
# 'git push origin :refs/tags/tag_name' 删除远程的标签
# 注意：标签总是和某个commit绑定，如果commit出现在两个分支上，那么在两个分支上都可以看到标签


# -----------------------------------------------------------------------------------------
# 多人维护同一份代码时：
# 本地1             远程              本地2
#  A                  A                 A
#  B                  B                 B
#  C                  C                 C
# ---------------------------------------------------------------------------------
# 本地2修改后先向远程push，会给2创建一个新的分支，在远程的新分支上A文件就会被删除
#              原分支 | 新分支
#  A                A |           
#  B1               B | B2                B2
#  C                C | C     <--push     C
#                     | D                 D   
# 此时本地1就无法直接向远程新分支push，只能先pull新分支到本地，手动解决完冲突之后再push上去
#--------------------------------------------------------------------------------------
