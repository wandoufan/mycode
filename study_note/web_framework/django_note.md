# 主要记录django相关的知识


## django的处理流程
* 用户通过浏览器发出一个请求
* 请求传递到urls.py中，django在urlpatterns中匹配链接，在匹配到的第一个就停下来
* 匹配成功后django根据path找到views.py中对应的函数或类
* 根据views.py中具体的情况，直接返回内容给用户或者找到对应的templates中的内容返回给用户
* 如果匹配到最后一个地址后没有找到，则用户端出现报错界面



## django项目的结构
```
project_name
├── app1_name
│   ├── admin.py  后台文件，实现后台管理功能
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py  数据库文件，定义数据表、数据表中的字段、字段的属性等
│   ├── templates  存放html模板，可以被views.py中函数渲染后得到动态内容的网页
│   │   └── home.html  html页面文件，文件中可以加入django提供特殊的模板标签{}
│   ├── tests.py
│   └── views.py  定义实现不同功能的函数或类，根据需要关联templates中的模板文件
├── app2_name
│   └── 结构类似app1
├── db.sqlite3  数据库文件，默认使用sqlite3数据库
├── manage.py  django创建完项目后自动在目录中生成manage.py，可以用'python manage.py 参数'命令实现很多功能
└── project_name
    ├── __init__.py
    ├── settings.py  可以设置关联数据库(DATABASES)、关联自己创建的app(INSTALLED_APPS)、配置模板文件路径(TEMPLATES)等
    ├── urls.py  通过urlpatterns匹配用户的请求地址，并关联每个地址到views.py中的函数或类
    └── wsgi.py
```

### urls.py文件示例
```
from django.contrib import admin
from django.urls import path
from calc import views as calc_views

urlpatterns = [
    path('', calc_views.index, name='home'),
    path('add/', calc_views.add, name='add'),
    path('admin/', admin.site.urls),
    path('add/<int:a>/<int:b>/', calc_views.old_add2_redirect),
    path('new_add/<int:a>/<int:b>/', calc_views.add2, name='add2'),
]
```
备注：path函数中的name参数可以用于在templates、models、views中得到对应的网址，相当于给网址取了个名字  

### views.py文件示例
```
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

def add(request):
    """
    匹配路径：path('add/', calc_views.add, name='add')
    请求形式：http://127.0.0.1:8002/add/?a=4&b=5
    """
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    """
    匹配路径：path('new_add/<int:a>/<int:b>/', calc_views.add2, name='add2')
    请求形式：http://127.0.0.1:8002/new_add/4/5/
    """
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    """
    匹配路径：path('add/<int:a>/<int:b>/', calc_views.old_add2_redirect)
    利用reverse函数实现url跳转
    将形如'/add/4/5/'的请求跳转到add2函数的'/new_add/4/5/'地址上
    """
    return HttpResponseRedirect(reverse('add2', args=(a, b)))

def home(request):
    """
    利用render函数返回templates目录中的html模板，第三个可选参数以字典结构返回数据
    数据包括列表、字符串、字典等各种类型，数据将在html文件中被调用
    """
    string = 'django中使用各种数据类型'
    num_list = [1,2,3,4,5]
    info_dict = {'name':'豌豆帆', 'age':10, 'color':'bule'}
    return render(request, 'home.html', {'string':string, 'num_list':num_list, 'info_dict':info_dict})

```
备注：request.GET对象类似于字典结构，推荐使用request.GET.get('a', 0)，当没有传递a参数时默认a为0  
备注：调用render函数后django会自动找到INSTALLED_APPS中列出的各个app下的templates目录中的html模板文件  
备注：要在TEMPLATES参数中设置DIRS，即指定templates文件的路径，否则可能会报错TemplateDoesNotExist  
示例：'DIRS': [os.path.join(BASE_DIR, 'HelloWorld/templates')],

### models.py文件示例
* 创建一个Person数据表，包含name字段(字符型)、int字段(整型)
```
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name
```
备注：Django中所有的模型(Model)都必须继承django.db.models.Model模型，即顶部的导入  
备注：推荐在数据表中写一个__str__函数，否则查询或显示的结果都会是'Person object'，无法对每一行数据做区分  

