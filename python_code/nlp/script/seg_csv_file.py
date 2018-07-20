import csv

'''
从baidubaike.csv文件中切出一小部分数据用来做测试
'''

# 注意：用Linux命令可以快速实现,
# 取出test1.txt文件的前100行存入test2.txt文件中，'head 100 test1.txt > test2.txt'


# 原始的CSV文件(一般都非常大)
baike_file = '/data/share/corpus/text_classify/baidubaike/baidubaike.csv'
# 切分出的CSV文件
simple_file = '/data/share/corpus/text_classify/baidubaike/simple.csv'

with open(baike_file, 'rt') as file_1:
	content = csv.reader(file_1)
	with open(simple_file, 'wt') as file_2:
		csv_writer = csv.writer(file_2, dialect='excel')
		count = 0
		for line in content:
			count += 1
			if count > 5:# 5代表从表格中取出5行数据
				break
			csv_writer.writerow(line)
