# 1.关于装饰器@app.route()：
# route()装饰器把一个函数绑定到对应的URL上，告诉Flask什么样的URL才能触发函数
# URL中还可以添加变量部分

# 2.关于url_for(func,[variable_name])函数:
# flask可以用url_for()函数来给指定的函数构造URL,它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。

# 3.关于页面重定向：
# 可以用 redirect() 函数把用户重定向到其它地方,比如未登陆用户点击内容页面时先跳转到登陆页面

# 4.关于render_template():
# Flask 配备了 Jinja2 模板引擎,可以使用 render_template()方法来渲染模板。
# 参数是模板名（html文件名）和变量的值，其中HTML文件需要放在templates 文件夹里

# 5.关于jinja:
# jinja是Flask中用来渲染模板的模板引擎，它在HTML的基础上增加了变量和if/for循环等功能；
# jinja中变量用{{variable_name}}来表示,可以识别列表，字典，对象等所有的变量类型；
# {% if a=b%}#注意：语句结尾处不用加冒号
#    pass
# {% endif %}#注意：结尾处要加上endif/endfor

# 6.关于templates文件夹：
# 将HTML文件都放在程序目录下的templates文件夹中，在flask程序中可以直接调用HTML文件且不需要再给出具体的路径
# app.py程序和templates文件夹在目录中应该平级，在同一目录下
# 如果HTML放在/templates/a文件夹中，调用时也要加上/a路径

# 7.关于过滤器：
# Jinja中提供过滤器来处理变量，过滤器有非常多，类似于Python中各种方法和函数的功能，格式为{{variable|过滤器名}}

