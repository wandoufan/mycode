# coding:utf-8
from discover_word import word_segment
import requests
import json

def test(text):
    return word_segment(text)

if __name__ == '__main__':
    file_path = '/data/share/tmp/new_words_mining/test_v1.1/zhoujielun'
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    result = test(text)
    print('!!!!', len(result))
    print(result)


