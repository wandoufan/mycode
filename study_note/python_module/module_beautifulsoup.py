# coding:utf-8 

# Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库，常用来解析web服务器响应的网页内容
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码

# 参考资料：
# https://blog.csdn.net/love666666shen/article/details/77512353
# http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id7
# https://cuiqingcai.com/1319.html

from bs4 import BeautifulSoup  # bs4就是Beautiful Soup 4
import requests
import re


douban_url = 'https://movie.douban.com/top250'
response = requests.get(douban_url)
content = response.text
# 'html.parser'是指最常用的HTML解析器，属于python内置的标准库
soup = BeautifulSoup(content, 'html.parser')

# 备注：beautifulsoup中最常用的是find方法和select方法
# 备注：既可以soup.find/select，也可以tag.find/select



# 一.搜索文档树(find方法)：
# Beautiful Soup提供了find和find_all方法来搜索当前节点的所有子孙节点
# 区别是find直接返回第一个结果，find_all返回包含所有结果的列表
# 备注：如果没有搜索结果，find会返回None，find_all会返回空列表[]
# find(name, attrs, recursive, text, **kwargs)
# find_all(name, attrs, recursive, text, **kwargs )

# 1.name参数
# name参数通过标签名字查找tag,字符串对象会被自动忽略掉
# name参数可以为字符串,例如'body','head','title'
print(soup.find_all('body'))
# name参数可以为列表,匹配列表中的所有元素
print(soup.find_all(['body','title']))
# name参数可以为True,可以匹配任何值，返回所有节点
for tag in soup.find_all(True):
  print(tag.string)
# name参数可以是一个正则表达式，正则会通过re库中的match()方法来进行匹配
print(soup.find_all(re.compile('^b')))  # 查找所有以b开头的标签

# 2.attrs参数
# attrs参数通过指定tag具体的属性值来查找tag
print(soup.find_all(target = '_blank'))
# 可以同时指定多个属性来实现更精确的查找，多个属性之间用逗号隔开
print(soup.find_all(target = '_blank', href = 'https://music.douban.com'))
# 可以同时的指定标签名和标签属性
print(soup.find('body', target = '_blank'))
# 注意：'class'既是tag属性又是python关键字，在python中使用时要变为'class_'
print(soup.find_all(class_ = 'title'))

# 3.recursive参数
# recursive参数设置搜索时的递归深度，默认会检索当前tag节点的所有子孙节点
# 可以通过设置recursive=False来让find方法只搜索当前节点的直接子节点
print(soup.find_all('div',recursive = False))

# 4.text参数
# text参数搜索标签中的文字内容，但返回结果为列表并非标签，基本没有什么作用
print(soup.find_all(text = '豆瓣电影排行榜'))

# 5.limit参数
# limit参数限制搜索和返回结果的数量，默认会返回所有结果
print(soup.find_all('a', limit = 3))

# 其他搜索方法(参数等和上面的find方法都一致)：
# find_parents()和find_parent()，搜索当前节点的父节点
# find_next_siblings()和find_next_sibling()，搜索当前节点之后的所有兄弟节点
# find_previous_siblings()和find_previous_sibling()，搜索当前节点之前的所有兄弟节点
# find_all_next()和find_next()，搜索当前节点后边的所有节点
# find_all_previous()和find_previous()，搜索当前节点前面的所有节点


# 二.CSS选择器(select方法)：
# Beautiful Soup提供了select方法可以通过CSS选择器的语法查找节点
# soup.select()接收字符串参数，返回结果是列表类型的标签结果
# soup.select_one()只返回查找结果中的第一个

# 1.通过标签名直接查找标签，不加任何修饰
print(soup.select('title'))

# 2.通过标签中class属性的值查找标签，其中属性的值前面要加点.
# 备注：class是标签中的一个属性，如<div class="star">，但并非所有标签都有class属性
print(soup.select('.star'))  # 查找所有标签中class属性的值为'star'的标签
print(soup.select('a.star'))  # 查找所有a标签中class属性的值为'footer'的标签
print(soup.select('.star, .title'))  # 查找所有标签中class属性的值为'star'或'title'的标签

# 3.通过标签中id属性的值查找标签，其中属性的值前面要加井号#
# 备注：id是标签中的一个属性，如<div id="footer">，但并非所有标签都有id属性
print(soup.select('#footer'))  # 查找所有标签中id属性的值为'footer'的标签
print(soup.select('a#footer'))  # 查找所有a标签中id属性的值为'footer'的标签
print(soup.select('#footer, #icp'))  # 查找所有标签中id属性的值为'footer'或'icp'的标签

# 4.通过标签中某个属性的值查找标签
print(soup.select('span[class="title"]'))  # 查找所有span标签中class属性的值为'title'的标签
# 其中属性的值可以与正则表达式结合进行模糊匹配
print(soup.select('span[class^="t"]'))  # 查找所有span标签中class属性的值以't'为开头的标签
print(soup.select('span[class$="e"]'))  # 查找所有span标签中class属性的值以'e'为结尾的标签
print(soup.select('span[class*="i"]'))  # 查找所有span标签中class属性的值中包含'i'的标签

# 5.通过标签中是否存在某个属性查找标签
print(soup.select('span[class]'))  # 查找所有含有class属性的span标签

# 6.通过标签逐层查找下面的子孙标签，多个标签之间用空格隔开
print(soup.select('body div span'))  # 查找body标签中div标签中的span标签

# 7.通过标签查找下面的直接子标签
print(soup.select('a > span'))  # 查找a标签下面的直接子标签span


# 三.4种对象及其属性:
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
# 使用tag.string就可以获取标签中的文字，返回一个字符串类型
# 注意：如果tag下面还包含多个子节点，tag就无法确定.string方法该调用哪个子节点的内容，会返回一个None
# print(tag.string)
# 使用tag.get_text()方法同样可以获取标签中的文字，在tag下面包含多个子节点时仍能有效返回文字，返回一个字符串类型
# 注意：返回的字符串会把tag中的文字和子标签中文字拼接起来
# print(tag.get_text())
# 使用tag.contents可以获取tag下面包括文字和子标签在内的所有内容，返回一个列表结构
# print(tag.contents)

# 3.BeautifulSoup,表示的是一个html文档的全部内容,可以当做一个特殊的Tag
# print(type(soup))
# 同样可以获得特殊标签的name,attrs等属性
# print(soup.name)
# print(soup.attrs)

# 4.Comment,是一个特殊类型的NavigableString对象,内容不包括注释符号
# bs4.element.Comment类型主要针对带有注释的标签


# 四.遍历文档树：
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


# 五.修改文档树
# Beautiful Soup的强项是搜索文档树，但也提供了修改文档的功能
# ......