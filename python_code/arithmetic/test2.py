#输入某年某月某日，判断这一天是这一年的第几天？
#将输入的字符串进行分段处理
date=list(input('请输入格式为2018-05-01的日期：'))
year=date[0:4]
month=date[5:7]
day=date[8:10]

year1=int(date[0])*1000+int(date[1])*100+int(date[2])*10+int(date[3])

print(date)
print(year,month,day,year1)