### home.html文件示例
```
<!DOCTYPE html>
<html>
<head>
    <title>豌豆帆</title>
</head>
<body>
豌豆帆 django测试
<p>{{string}}</p>
<p>{% for i in num_list %}
{{i}}
{% endfor %}</p>
<p>{% for k, v in info_dict.items %}
<p>{{k}}:{{v}}</p>
{% endfor %}</p>
</body>
</html>
```
备注：django提供特殊的模板标签{}，这些标签与html无关，但是可以写在html中  

### admin.py文件示例
* admin.py实现后台管理的功能，创建后台管理员账户后，可以通过'127.0.0.1/admin'登录进去
* 在后台管理界面可以直接以管理员的身份对Article进行增删改查等操作(不要提前自己定义各种操作)
```
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```



## django中的常用命令
* 'django-admin.py startproject project_name'  新建一个django项目
* 'django-admin.py startapp app_name'  进入项目目录后新建一个应用
* 'python manage.py startapp app_name'  进入项目目录后新建一个应用
备注：以上两个命令功能一样
* 'python manage.py makemigrations'  创建更改的文件(修改mdoels.py中数据表后要重新运行该命令更新)
备注：上面命令运行后会生成文件，如'article/migrations/0002_article_updated.py'  
* 'python manage.py migrate'  将py文件应用到数据库(首次执行后就会在项目目录中生成数据库文件如db.sqlite3等)
备注：上面命令运行后数据库文件如db.sqlite3就会相应进行更新
* 'python manage.py runserver port'  运行项目，后面可以加端口，不指定则默认8000端口
* 'python manage.py flush'  清空数据库
* 'python manage.py createsuperuser'  创建后台管理员(用于登录'localhost\admin')，指定账户邮箱密码
* 'python manage.py changepassword username'  修改账户密码
* 'python manage.py dumpdata appname > appname.json'  导出数据
* 'python manage.py loaddata appname.json'  导入数据
* 'python manage.py shell'  进入python的shell，在这个shell中可以调用当前项目的models.py中的API
* 'python manage.py dbshell'  进入settings.py中配置的数据库的shell，在这个shell中可以直接使用sql语句

备注: 一个项目一般包含多个应用，一个应用也可以用在多个项目中
备注：django创建完项目后自动在目录中生成manage.py文件
备注：django-admin.py是安装django后多出的一个命令，并不是运行的当前目录下的django-admin.py(实际也没有这个文件)



## django中的模板标签{} 
* 这些模板标签可以看做是jinja2模板，django对其进行了封装，可以在django中直接使用
```
<!DOCTYPE html>
<html>
<head>
    <title>豌豆帆</title>
</head>
<body>
豌豆帆 django测试
<p>{{string}}</p>
<p>{% for i in num_list %}
{{i}}
{% endfor %}</p>
<p>{% for k, v in info_dict.items %}
<p>{{k}}:{{v}}</p>
{% endfor %}</p>
</body>
</html>
```
* django提供特殊的模板标签{}，这些标签与html无关，但是可以写在html中 
* 模板中的列表、字符串、字典等类型的变量来自于views.py中render函数的返回
* 一般的变量之类的用{{ }}来表示，功能类的如循环、条件判断等用{%  %}来表示

### if/else标签
```
{% if condition1 %}
   展示1
{% elif condition2 %}
   展示2
{% else %}
   展示3
{% endif %}
```
注意：条件判断完成后要用{% endif %}来表示结束  

### for标签
```
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
```
注意：序列迭代完成后要用来{% endfor %}表示结束  
备注：使用reversed关键字可以使序列被反向迭代，{% for athlete in athlete_list reversed %}  
备注：for循环中还提供forloop变量，可以提供更复杂的功能  
* forloop.first  当遍历的元素为第一项时为true，否则为false
* forloop.last   当遍历的元素为最后一项时为true，否则为false
* forloop.parentloop  用在嵌套的for循环中，获取上一层for循环的forloop
* forloop.counter  索引从1开始算
* forloop.counter0   索引从0开始算
* forloop.revcounter  索引从最大长度到1
* forloop.revcounter0  索引从最大长度到0

