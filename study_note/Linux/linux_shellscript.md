# 主要记录关于linux脚本的相关内容：

* 注意：linux的/bin目录中有多个shell，其中默认shell是/bin/bash
* 'sh a.sh'或'bash a.sh'执行脚本 

> http://www.runoob.com/linux/linux-shell.html

* 注意：linux的.sh脚本如果下载到windows环境打开查看后再上传到linux环境，
* 执行会报错： $'\r': command not found 
* 实际在windows环境打开后脚本的编码格式会改变，因此不要打开

> https://blog.csdn.net/qq_33341037/article/details/79718588


## 常见符号含义：
```
-   减号在管道命令中可以代替stdin和stdout;减号用在'变量名={变量名-default}'中设置变量的默认值,另外也代表刚才的目录
.   小数点开头的文件代表是隐藏文件；小数点代表当前的目录，也可以用./表示
..  两个小数点代表上一层目录，也可以用../来表示
&   后台运行命令，最大的好处是无需等待命令执行结束，就可以在同一命令行下继续输入命令
=   变量名=值，为变量赋值。注意"="左右紧跟变量名和值，中间不要有空格,例如：myname=xyf
$   变量值替换，"$变量名"替换为shell变量的"值"，为避免在文本连接时混淆，请使用${变量名}，另外$是一般身份用户的提示符
>   输出重定向，prog > file 将标准输出重定向到文件（覆盖原文件内容）
>>  输出重定向，prog >> file 将标准输出追加到文件
<   输入重定向，prog < file 从文件file中获取标准输入
|   管道命令，例：p1 | p2 将p1的标准输出作为p2的标准输入
()  在子shell中执行命令，或用于运算，或用于命令替换（$（command））
{}  在当前shell中执行命令，或用在变量替换的界定范围(例如上面的${变量名}用法)
$?  命令回传码；如果前一个命令执行成功，会在Linux下返回一个命令回传码$?=0，执行错误，则$?为非零的其他值
&&  前一个命令执行成功后，才继续执行下一个命令。例：p1 && p2 ，若p1执行成功后，才执行p2，反之，不执行p2
||  前一个命令执行失败后，才继续执行下一个命令。例：p1 || p2 ，若p1执行成功后，不执行p2，反之，才执行p2
;   命令分隔符，在前一个命令结束时，忽略其返回值，继续执行下一个命令
!   逻辑运算中的非(not)，另外代表执行历史记录（history列表）中的命令，如!1
\   转义紧接着的下一个字符，例如特殊符号：$,\,!,空格,[Enter]等变成普通字符，也可以在命令太长时用来换行
~   当前登陆用户的主目录
#   后边跟关键字，表示从左边(头部)开始删除符合关键字的最短数据部分，另外代表root用户的提示符
##  后边跟关键字，表示从左边(头部)开始删除符合关键字的最长数据部分
%   后边跟关键字，表示从右边(尾部)开始删除符合关键字的最短数据部分
%%  后边跟关键字，表示从右边(尾部)开始删除符合关键字的最长数据部分
/   后边接旧关键字/新关键字，表示替换符合旧关键字的第一个数据部分
//  后边接旧关键字/新关键字，表示替换符合旧关键字的所有数据部分
"   双引号中包含的特殊字符如$等还可以保持原有的功能，例如："$HOME" --> /root
'   单引号中包含的特殊字符如$等会被转换为普通的字符  例如：'$HOME' --> $HOME
`   反单引号(数字1左边的键)中可以包含命令，例如:mycmd=`ls -al`,等同于mycmd=$(ls -al)，注意：在一串命令中反单引号中的部分会被优先执行
```


## 通配符的符号含义：
```
*   代表0到无穷多个任意字符
?   代表一定有一个任意字符
[]  代表一定有一个在中括号内的字符，例如[abcd]代表一定有a,b,c,d中任意一个字符
[-] 有减号在中括号内时代表在编码顺序的所有字符，例如[1-9]代表1到9之间的所有数字
[^] 中括号内第一个字符为指数符号代表反向选择，例如[^abc]表示一定有一个除了a,b,c以外的字符
详见module_re中的正则表达式
```


## 变量的设置规则：
```
自定义变量小写表示，系统变量大写表示，如：PATH,HOME,MALL,SHELL
'echo'命令用来显示变量，但要用$变量名或${变量名}的格式，例如:'echo $PATH'
变量名可以包含英文字母，下划线_，数字，但不能以数字开头
变量值中若有空格可以使用双引号或单引号包起来，还可以保持原有的内容格式
可以用变量设置经常访问的目录，例如：mydir="/root/a/b/c";  cd $mydir;   ls -al $mydir;
变量值默认为字符串类型，即sum=1+2，sum是一个字符串而不是数字
'变量名={变量名-default}'设置变量的默认值，如果变量未被提前设置，则给予default的值
'变量名={变量名:-default}'加上冒号后，如果变量未被提前设置或被设置为空字符串，均会被给予default的值
```


## 变量内容的修改：
```
1.变量值中增加新内容
变量名="$变量名或${变量名}"新内容   ,新内容中如有空格特殊字符等也有用引号包起来
2.变量值中删除内容，注意灵活运用通配符
变量名=${变量名#关键字},例如：name=abcbcbcdef-->name=${name#a*c}-->bcbcdef
变量名=${变量名##关键字},例如：name=abcbcbcdef-->name=${name##a*c}-->def
变量名=${变量名%关键字},例如：name=efgabcabbcabbbc-->name=${name%a*c}-->efgabcabbc
变量名=${变量名%%关键字},例如：name=efgabcabbcabbbc-->name=${name%%a*c}-->efg
3.变量值中替换内容
变量名=${变量名/旧关键字/新关键字},例如：name=efgabcabcabc-->name=${name/abc/x}-->efgxabcabc
变量名=${变量名//旧关键字/新关键字},例如：name=efgabcabcabc-->name=${name//abc/x}-->efgxxx
```


## 数据流重定向(redirect)：
```
数据流重定向就是将某个命令执行后应该出现在屏幕上的数据传输到其他地方去
即把standard output和standard error output分别传送到其他文件或设备中
或者把原本需要键盘输入的数据用文件内容来输入
标准输入(stdin)：代码为0，使用<或<< 
标准输出(stdout): 代码为1，使用>或>>
标准错误输出(stderr): 代码为2，使用2>或2>>
'cat > file1 < file2'从已存在的file2文件中读取数据并写入新建的file1文件
'cat > file1'表示新建一个file1文件并等待输入数据
'cat > file1 << "keyword"'当从输入数据为预置的keyword时，就结束此次输入，相当于ctrl+D的效果，但可以在脚本中实现自动处理
'命令 > filename'把命令的正确结果输入到filename文件中，如果filename不存在就新建一个，若存在则原文件内容会被覆盖
'命令 >> filename'把命令的正确结果输入到filename文件中，如果filename不存在就新建一个，若存在则新内容追加在原文件内容后边
'命令 2> filename'把命令的错误结果输入到filename文件中，如果filename不存在就新建一个，若存在则原文件内容会被覆盖
'命令 2>> filename'把命令的错误结果输入到filename文件中，如果filename不存在就新建一个，若存在则新内容追加在原文件内容后边
'命令 > file1 2> file2'把命令的正确和错误结果分别输入到file1和file2中
'命令 > filename 2>&1'或'命令 &> filename'把命令的正确和错误结果都输入到filename文件中
'命令 2> /dev/null'把命令的错误信息都丢弃，/dev/null相当于垃圾桶，可以吃掉任何导向这个设备的信息
```


## 关于命令的执行顺序：
```
决定命令执行顺序的特殊符号：  ;  &&  ||
'ls -l ./a || mkdir ./a && mkdir ./a/b && mkdir ./a/b/c'如果a目录存在就列出内容，如果不存在就建立./a/b/c目录
符号的使用顺序一般是:'command1 && command2 || command3'
```


---


## 脚本示例：清空磁盘
```
str="/home/disk1"
for app_path in `ls`;
do
    #[[ $app_path =~ "*qucloud*" ]]
    #echo $?
    echo $app_path
    rm -f $app_path/strategy/bin/core.*
    echo $app_path | grep "qucloud"
    if [ $? -eq 0 ]
    then
        r=${app_path##*qucloud-}
        m=`echo $r|awk -F '-' '{print $1}'`
        echo $m
        if [ ! -d "$str/sofacloud_unit_log/$m" ];
        then
         echo $str
          mkdir -p $str/sofacloud_unit_log/$m
        fi
         mv $app_path/strategy/log/* $str/sofacloud_unit_log/$m
    fi
done
```