#coding:utf-8

#程序初始化，导入Flask类
from flask import Flask 
#程序实例app是Flask类的对象
app = Flask(__name__)

#修饰器route()告诉Flask什么样的URL才能触发函数
@app.route('/')
def index():
    return "Hello World"
    
#访问../test2和../test2/和../test都会到达目标页面，但访问../test/会404 not found
@app.route('/test')
def test():
    return 'this is a test'
@app.route('/test2/')
def test2():
    return 'this is a test2'

#可以给URL添加变量部分<variable_name>，变量会作为命名参数传递到函数中
@app.route('/user/<username>')
def show_username(username):
    return 'user is %s' % username
#可以用 <converter:variable_name> 指定一个可选的转换器(包括：int,float,path)
@app.route('/user/<int:userid>')
def show_userid(userid):
    return 'ID is %d' % userid
@app.route('/user/<path:userpath>')
def show_path(userpath):
    return 'path is %s' % userpath




if __name__=='__main__':
    app.run(debug=True)