import os 
print(os.getcwd())

in_path = 'C:\mywork\mytest\my.txt'

with open(in_path, 'r') as f:
    for line in f.readlines():
        print(line)