from flask import Flask,render_template
app = Flask(__name__)

#render_template函数用来渲染模板
@app.route('/')
def index():
    #用字典结构一次性传入多个参数
    context={
    'name':'Tom',
    'age':18,
    'sex':'boy'
    }
    return render_template('index.html',**context)#用**来传递多个参数

@app.route('/login')
def login():
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)

    