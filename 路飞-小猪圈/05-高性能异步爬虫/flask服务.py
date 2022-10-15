# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/15 15:40:09

from flask import Flask
import time

app = Flask(__name__)


# 路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'hello bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'hello jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'hello tom'




if __name__ == '__main__':
    app.run(threaded=True)