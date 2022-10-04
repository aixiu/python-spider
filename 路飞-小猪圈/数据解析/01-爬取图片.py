# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/04 09:36:36

# 需求：爬取糗事百科中糗图板块下所有的糗图图片
import requests

if __name__ == '__main__':
    # 如何爬取图片数据
    url = 'https://static.qiushibaike.com/images/download/slogan.png'
    # content 返回的是二进制形式的图片数据
    # text 返回的是字符串   contet 返回二进制数据   json 返回 对象
    img_data = requests.get(url=url).content
    
    with open('./qiutu.png', mode='wb') as fp:
        fp.write(img_data)
