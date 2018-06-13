#coding:utf-8

from flask import Flask,render_template, url_for
app = Flask(__name__)

#过滤器：作用对象是变量，把原始的变量处理后再展示出来，过滤器有很多中

#defult过滤器：如果当前变量不存在可以指定默认值,例如用户没有设置头像时给指定默认头像
#写在HTML中：{{variable|default('value')}} 如果变量没有指定值，则变量设为default的值
@app.route('/')
def index():
    #有指定的头像
    # return render_template('filter.html',picture='http://img4.imgtn.bdimg.com/it/u=1373411777,3992091759&fm=27&gp=0.jpg')
    #没有指定的头像
    return render_template('filter.html')

if __name__=='__main__':
    app.run(debug=True)