# coding:utf-8
import csv


def read_file(inpath, outpath):
    '''
    把指定csv文件的第三列由'a,b,c,d'拆分成每个各单独一列
    '''
    word_list = []
    with open(outpath, 'wt', encoding='utf-8') as out_file:
        csv_writer = csv.writer(out_file, dialect='excel')
        with open(inpath, 'rt', encoding='utf-8') as in_file:
            content = csv.reader(in_file)
            for line in content:
                title = line[0]
                text = line[1]
                keywords = line[2]
                word_list = keywords.split(',')
                row = []
                row.append(title)
                row.append(text)
                for i in range(5):
                    row.append(word_list[i])
                csv_writer.writerow(row)

if __name__ == '__main__':
    inpath = 'C:/mywork/collection_02_result_0901.csv'
    outpath = 'C:/mywork/a.csv'
    read_file(inpath, outpath)
