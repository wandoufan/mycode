# MTU

## 基本概念
最大传输单元（MTU）是Maximum Transmission Unit的缩写
意思是网络上传送的最大数据包，MTU的单位是字节
win7 和 win10 默认的MTU值就是1500
在默认情况下，可以互相发送合法值(65500)以内的所有数据包
备注：MTU值和数据包的大小并不一致，MTU值并不是65500，原因不清楚


## 相关命令
1. 查看MTU值
```
netsh interface ipv4 show subinterfaces
```
2. 修改MTU值
```
netsh interface ipv4 set subinterface "本地连接" mtu=1500 store=persistent
```
备注：实际测试发现，win10系统下，MTU值已经改为2000了，命令查看MTU值也是2000，但在网络连接那里显示的最大传输单元还是1500


## 遇到了问题
win7和win10电脑之间，只有data <= 1472或1476时可以发送过去
解决：把电脑的MTU值都设置1500就可以发送65500的数据包了
备注：MTU值一定要设置为1500，如果设置为比1500更大的值，比如2000，反而变成了只能发送大小1476以下的数据包