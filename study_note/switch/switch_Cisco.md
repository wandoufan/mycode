# 思科交换机命令

## 基本信息
思科交换机的品牌为Catalyst，产品名一般为"Catalyst NN XX [-C] [-M] [-A/-EN]"  


## 交换机的命令模式(假设交换机名为switch)
1. 用户模式
登入交换机后得到的就是用户模式，该模式可以简单的查看交换机的软硬件版本信息，并对其就行简单的测试  
用户模式的提示符为：```switch>```

2. 特权模式
从用户模式进入的下一级模式，该模式下可以对交换机的配置文件进行管理，查看交换机的配置信息，进行网络测试和调试等  
特权模式提示符为：```switch#```

3. 全局配置模式
从特权模式进入的下一级模式，该模式下可以配置交换机的全局性参数（交换机名称、登陆密码等）  
全局配置模式的提示符为：```switch(config)#```

4. 端口(接口)模式
从全局配置模式进入的下一级模式，该模式可以进行对指定的某个交换机端口进行配置  
备注：在进入该模式的命令中就要写明要进入的具体端口  
端口模式的提示符：```switch(config-if)```

5. Line配置模式
从全局配置模式进入的下一级模式，该模式主要用于对虚拟终端（vty）和控制台端口进行配置，其配置主要是设置虚拟终端和控制台的用户级登录密码  
备注：可以设置交换机console口的密码  
Line配置模式的提示符为：```switch(config-line)#```

6. vlan数据库配置模式
从特权模式进入的下一级模式，该模式下可以实现对vlan的创建、修改或删除等配置操作  
vlan数据配置模式的提示符为：```switch(vlan)#```


## 模式切换命令
* 进入特权模式
```
enable
```
* 进入全局配置模式
```
config terminal
```
* 进入到交换机的F0/1接口
```
interface fastethernet 0/1
```
* 进入Line配置模式
```
line vty 或 line console
```
* 进入vlan数据库配置模式
```
vlan database
```
* 退回到上一级的操作模式
```
exit
```
* 直接退回到特权模式
```
end
```


## 交换机系统命令
* 重启交换机
```
switch#reload
```
* 保存配置到NVRAM中(需要拷贝配置)
```
switch#copy running-config startup-config
switch#wr
```


## 查看交换机的基本信息
* 查看RAM中的临时配置
```
switch#show running-config
```
* 查看NVRAM中的永久配置
```
switch#show startup-config
```
* 查看Mac地址表
```
switch#show mac-adress-table
```
* 查看端口信息
```
switch#show interface
```
* 查看路由表
```
switch#show ip route
```
* 查看CPU状态
```
switch#show processes
```
* 查看版本信息
```
switch#show version
```
* 查看vlan信息
```
switch#show vlan brief
```


## 设置交换机的基本信息
* 更改主机名
```
Switch(config)#hostname Cisco
```


## 端口配置相关命令
* 将当前端口加入到vlan 10中
```
switch(config-if)#switchport access vlan 2
```
* 允许当前端口(trunk口)通过vlan 10和vlan 20
```
switch(config-if)#switchport trunk allowed vlan 10, 20
```


## vlan配置相关命令
* 创建vlan 10
```
switch(vlan)#vlan 10
```
* 删除vlan 10
```
switch(vlan)#no vlan 10
```
* 进入vlan 10
```
switch(config)#interface vlan 10
```








