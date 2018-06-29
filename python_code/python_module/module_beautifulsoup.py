# https://blog.csdn.net/love666666shen/article/details/77512353
# http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id7
# https://cuiqingcai.com/1319.html


# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码

from bs4 import BeautifulSoup  # bs4就是Beautiful Soup 4
import requests

douban_url = 'https://movie.douban.com/chart'
response = requests.get(douban_url)
content = response.text
# 'html.parser'是指最常用的HTML解析器，属于python内置的标准库
soup = BeautifulSoup(content, 'html.parser')

# 注意：beautifulsoup中最常用的是d和e中介绍的find方法和select方法

# a.常用获取数据方法:
# 按照标准缩进格式输出html文档的内容
# print(soup.prettify())
# 找到html文档中的标题
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# 找到第一个<P>标签
# print(soup.p)
# print(soup.p['class'])
# 找到第一个<a>标签
# print(soup.a)
# print(soup.a['href'])
# 找到所有的<a>标签
# print(soup.find_all('a'))
# 找到所有的<a>标签中的链接
# for a_tag in soup.find_all('a'):
#     print(a_tag['href'])
# 从html文档中获取所有的文字内容
# print(soup.get_text())


# b.四大对象种类:
# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
# 所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .

# 1.Tag,就是html中的一个标签
# 利用soup.标签名就可以轻松获取标签的内容，但找到的都是符合要求的第一个标签；
# print(type(soup.head))
# 对于Tag，有两个重要的属性：name和attrs
# print(soup.title.name)# 标签的name属性一般就是标签本身的名字
# print(soup.a.attrs)# 输出一个包含标签所有属性的字典
# print(soup.a.get('class'), soup.a['class'])# 可以按照字典方法去获取标签的某一个属性

# 2.NavigableString,就是标签内部的文字部分
# print(type(soup.p.string))
# 利用soup.标签名.string就可以获取标签中的文字,当前有多个标签时可能返回None
# print(soup.p.string)

# 3.BeautifulSoup,表示的是一个html文档的全部内容,可以当做一个特殊的Tag
# print(type(soup))
# 同样可以获得特殊标签的name,attrs等属性
# print(soup.name)
# print(soup.attrs)

# 4.Comment,是一个特殊类型的NavigableString对象,内容不包括注释符号
# bs4.element.Comment类型主要针对带有注释的标签


# c.遍历文档树：
# 1.获取直接子节点
# tag的.contents属性可以输出一个包含tag子节点的列表
# print(soup.head.contents)
# tag的.children属性输出一个可以迭代的list生成器对象
# print(soup.head.children)
# 遍历方法可以获取所有的内容
# for child in soup.head.children:
#     print(child)

# 2.获取所有子孙节点
# tag的.descendants属性可以递归的获取tag的所有子孙节点
# for child in soup.head.descendants:
#     print(child)

# 3.获取节点内容
# tag的.string属性会返回tag内的文字
# 当标签内没有子标签时，会返回标签的内容；当标签有唯一子标签时，会返回子标签的内容
# print(soup.title.string)
# 当标签内有多个子标签时，.string方法就无法确定该调用哪个子节点的内容，返回None
# print(soup.head.string)

# 4.获取多个节点的内容
# tag的.strings属性可以用遍历方法获取多个内容
# for string in soup.strings:
#     print(string)
# tag的.stripped_strings可以用遍历方法获取多个内容，同时去除多余的空格
# for string in soup.stripped_strings:
#     print(string)

# 5.获取父节点
# tag的.parent属性可以获取到tag的父节点
# print(soup.a.parent.name)

# 6.获取所有父节点
# tag的.parents属性可以递归的获取到tag的父节点和父节点的父节点
# content = soup.head.title.string
# for parent in content.parents:
#     print(parent.name)

# 7.获取兄弟节点
# tag的.next_sibling和.previous_sibling属性分别返回tag的前一个和下一个兄弟节点
# 如果兄弟节点不存在了，就返回None
# 注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
# 因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行
# tag = soup.a
# print(tag.next_sibling)
# print(tag.next_sibling.next_sibling)
# print(tag.previous_sibling.previous_sibling)

