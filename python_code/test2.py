
import re

path1 = '/data/share/corpus/cws/pku_1998/pku_holdout'
path2 = '/data/share/corpus/cws/pku_1998/pku_test'
path3 = '/data/share/corpus/cws/pku_1998/pku_training'
for file_path in (path1, path2, path3):
	with open(file_path, 'r') as file:
		for line in file:
			list1 = line.split()
			for word in list1:
				if re.search(r'[a-z][\u4E00-\u9FA5]|[A-Z][\u4E00-\u9FA5]|[\u4E00-\u9FA5][a-z]|[\u4E00-\u9FA5][A-Z]', word) is not None:
					print(word)





