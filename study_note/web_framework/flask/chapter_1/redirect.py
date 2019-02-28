#coding:utf-8

from flask import Flask,url_for,redirect,abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"
#redirect() 函数把用户重定向到其它地方,例如未登陆用户查看内容时先跳转到登陆页面
@app.route('/write')
def write():
    #暂时不做用户登陆状态判断，默认未登陆，直接跳转到登陆界面
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return 'this is login page'

#abort()函数放弃请求并返回指定的错误类型
@app.route('/admin')
def forbid():
    abort(404)


if __name__=='__main__':
    app.run(debug=True)