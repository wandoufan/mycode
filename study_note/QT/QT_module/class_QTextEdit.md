# QTextEdit

## 基本功能
QTextEdit是一个富文本控件，可以用来编辑和显示各种文本信息  
父类：QAbstractScrollArea  
子类：QTextBrowser  
备注：.pro文件中要声明'QT += widgets'  


## 构造函数
1. QTextEdit::QTextEdit(const QString &text, QWidget \*parent = nullptr)
text参数会显示在文本框内，相当于设置一个初始文本  

2. QTextEdit::QTextEdit(QWidget \*parent = nullptr)


## 常用公共函数
1. QString toHtml() const
以html格式返回文本框中的内容  

2. QString toMarkdown(QTextDocument::MarkdownFeatures features = QTextDocument::MarkdownDialectGitHub) const
以Markdown格式返回文本框中的内容  

3. QString QTextEdit::toPlainText() const
以富文本格式返回文本框中的内容  


## 常用公共槽函数
1. [slot] void QTextEdit::clear()
注意：清除文本内容时，字体格式也会被重置，redo/undo的历史会被清除  

2. [slot] void QTextEdit::copy()
将选中的文本内容复制到粘贴板(需要先选中文本内容)  

3. [slot] void QTextEdit::cut()
将选中的文本内容剪切(需要先选中文本内容)  

4. [slot] void QTextEdit::paste()
将粘贴板中的内容复制到当前光标所在位置  

5. [slot] void QTextEdit::redo()
重复上次的操作  

6. [slot] void QTextEdit::undo()
撤销上次的操作  

7. [slot] void QTextEdit::selectAll()
选中全部文本  

8. [slot] void QTextEdit::append(const QString &text)
以追加模式向文本末尾添加内容  

9. [slot] void QTextEdit::setText(const QString &text)
向文本框中设置文本内容(原本的文本内容会被清空)  
备注：如果内容是中文的，会显示乱码，需要设置编码  
```
ui -> message_column -> setText(QString::fromLocal8Bit("这是测试"));
```


## 常用信号函数
1. [signal] void QTextEdit::textChanged()