from flask import Flask,render_template
app = Flask(__name__)

#路径中带有变量参数，输入路径时要加入变量的值，否则会404
@app.route('/<is_login>/')
def index(is_login):
    #暂时以is_login变量值为'1'代表用户可以登陆
    if is_login=='1':
        username='li'
        #注意传参形式，其中user_name是HTMl文件中的变量名，username是py文件中的变量名
        return render_template('if.html',user_name=username)
    else:
        return render_template('if.html')

if __name__=='__main__':
    app.run(debug=True)
    