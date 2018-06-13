# 使用字典模拟一个用户账号密码管理系统，实现不同用户的登陆注册功能
# 功能：注册，登陆，修改密码，管理员查看账号密码，管理员删除账号
# 改进：当出错时添加跳转，不用重新输入命令；使用json将运行结果保存到文件中
# 备注：账号密码都以字符串的类型存储

# 定义一个字典来存储用户的账号密码，包含一个内置的管理员账号
data_base = {'admin': str(666666)}

# 注册函数


def newuser():
    newname = str(input('please input your name:'))
    if newname in data_base:
        print('name already exist!')
    else:
        newpassword = str(input('please input your password:'))
        if len(newpassword) < 6:
            print('password not long enough！')
        else:
            data_base[newname] = newpassword
            print('newuer success!')

# 登陆函数


def login():
    name = str(input('please input your name:'))
    if name not in data_base:
        print('name not exist! ')
    else:
        password = str(input('please input your password:'))
        if data_base[name] == password:
            print('login success!')
        else:
            print('wrong password!')

# 查看函数


def show():
    adminname = str(input('please input your name:'))
    if adminname != 'admin':
        print('you do not have access!')
    else:
        adminpassword = str(input('please input your password:'))
        if data_base[adminname] != adminpassword:
            print('wrong password!')
        else:
            print('all of the accounts：', data_base.items())

# 修改密码函数


def change():
    changename = str(input('please input your name:'))
    if changename not in data_base:
        print('name not exist!')
    else:
        oldpassword = str(input('print input your password:'))
        if data_base[changename] != oldpassword:
            print('wrong password!')
        else:
            newpassword = str(input('please input your new password:'))
            againpassword = str(input('please input your new password again:'))
            if newpassword == againpassword:
                data_base[changename] = newpassword
                print('successfully change password！')
            else:
                print('adminpassword different from newpassword!')

# 删除账号函数


def delete():
    adminname = str(input('please input your name:'))
    if adminname != 'admin':
        print('you do not have access!')
    else:
        adminpassword = str(input('please input your password:'))
        if data_base[adminname] != adminpassword:
            print('wrong password!')
        else:
            deletename = str(
                input('please input the accout that you want delete:'))
            if deletename not in data_base:
                print('accout do not exist!')
            elif deletename == 'admin':
                print('you can not delete the accout of administrator!')
            else:
                del data_base[deletename]
                print('successfully delete the accout!')

# 主函数


def mainmenu():
    user_input = input('please input your command:')
    if user_input == 'newuser':
        newuser()
    elif user_input == 'login':
        login()
    elif user_input == 'show':
        show()
    elif user_input == 'change':
        change()
    elif user_input == 'delete':
        delete()
    else:
        print('illegal command!')


while True:
    mainmenu()
