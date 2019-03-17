#-*-coding:utf-8-*-
from flask_script import Manager
from ab import app
import sqlalchemy


manger = Manager(app)

if __name__ == '__main__':
    manger.run()