### empty标签
* 在循环中当列表为空值时执行empty标签后边的内容
```
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>列表已为空值</li>
{% endfor %}
```

### ifequal/ifnotequal标签
* {% ifequal %}标签比较两个值，如果值相等则返回true，否则为false
```
{% ifequal user root %}
    <h1>欢迎管理员</h1>
{% else %}
    <h1>非管理员账户</h1>
{% endifequal %}
```
注意：比较完成后要用{% endifequal %}来表示结束  

### 注释标签
```
{# 这是一个注释 #}
```

### 过滤器标签
* 模板过滤器可以在变量被显示前修改它，过滤器使用管道字符
```
{{ string|lower }}  # 将string变量都转换为小写再显示
{{ string|length}}  # 显示string变量的长度
```

### 逻辑符号
* ==、!=、>=、<=、>、< 这些比较符号都可以在模板中使用
* and、or、not、in、not in 这些逻辑符号也可以在模板中使用
注意：逻辑符号在html中使用时，前后至少要有一个空格  

### 模板标签中的字典类型
```
{% for key, value in info_dict.items %}
    {{ key }}: {{ value }}
{% endfor %}
```
注意：在模板中dict获取值是dict.key，而不是python中的dict[key]  

### 模板标签中的request
* 在模板标签中可以使用request实现多种功能
```
{{ request.user }}  获取当前用户
{{ request.user.username }}  获取当前用户的用户名
{{ request.path }}  获取当前网址
{{ request.GET.urlencode }}  获取当前GET参数
```

### 继承模板
* 模板可以通过继承进行复用
* 撰写基本模板：所有可重定义的地方用{% block 块名 %}XXX{% endblock %}表示出来
* 继承模板：开头处声明要继承的模板{% extends 'html文件名' %}，重写处用{% block 块名 %}XXX{% endblock %}表示出来
* 调用模板：{% include '模板名' %}



## django与数据库

### 数据库配置
* django支持sqlite3、Mysql、Postgresql等数据库，默认使用sqlite3数据库(无需安装配置)
* 如果需要使用其他数据库，在settings.py中配置DATABASES即可
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER':'root',
        'PASSWORD': '******', 
        'HOST': '127.0.0.1',  
        'POST': '3306',
    }
}
```

### 数据库文件models.py
* 创建一个Person数据表，包含name字段(字符型)、int字段(整型)
```
from django.db import models

