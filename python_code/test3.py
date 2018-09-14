# coding:utf-8
from discover_word import word_segment
import csv

file_path = '/data/share/corpus/military/ner_data/news_data/all_news.csv'

def get_word(text):

    result = word_segment(text)
    # print(result)
    word_list = list(result.keys())
    word_list.remove('code')
    word_list.remove('message')
    return word_list



with open(file_path, 'rt') as csv_file:
    content = csv.reader(csv_file)
    result_list = []
    for line in content:
        text = line[2]
        result_list.extend(get_word(text))
        print('新词结果 ：', result_list)
    result_set = set(result_list)
    print('集合长度 : ', result_set)
    print(result_set)



