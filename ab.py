#-*-coding:utf-8-*-
from flask import Flask,render_template,request,redirect,flash,get_flashed_messages
import logging


app = Flask(__name__)
app.secret_key='ssas'

@app.route('/')
def index():
    res = ''
    for msg,info in get_flashed_messages(with_categories=True):
        res += msg + info + '<br>'
    res = res + 'hello'
    return res

@app.route('/profile/<int:uid>')
def profile(uid):
    colors = ['red','green']
    return render_template('profile.html',uid = uid,colors = colors)

@app.route('/newpath/')
def newpath0():
    return '跳转成功!'

@app.route('/re/<int:code>')
def tiaozhuan_demo(code):
    return redirect('/newpath/',code = code)

#错误处理
@app.errorhandler(404)
def page_notfound(error):
    print(error)
    return render_template('page_not_found.html',url = request.url)

@app.route('/login/')
def login():
    flash('deng lu cheng gong',category='INFO')
    return redirect('/')
# def log(func):
#     def wrapper():
#         print('begining.....')
#         func()
#         print('ending.....')
#     return wrapper

# def log(level,func):
#     def wrapper(*a,**b):
#         print(a)
#         print(b)
#         print('begining.....')
#         func(*a,**b)
#         print('ending.....')
#     return wrapper
#
# @log(level='INFO')
# def hello(name,age):
#     print('hello word'+' '+name+' '+str(age))

if __name__ == '__main__':
    app.run()#log(func)