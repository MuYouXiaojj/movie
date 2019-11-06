# _*_ coding: utf-8 _*_
# __author__ = 'Moliao'
# __data__ = '2019/9/9 16:33'


from app import app
from flask_script import Manager

manage = Manager(app)

if __name__ == '__main__':
    manage.run(host='0.0.0.0',port = 5000)
