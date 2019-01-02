# coding:utf-8
from flask import Flask, render_template
app = Flask(__name__)

#for遍历字典
@app.route('/user')
def index():
    user={'name':'li','age':10,'sex':'boy'}
    return render_template('for.html',user_info=user)

#for遍历列表
@app.route('/color')
def color():
    color = ['bule', 'red', 'black', 'white']
    print('a')
    return render_template('for.html', color_list=color)

if __name__ == '__main__':
    app.run(debug=True)
