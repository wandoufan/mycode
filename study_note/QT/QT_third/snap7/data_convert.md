# 向DB块读写数据时的格式转换问题

## byte数组
数据读写函数中的数据存储参数都是一个空类型指针`void *pUsrData`
在实际操作中，这个参数一般都是byte数组，原因未知
在定义数组时，数组的长度要≥数据的字节数
备注：DB块中的一个地址代表一个字节，例如，32位浮点数要使用4个地址，即4个字节
```
byte read_data[4];
byte write_data[4];
```
备注：byte并不是C或C++中自带的数据类型，但直接写在代码中并不报错


## 数据格式转换说明
1. 这个问题的本质是byte数组和某个数据类型的转换
2. 转换的时候要进行高位和低位的对调
3. 转换的时候不需要进行10进制和16进制的转换


## 数据格式转换示例
1. 读取DB块中的32位浮点数
```
//把DB块的数据读取到byte数组中
byte data_read[4] = {0};
int result = Cli_DBRead(plc_client, DBNumber, Start, 4, data_read);

//把byte数组解析为32位浮点数
byte data_parse[4];
data_parse[0] = data_read[3];
data_parse[1] = data_read[2];
data_parse[2] = data_read[1];
data_parse[3] = data_read[0];
float num;
memcpy(&num, data_parse, 4);
info.setNum(num);
ui -> textBrowser -> setText(info);
```

2. 向DB块写入32位浮点数
备注：这部分没有看太懂，但代码是有效的
```
//把浮点数解析为byte数组
byte data_write[4] = {0};
float num = static_cast<float>(ui -> doubleSpinBox -> value());
data_write[3] = *((byte*)&num + 0);
data_write[2] = *((byte*)&num + 1);
data_write[1] = *((byte*)&num + 2);
data_write[0] = *((byte*)&num + 3);

//把byte数组写入到DB块中
int result = Cli_DBWrite(plc_client, DBNumber, Start, 4, data_write);
```

3. 读取DB块中的布尔值
一般用1个地址(1个字节)来存储8个布尔变量的值
```
//把DB块的数据读取到byte数组中
byte data_read[1] = {0};
int result = Cli_DBRead(plc_client, DBNumber, Start, 1, data_read);

//数据格式解析
byte data_parse[1];
data_parse[0] = data_read[0];
bool result_bool;
result_bool = data_parse[0] & 0;//第1位
result_bool = data_parse[0] & 2;//第2位
result_bool = data_parse[0] & 4;//第3位
result_bool = data_parse[0] & 8;//第4位
result_bool = data_parse[0] & 16;//第5位
result_bool = data_parse[0] & 32;//第6位
result_bool = data_parse[0] & 64;//第7位
result_bool = data_parse[0] & 128;//第8位
```

4. 向DB块写入布尔值
备注：在仿真PLC中测试时，修改后的布尔值会很快被PLC自动改回去，看起来就像是闪烁
```
//由于不知道怎么单独写其中一位，就把整个字节读出来，更改其中一位之后再写回DB块
byte data_read[1] = {0};
byte data_write[1] = {0};
Cli_DBRead(plc_client, DBNumber, Start, 1, data_read);
int bit = ui -> spinBox_11 -> value() - 1; //要修改的位，范围0-7
if(ui -> spinBox_12 -> value() == 0)//某一位改为0
{
    int num = data_read[0] & (255 - static_cast<int>(pow(2, bit)));
    data_write[0] = static_cast<byte>(0xff & num);
}

else//某一位改为1
{
    int num = data_read[0] | static_cast<int>(pow(2, bit));
    data_write[0] = static_cast<byte>(0xff & num);
}

//把byte数组写入到DB块中
int result = Cli_DBWrite(plc_client, DBNumber, Start, 1, data_write);
```
