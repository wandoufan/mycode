#coding:utf-8

from flask import Flask,url_for 
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/test')
def test():
    return 'this is a test'

@app.route('/user/<username>')
def show_username():
    return 'username is %s' % username

#url_for()函数来给指定的函数构造URL
#它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。
with app.test_request_context():
    print(url_for('index'))
    print(url_for('test'))
    print(url_for('show_username',username='Tom'))

if __name__=='__main__':
    app.run(debug=True)

