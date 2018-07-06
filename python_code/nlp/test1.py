
import pickle
import codecs
import jieba# 分词模块
import multiprocessing
import codecs
import pandas as pd
from gensim.models.word2vec import Word2Vec

train_file = "train.csv"
test_file = "test.csv"
train_file = codecs.open(train_file, 'r', 'utf-8')
train_lines = train_file.readlines()
test_file = codecs.open(test_file, 'r', 'utf-8')
test_lines = test_file.readlines()

label = []
train_title = []
train_content = []
train_title_cut = []
train_content_cut = []

test_id = []
test_title = []
test_content = []
test_title_cut = []
test_content_cut = []

print("Segment train title/content...")
for i in range(len(train_lines)):
    if i % 10000 == 0:
        print(i)
    if len(train_lines[i].split('\t')) != 4:
        continue
    article_id, title, content, l = train_lines[i].split('\t')
    if 'NEGATIVE' in l:
        label.append(0)
    else:
        label.append(1)

    train_title.append(title)
    train_content.append(content)
    train_title_cut.append(' '.join(jieba.cut(title.strip('\n'), cut_all=False)))
    train_content_cut.append(' '.join(jieba.cut(content.strip('\n'), cut_all=False)))

print("Segment train completed.")
print("Segment test title/content...")
for i in range(len(test_lines)):
    if i % 10000 == 0:
        print(i)
    if len(test_lines[i].split('\t')) != 3:
        continue
    article_id, title, content = test_lines[i].split('\t')

    test_id.append(article_id)

    test_title.append(title)
    test_content.append(content)
    test_title_cut.append(' '.join(jieba.cut(title.strip('\n'), cut_all=False)))
    test_content_cut.append(' '.join(jieba.cut(content.strip('\n'), cut_all=False)))
print("Segment test completed.")

pickle.dump(label, open('train_label.p', 'wb'))
pickle.dump(train_title, open('train_title.p', 'wb'))
pickle.dump(train_content, open('train_content.p', 'wb'))
pickle.dump(train_title_cut, open('train_title_cut.p', 'wb'))
pickle.dump(train_content_cut, open('train_content_cut.p', 'wb'))
pickle.dump(test_id, open('test_id.p', 'wb'))
pickle.dump(test_title, open('test_title.p', 'wb'))
pickle.dump(test_content, open('test_content.p', 'wb'))
pickle.dump(test_title_cut, open('test_title_cut.p', 'wb'))
pickle.dump(test_content_cut, open('test_content_cut.p', 'wb'))

corpus = train_title_cut + train_content_cut + test_title_cut + test_content_cut

class CorpusData:
    def __init__(self, corpus):
        self.corpus = corpus
    def __iter__(self):
        for doc in corpus:
            origin_words = doc.split(' ')
            yield origin_words

print("Train word to vector...")
corpus_data = CorpusData(corpus)
model = Word2Vec(corpus_data, size=256, window=5, min_count=5, workers=15)
model.save('w2v_model_s256_w5_m5.save')
print("Train w2v completed.")