# models.py中定义的类必须继承来自django中的models.Model
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name
```
备注：推荐在数据表中写一个__str__函数，否则查询或显示的结果都会是'Person object'，无法对每一行数据做区分  
> https://docs.djangoproject.com/en/dev/topics/db/models/

### models.py中的字段类型
* AutoField  自增长字段
不需要手动设置就可以根据ID自动递增，默认为主键字段，映射到数据库中是11位的整数  
* BooleanField  布尔字段
映射到数据库中会变成长度只有1位的tinyint类型，只能存储True/False，不能存储null  
* IntegerField  整数字段
映射到数据库中会变成11位的int类型  
* FloatField  浮点数字段
映射到数据库中会变成double类型  
* CharField  字符串字段
classCharField(max_length = None,** options)  
CharField.max_length为必选参数，设定字段的最大字符数，用于用于数据库层级和django的数据验证层级  
映射到数据库中会转换成varchar类型，用于存储较短的字符串  
* TextField  大文本字段
映射到数据库中会转换成text类型，用于存储较长的字符串  
* ImageField  图片字段
classImageField(upload_to = None,height_field = None,width_field = None,max_length = 100,** options)  
* FileField  文件字段
classFileField(upload_to = None,max_length = 100,** options)  
* DateField  日期字段
classDateField(auto_now = False，auto_now_add = False，** options)  
DateField.auto_now每次保存对象时自动将字段设置为现在，对最后修改的时间戳有用  
DateField.auto_now_add首次创建对象时自动将字段设置为现在，用于创建时间戳  
在python中对应的是datetime.date类型，在映射到数据库中是date类型  
* TimeField  时间字段
classTimeField(auto_now = False，auto_now_add = False，** options)，参数含义同上  
在python中对应的是datetime.time类型，在映射到数据库中是time类型  
* DateTimeField  日期时间字段
classDateTimeField(auto_now = False，auto_now_add = False，** options)，参数含义同上  
在python中对应的是datetime.datetime类型，在映射到数据库中是datetime类型  

### models.py中的字段选项
* null
如果True，django将NULL在数据库中存储空值，默认为False  
注意：尽量不再字符串类型的字段上使用null，如TextField和CharField，因为无法区分空字符串和null  
* blank
如果True，该字段允许为空，默认是False  
注意：blank表示运行不存储数据，null表示存储的数据值为空  
* db_column
存储此字段的数据库对应的列名称，如果没有给出，django将使用该字段的名称作为数据库中字段的名称  
* db_index
如果True，将为此字段创建数据库索引  
* primary_key
如果True，此字段是数据表的主键，如果没有指定任何字段，django将自动添加一个AutoField来保存主键  
注意：自动添加的主键字段默认为id，通过'类名.id'可以查看id值  
* unique
如果True，该字段在整个表格中必须是唯一的，一般是设置手机号码/邮箱等  
* default
设置字段的默认值，可以为一个值，或者是一个函数，在用函数作为值传递给default时，只能传递函数名，不需要加括号  
不支持lambda表达式。也不支持列表、字典、集合等可变的数据结构  
* choices
在一个范围内选择出一项，对应的值一般是二元元组，元组中第一个元素是实际值，第二个元素是便于理解的描述
```  
TYPE_CHOICES = ((1, '第一类'),(2, '第二类'),(3, '第三类'),)  
type = models.IntegerField(default=0,choices=TYPE_CHOICES) 
``` 
注意：choices字段可以在django admin中显示下拉框  

### QuerySet API接口
* django提供专门的数据库接口QuerySet API，有自己单独的增删改查操作语法(不同于sql语法)
* 通过QuerySet API这种间接操作数据库的方式属于ORM模型
注意：对数据表及字段的定义是写在models.py中的，但对表中数据增删改查的操作是写在views.py中的
* 使用QuerySet API的数据库语法进行数据操作的views.py示例：
```
from django.shortcuts import render
from models import Book
from django.http import HttpResponse

def index(request):
    # 1. 使用ORM添加一条数据到数据库中
    book = Book(name='三国演义',author='罗贯中',price=200)
    book.save()
    # 2. 查询
    # 2.1 使用主键进行查询，直接返回要查询的类对象
    book = Book.objects.get(pk=1)
    print(book.name,book.author,book.price)
    # 2.2 根据其他条件进行查找，返回的是一个列表，将所有满足条件的类对象都放在列表里面
    books = Book.objects.filter(name='三国演义')
    print(books[0].name,books[0].author,books[0].price)
    # 3. 删除数据
    book = Book.objects.get(pk = 1)
    book.delete()
    # 4. 修改数据
    book = Book.objects.get(pk=2)
    book.price = 200
    book.save()
    # 5.初始化查询集，得到一个包含Book表中所有数据的类对象
    book_list = Book.objects.all()
    book_list = book_list.filter(name='三国演义')
    return HttpResponse('图书插入成功')
```
> https://code.ziqiangxuetang.com/django/django-queryset-api.html
> https://docs.djangoproject.com/en/dev/ref/models/querysets/

### ORM模型
* ORM(Object Relational Mapping)，即对象关系映射，通过ORM我们可以通过类的方式去操作数据库，而不用再写原生的sql语句
* 通过把表映射成类，把行作实例，把字段作为属性，ORM在执行对象操作的时候最终还是会把对应的操作转换为数据库原生语句
* django中使用原生sql语句的缺点：
1.sql语句重复利用率不高，越复杂的sql语句条件越多，代码越长，会出现很多相近的sql语句  
2.很多sql语句是在业务逻辑中拼出来的，如果业务逻辑生变，原生sql更改起来比较多  
3.写sql时容易忽略web安全问题，造成一些如sql注入之类的安全漏洞  
* 使用ORM模型操作数据库的优点：
1.使用ORM做数据库的开发可以有效的减少重复SQL语句的概率，写出来的模型也更加直观、清晰  
2.ORM语句转化成原生的sql语句需要一定开销，但实际造成的性能损耗很小  
3.设计更加灵活，可以写出更加复杂的查询语句  
4.django封装了底层的数据库实现，ORM语句可以在sqlite3、Mysql、Postgresql等多种数据库间自由切换  

### 在django中使用原生的sql语句
* 除了上述基于ORM模型的QuerySet API外，django还提供了用原生sql语句操作数据库的接口
* 使用原生sql语句进行数据操作的views.py示例：
```
from django.db import connection

