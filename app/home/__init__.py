# _*_ coding: utf-8 _*_
# __author__ = 'Moliao'
# __data__ = '2019/9/9 16:34'

from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views