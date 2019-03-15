#-*-coding:utf-8-*-
import requests
import flask
import random
import re
#random.seed(1)
print(random.random())#0-1之间的浮点数
print(random.random()*100)
print(random.randint(100,200))
print(random.choice(range(100)))
print(random.sample(range(100),4))
str = 'asdas2326dasd48'
p1 = re.compile('[\d]+')
p2 = re.compile('\d')
print(p1.findall(str))
print(p2.findall(str))

a = 'adadc'
print(a.startswith('a'))
d ={1:1,2:4,3:9}
print(d.keys())
for key,value in d.items():
    print(key,value)