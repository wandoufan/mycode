import pandas as pd# 惯例改名为pd
import numpy as np
from pandas import Series# 注意首字母是大写
from pandas import DataFrame# 注意首字母是大写


frame = pd.read_csv('E:/nlp_project/fasttext/sp_channels.csv')

# print(frame.head())

classify_dict = {}

for i in range(len(frame)):
	key = frame.iloc[i]['id']
	value = frame.iloc[i]['name']
	classify_dict[key] = value

# print(classify_dict)

# str1 = str(classify_dict)
# str1 = str1[1:-1]
# # print(str1)

# list1 = str1.split(',')
# print(list1)


# for key,value in classify_dict.items():
# 	print(key,value)

pred_prob = 3.1415926

print(round(pred_prob,2))