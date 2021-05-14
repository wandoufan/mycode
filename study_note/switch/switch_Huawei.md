# 华为交换机

## 基本信息


## 交换机的命令视图(假设交换机名为huawei)
1. 用户视图
登入交换机后得到的就是用户视图，该视图可以查看交换机运行状态和基本信息  
用户视图的提示符为：```<huawei>```

2. 系统视图
从用户视图进入的下一级视图，该视图可以配置系统参数  
系统视图的提示符为：```[huawei]```

3. 以太网端口视图
从系统视图进入的下一级视图，该视图可以配置某个以太网端口参数  
以太网端口视图的提示符为：```[Huawei-GigabitEthernet0/0/1]```

4. 协议视图
从系统视图进入的下一级视图，该视图用来配置某个协议  
协议视图的提示符为：```[Huawei-ospf-1]```

5. vlan接口视图
从系统视图进入的下一级视图，该视图用来配置vlan接口参数  
vlan接口视图的提示符为：```[Huawei-vlan10]```


## 视图切换命令
* 进入系统视图
```
<Huawei>system-view 或者 sys 或者 system
[Huawei]
```
* 进入以太网端口视图
```
interface 接口类型+接口编号
[Huawei]interface Ethernet0/0/1
[Huawei-Ethernet0/0/1]
```
* 进入ospf协议视图
```
[Huawei]ospf
[Huawei-ospf-1]
```
* 进入vlan接口视图
```
[Huawei]vlan 10
[Huawei-vlan10]
```
* 返回上一级视图
```
quit
```
* 直接返回到用户视图
```
return 或 ctrl+z
```


## 交换机系统命令
* 重启交换机
```
reboot
```
* 重置交换机配置
```
reset saved-configuration
```
* 更改交换机配置后保存
```
save
```


## 查看交换机的基本信息
* 显示当前配置
```
display current-configuration
```
* 显示已经保存配置
```
display saved-configuration
```
* 显示版本信息
```
display version
```
* 显示接口信息
```
display interfaces
```
* 显示路由信息
```
display ip route
```
* 显示vlan信息
```
display vlan
```
* 显示Mac信息
```
display mac
```
* 显示端口与vlan的对应关系
```
display port vlan
```


## 设置交换机的基本信息
* 更改主机名
```
[Huawei]sysname HW
```
* 设置口令
```
[Huawei]super password 123456
```


## 配置接口相关命令
* 关闭接口
```
[Huawei-Ethernet0/0/1]shutdown
```
* 开启接口
```
[Huawei-Ethernet0/0/1]undo shutdown
```


## 接口类型相关命令
* 配置该接口为Access类型
```
[Huawei-Ethernet0/0/1]port link-type access
```
* 配置该接口为Trunk类型
```
[Huawei-Ethernet0/0/1]port link-type trunk
```


## vlan配置相关命令
* 创建vlan 10，创建后会自动进入到vlan 10的视图中
```
[Huawei]vlan 10
[Huawei-vlan10]
```
* 同时创建vlan 10和20
```
[Huawei]vlan batch 10 20
```
* 创建10-20的vlan
```
[Huawei]vlan batch 10 to 20
```
* 把0/1端口加入到vlan 10中
```
[Huawei-vlan10]port Ethernet 0/1
```
