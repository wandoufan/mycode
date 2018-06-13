import requests

from lxml import etree

for i in range(10):
    url='https://book.douban.com/top250?start='+str(i*25)

    data = requests.get(url).text

    s = etree.HTML(data)

    bookname=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/text()')

    print(bookname)
