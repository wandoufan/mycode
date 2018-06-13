import requests,queue

from lxml import etree

url='https://movie.douban.com/subject/1292052/'

data=requests.get(url).text

s=etree.HTML(data)

film=s.xpath('//*[@id="content"]/h1/span[1]/text()')

director=s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')

actor=s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')

print(film)
print(director)
print(actor)
