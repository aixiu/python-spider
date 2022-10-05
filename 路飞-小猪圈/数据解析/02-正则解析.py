# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/04 09:41:55

import requests
import re
import os

# 需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/pic/'
    
    #创建一个文件夹：
    #   os.path.exists() 判断文件夹是否存在
    #   os.mkdir() 创建文件夹
    
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')    
    
    # UA伪装：将对应的 User-Agent 封装备到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    # 使用以爱用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text
    
    # 使用聚焦爬虫将页面中
    ex = '<div class="thumb">.*?<img src="(.*?)".*?</div>'
    
    img_src_list = re.findall(ex, page_text, re.S)   #加re.S是为了让.匹配换行符
    # print(img_src_list)
    
    for src in img_src_list:
        #图片真实地址:https://pic.qiushibaike.com/system/pictures/12403/124037906/medium/O0ZS2I1ETML5XKP1.jpg
        # 爬取的地址和图片的真实地址差一个'https:'
        src = f'https:{src}'
        # 请求到了图片的二进制数据  因为图片是二进制格式，所以用requests.get().content
        img_data = requests.get(url=src, headers=headers).content
        
        # 获取图片的name,通过split截取链接的最后一部分用来作为图片的name，区分不同的图片
        img_name = src.split('/')[-1]
        img_path = f'./qiutuLibs/{img_name}'
        
        # 以二进制形式写文件，'wb':以二进制形式写文件
        with open(img_path, mode='wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！')
    
        
        