cursor=connection.cursor()
cursor.execute("insert into hello_author(name) values('郭敬明')")
```



## django实现前后端交互

### html中的表单简介
* 表单可以让用户通过前端页面提交信息到后台，实现前后端交互，例如用户输入账户密码实现登录功能
* html本身提供了表单功能，标签为 <form>，允许用户在表单中输入内容
> https://code.ziqiangxuetang.com/html/html-forms.html
```
<form>
普通文本域(text)
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname">
</form>

<form>
密码字段(password)，不会明文显示，用户输入后以星号或圆点代替
Password: <input type="password" name="pwd">
</form>

<form>
单选按钮(radio)
<input type="radio" name="sex" value="male">Male<br>
<input type="radio" name="sex" value="female">Female
</form>

<form>
复选框(checkbox)
<input type="checkbox" name="transportation" value="Bike">I have a bike<br>
<input type="checkbox" name="transportation" value="Car">I have a car 
</form>

<form name="input" action="html_form_action.php" method="get">
提交按钮(submit)，当用户单击确认按钮时，表单的内容会被传送到另一个文件
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>
```

### django中的表单文件forms.py
* django在forms.py中提供表单功能，可以实现表单渲染、数据验证等功能
* 实现表单功能的forms.py示例：
```
# 引入表单类
from django import forms
# 引入文章模型
from .models import Article

# forms.py中定义的类必须继承来自django中的forms.ModelForm
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = Article
        # 指明从html表单中返回的字段
        # fields = '__all__'
        fields = ('title', 'body')
```
注意：在表单类中必须用model参数指明对应的数据表，用fields参数指明对应的表中字段  
forms.py接收从html中返回的字段，并赋值给models.py中对应的字段  
fields指明的字段必须和从html表单中返回的字段，以及models.py中定义的字段保持一致  
备注：fields指明部分字段时可以用元组表示，如果包含models类中所有字段，也可以写做fields = '__all__'  
例如：models.py的Article类中定义了一个发表时间字段，但该字段是根据当前时间自动填写的，  
不需要用户在前端页面中填写，因此从前端返回的字段就不包含这个时间字段  

* 以上forms.py对应的html文件
```
<!DOCTYPE html>
<html>
<head>
    <title>豌豆帆 创建文章</title>
</head>
<body>
<!-- 写文章表单 -->
<div class="container">
    <div class="row">
        <div class="col-12">
            <br>
            <!-- 提交文章的表单 -->
            <form method="post" action="." enctype="multipart/form-data">
                <!-- Django中需要POST数据的地方都必须有csrf_token -->
                {% csrf_token %}

                <!-- 文章标题 -->
                <div class="form-group">
                    <!-- 标签 -->
                    <label for="title">文章标题</label>
                    <!-- 文本框 -->
                    <input type="text" 
                           class="form-control" 
                           id="title" 
                           name="title"
                    >
                </div>

                <!-- 文章正文 -->
                <div class="form-group">
                    <label for="body">文章正文</label>
                    <!-- 文本区域 -->
                    <textarea type="text" 
                              class="form-control" 
                              id="body" 
                              name="body" 
                              rows="12"
                    ></textarea>
                </div>
                <!-- 提交按钮 -->
                <button type="submit" class="btn btn-primary">完成</button>
            </form>
        </div>
    </div>
</div>
</body>
</html>
```
注意：html文件中用post方法来传送数据时必须加上{% csrf_token %}，csrf_token可以预防跨站攻击  
注意：当用post提交数据的时候，django会去检查是否有一个csrf的随机字符串，如果没有就会报错  
备注：django中有内置的中间件django.middleware.csrf.CsrfViewMiddleware来实现相关功能  

* 以上forms.py对应的views.py文件
```
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .forms import ArticlePostForm

