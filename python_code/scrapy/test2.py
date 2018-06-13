import requests

from lxml import etree

url='https://book.douban.com/top250'

data=requests.get(url).text

s=etree.HTML(data)

#得到的bookname,pingfen等都是列表类型的数据
bookname=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')

pingfen=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')

comment=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/p[2]/span/text()')

# for i,j,k in zip(bookname,pingfen,comment):
#     print(i,j,k)

#book的路径比其他子元素的路径都要高，其他子元素的路径可以跟在其后边只写后半部分
# #实际测试不行？？？AttributeError: 'lxml.etree._ElementUnicodeResult' object has no attribute 'xpath'
# book=s.xpath('//*[@id="content"]/div/div[1]/div/table/text()')
# for i in book:
#     number=i.xpath('./tr/td[2]/div[2]/span[3]/text()')






#[0]表示取列表的第一个元素，.strip()方法用来处理文本，表示要删除文本的括号中的内容，内容为空时表示删除空白符
number=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip().strip(")")
#number=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[3]/text()')
for i in number:
    print(i)