# 8.获取全部兄弟节点
# tag的.next_siblings和.previous_siblings属性可以迭代输出所有兄弟节点
# tag = soup.title
# for sibling in tag.next_siblings:
#     print(sibling)

# 9.获取前后节点
# ？？？

# 10.获取全部前后节点
# ？？？


# d.搜索文档树：
# 常用的两个方法如下，都是只搜索当前节点的所有子孙节点
# 唯一区别就是find直接返回结果，find_all返回包含多个结果的列表
# find(name, attrs, recursive, text, **kwargs)
# find_all(name, attrs, recursive, text, **kwargs )

# 1.name参数
# 可以通过指定标签名字为name来查找tag,字符串对象会被自动忽略掉
# name参数可以为字符串,例如'a','head','title'
# print(soup.find_all('a'))
# name参数可以为列表,匹配列表中的所有元素
# print(soup.find_all(['a','title']))
# name参数可以为True,可以匹配任何值，返回所有节点
# for tag in soup.find_all(True):
# 	print(tag.string)

# 2.keyword参数
# 可以通过指定tag具体的属性值来查找tag
# print(soup.find_all(target = '_blank'))
# 可以同时指定多个属性来实现更精确的查找
# print(soup.find_all(target = '_blank', href = 'https://music.douban.com'))
# 特殊地,对于class既是tag属性又是python关键字,使用搜索时加上下划线即可
# print(soup.find_all(class_ = 'lnk-doubanapp'))

# 3.text参数
# 可以通过指定标签的文字内容来查找tag,但返回结果并不是标签
# print(soup.find('title').string)
# print(soup.find_all(text = '豆瓣电影排行榜'))

# 4.limit参数
# 可以通过指定limit的值来限制搜索和返回结果的数量
# print(soup.find_all('a', limit = 3))

# 5.recursive参数
# 可以通过设置recursive=False,来让find只搜索当前节点的直接子节点
# 如果不指定，默认会递归搜索所有子孙节点
# tag = soup.find('body')
# print(tag.find_all('div'))
# print(tag.find_all('div',recursive = False))

# 其他搜索方法(参数等和上面的find方法都一致)：
# find_parents()和find_parent()，搜索当前节点的父节点
# find_next_siblings()和find_next_sibling()，搜索当前节点之后的所有兄弟节点
# find_previous_siblings()和find_previous_sibling()，搜索当前节点之前的所有兄弟节点
# find_all_next()和find_next()，搜索当前节点后边的所有节点
# find_all_previous()和find_previous()，搜索当前节点前面的所有节点


# e.CSS选择器：
# 我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加#，
# 同样也可以利用类似的方法来筛选元素，用到的方法是soup.select()，返回结果是列表

# 1.通过标签名查找,不加任何修饰
# print(soup.select('title'))
# print(soup.select('a')[3])

# 2.通过类名class的值查找,tag中class对应的值前面要加点
# print(soup.select('.lnk-doubanapp'))

# 3.通过id的值查找,tag中id对应的值前面要加#
# print(soup.select('#inp-query'))

# 4.组合查找
# 不同标签中间用空格隔开，例如查找body标签中的link标签
# print(len(soup.select('body link')))
# print(len(soup.select('link')))

# 5.属性查找
# 要查找的属性用中括号，属性和tag要属于同一节点，中间不加空格
# 例如查找class值为lnk-doubanapp的a标签
# print(soup.select('a[class=lnk-doubanapp]'))
# 例如查找body标签中class值为no的div标签，不同的标签中间要加空格
# for div_tag in soup.select('body div[class=no]'):
# 	print(div_tag)
# 用find方法来实现上面的功能(可以发现find方法更麻烦)：
# body_tag = soup.find_all('body')[0]
# div_tags = body_tag.find_all('div')
# for div_tag in div_tags:
# 	if 'class' in div_tag.attrs:
# 		if 'no' in div_tag.get('class'):
# 			print(div_tag)