def article_create(request):
    """
    创建博客文章
    """
    # 如果用户提交了数据，就将数据保存，之后给用户反馈结果
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        atricle_post_form = ArticlePostForm(request.POST)
        # 判断提交数据是否合法
        if atricle_post_form.is_valid():
            atricle_post_form.save()
            return HttpResponse('数据已保存成功！')
        else:
            # 报错并返回错误原因
            return HttpResponse('报错：%s' % atricle_post_form.errors)
    # 如果第一次匹配到url，用户还没有填写内容时，跳转到创建博客页面
    else:
        atricle_post_form = ArticlePostForm()
        content = {'atricle_post_form': atricle_post_form}
        return render(request, 'article/create.html', content)

```
备注：atricle_post_form.is_valid()方法是form中的一个组件，判断数据是否有效，返回True或False  
注意：只有forms.py中的表单类才有is_valid()方法，models.py中的数据表类没有is_valid()方法  
备注：如果is_valid()方法报错，可以通过输出atricle_post_form.errors属性来查看报错原因
备注：request.POST类似一个字典结构，包含用户在前端页面中填写的各种信息以及'csrfmiddlewaretoken'字段  
备注：request.FILES类似一个字典结构，包含用户从前端页面中提交的各种文件图片等  
备注：atricle_post_form.cleaned_data方法可以得到一个字典结构，包含表单的返回值，即request.POST中的数据

> https://code.ziqiangxuetang.com/django/django-forms.html



## django中的用户管理系统

### 内置auth模块简介
* django内置了用户管理系统，通过django.contrib.auth实现用户身份认证、用户组、权限管理等功能
之前获取用户输入的用户名和密码后要自己从user表中查询是否匹配，auth模块可以协助我们快速实现用户登录信息验证  
settings.py的INSTALLED_APPS中已经默认添加了django.contrib.auth，可以直接使用相关功能  

* 1.authenticate()
authenticate()方法提供了用户认证的功能，即验证用户名和密码是否正确，需要username和password两个关键字参数  
如果认证有效，会返回一个user对象，authenticate()方法会在user对象上标记该用户已经过后端认证，用于后续登录  
注意：如果直接从数据库中取出一个user对象，没有经过authenticate()方法的认证，该用户在登录时会报错  
```
user = authenticate(username='someone',password='somepassword')
```

* 2.login(HttpRequest, user)
login()方法接收一个HttpRequest对象和一个已经经过认证的user对象，没有返回值，实现用户登录的功能  
login()方法使用django的session框架给某个已认证的用户附加上session id等信息  
```
from django.contrib.auth import authenticate, login
   
def my_view(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirect to a success page.
    ...
  else:
    # Return an 'invalid login' error message.
    ...
```

* 3.logout(HttpRequest)
logout()方法接收一个HttpRequest对象，没有返回值，实现注销用户的功能  
当调用该函数时，当前请求的session信息会全部清除。该用户即使没有登录，使用该函数也不会报错  
```
from django.contrib.auth import logout
   
def logout_view(request):
  logout(request)
 # Redirect to a success page.
```

### user对象
user对象是django中经过authenticate()认证的对象，具有多种内置的方法和属性，数据库中对应的用户表为auth_user  
注意：django只有一个用户类，即使超级用户(superusers)也只是设置了特别属性的该用户类  
* user表的sql描述：
```
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "password" varchar(128) NOT NULL, 
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30), 
    "last_name" varchar(30),
    "email" varchar(254), 
    "is_superuser" bool, 
    "is_staff" bool, 
    "is_active" bool,
    "last_login" datetime NULL, 
    "date_joined" datetime,
    "groups" varchar,
)
```
password和username是必填项，其中password用哈希算法加密后保存到数据库  
is_staff属性为布尔值，设置用户是否有网站的管理权限，即是否可以登录/admin管理界面  
is_active属性为布尔值，设置允许用户登录，设置为False时可以不删除用户来禁止用户登录，相当于激活功能  
is_superuser属性为布尔值，设置用户是否为超级用户，超级用户拥有全部权限  
date_joined属性为用户的创建时间  
last_login属性为用户的最近登录时间  
groups属性为用户的用户组，这是一个多对多字段  
> https://www.cnblogs.com/linxiyue/p/4060213.html   

* 1.is_authenticated()
is_authenticated()方法检查user对象是否通过了认证，返回一个布尔值，常用来检查用户是否登录  
如果is_authenticated()返回True，则可以request.user.name查看用户名  
注意：通过认证不代表用户拥有任何权限，也不代表用户已经激活  
方法1：直接用is_authenticated()方法验证用户是否登录  
```
def my_view(request):
   if not request.user.is_authenticated():
      return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
