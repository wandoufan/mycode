# coding:utf-8

# XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。
# XPath 是 XSLT 中的主要元素,XPath 是一个 W3C 标准

# XPath 含有超过 100 个内建的函数。这些函数用于字符串值、数值、日期和时间比较、节点和 QName 处理、序列处理、逻辑值等等。
# XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。

# Xpath 即为 XML路径语言（XML path language）,它是一种用来确定XML文档中某部分位置的语言。

# Xpath基于XML的树状结构，提供在树中寻找节点的能力，常被用作小型查询语言和网页解析工具。

#   常见的网页解析方法比较(xpath是lxml的一种）

# 解析方法	 		性能	使用难度	安装难度
# 正则表达式		快		困难		简单（内置模块）
# Beautiful Soup	慢		简单		简单（内置Python）
# lxml				快		简单		困难


# 获取网页中指定信息的Xpath路径：

# 在网页中ctrl+shift+I或者右键‘检查’打开网页的代码；

# ctrl+shift+C，并将鼠标移动到目标元素即可在右侧代码中找到目标代码位置；

# 在右侧代码中右键-copy-copy xpath，即可获得目标的xpath,将其复制到URL路径中；

# 注意：获得的xpath中可能包含多余的tbody标签，如果有，手动删掉这部分。



# url='xpath/text()'或者‘xpath/@title’ ?????????????



# import requests

# from lxml import etree

# url='https://book.douban.com/top250'

# data=requests.get(url).text

# s=etree.HTML(data)

# #得到的bookname,pingfen等都是列表类型的数据
# bookname=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a/@title')

# pingfen=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]/text()')

# comment=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/p[2]/span/text()')

# # for i,j,k in zip(bookname,pingfen,comment):
# #     print(i,j,k)

# #book的路径比其他子元素的路径都要高，其他子元素的路径可以跟在其后边只写后半部分
# book=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/text()')

# #跟网上代码一样，但有报错？？？？
# for div in book:
#     number=div.xpath('./div[2]/span[3]/text()')
#     print(number)




# #[0]表示取列表的第一个元素，.strip()方法用来处理文本，表示要删除文本的括号中的内容，内容为空时表示删除空白符
# # number=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip().strip(")")
# # number=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[3]/text()')


