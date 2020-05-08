# 门控制循环单元（GRU）


## GRU对LSTM的改动
1. 将输入门、遗忘门、输出门变为两个门：更新门(Update Gate)和重置门(Reset Gate)  
2. 将单元状态与输出合并为一个状态  
GRU只用了两个gates，将LSTM中的输入门和遗忘门合并成了更新门  
而且并不把线性自更新建立在额外的memorycell上，而是直接线性累积建立在隐藏状态上，并靠gates来调控  