```
方法2：根据request.user.username来验证，如果为空，则说明没有登录  
```
def my_view(request):
   if not request.user.username:
      return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
```
方法3：django内置了用于检查用户登录状态的装饰器login_requierd()  
若用户没有登录，则会跳转到django默认的登录url'/accounts/login/'(这个值可以在settings文件中通过LOGIN_URL进行修改)  
并且登录成功后会重新定向到当前访问的url路径上  
```
from django.contrib.auth.decorators import login_required
    
@login_required
def my_view(request):
   pass
```

* 2.create_user()
create_user()方法用来创建新用户  
```
from django.contrib.auth.models import User
user = User.objects.create_user（username='',password='',email=''）
```

* 3.check_password() / set_password()
check_password()方法用来检查用户密码是否正确，返回一个布尔值  
set_password()方法用来修改用户密码，一般修改前要先验证之前的密码是否正确  
```
user = User.objects.get(username='')
if user.check_password(old_passwd):
   user.set_password(password=new_passwd)
   user.save()
```

### 用户组group
django.contrib.auth.models.Group定义了用户组的模型,每个用户组拥有id和name两个字段， 数据库中对应的用户组表为auth_group  
user对象中有一个groups的多对多字段，多对多关系由auth_user_groups数据表维护  
备注：group对象可以通过user_set反向查询用户组中的用户  

* 1.通过group对象添加或删除用户组
```
from django.contrib.auth.models import Group

group = Group.objects.create(name=group_name) 
group.save()
group.delete()
```

* 2.管理用户与用户组的关系  
```
# 用户加入用户组
user.groups.add(group)
# 用户加入用户组
group.user_set.add(user)

# 用户退出用户组
user.groups.remove(group)
#用户退出用户组
group.user_set.remove(user)

# 用户退出所有用户组
user.groups.clear()
# 用户组中所有用户退出组
group.user_set.clear()
```

### 权限管理
django的auth模块提供权限管理功能，可以检查用户是否对某个数据表有增、删、改的权限  
注意：auth模块无法提供对象级的权限控制， 即检查用户是否对数据表中某条记录(如一篇博客)拥有增改删的权限  
备注：如果需要对象级权限控制可以使用django-guardian  

* 1.has_perm()
has_perm()检查一个user对象是否对指定数据表的权限，并返回一个布尔值  
备注：has_perm()仅是进行权限检查, 即是用户没有权限它也不会阻止程序员执行相关操作  
```
# 检查user是否对article模型有权限
user.has_perm('blog.add_article')
user.has_perm('blog.change_article')
user.has_perm('blog.delete_article')
```
@permission_required装饰器可以代替has_perm并在用户没有相应权限时重定向到登录页或者抛出异常  
permission_required(perm[, login_url=None, raise_exception=False])  
```
@permission_required('blog.add_article')
def post_article(request):
    pass
```

* 2.管理用户权限
user和permission通过多对多字段user.user_permissions关联，在数据库中由auth_user_user_permissions数据表维护  
```
#添加权限
user.user_permissions.add(permission)
#删除权限: 
user.user_permissions.delete(permission)
#清空权限: 
user.user_permissions.clear()
```

* 3.管理用户组权限
group和permission通过多对多字段permissions关联，在数据库中由auth_group_permissions数据表维护  
用户默认继承所属用户组的权限，可以通过设置用户组的权限来批量管理用户权限  
```
#添加权限: 
group.permissions.add(permission)
#删除权限: 
group.permissions.delete(permission)
#清空权限: 
group.permissions.clear()
```






## django中的静态文件
* 静态文件是指网站中的js、css、图片、视频等文件
* 如果要使用静态文件需要在setting.py中做配置修改，静态文件放在对应的app下的static文件夹中

