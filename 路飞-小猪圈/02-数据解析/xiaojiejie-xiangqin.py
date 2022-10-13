# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/05 11:14:27

import requests
import os
import re

if __name__ == '__main__':
    url = 'https://www.mmonly.cc/mmtp/list_9_1.html'
    
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./xiaojiejie'):
        os.mkdir('./xiaojiejie')
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    proxies = {
        "http": "103.247.121.114:8080",
        "http": "101.255.140.130:8080",
        "http": "120.26.0.11:8080",
    }
    
    page_text = requests.get(url=url, headers=headers, proxies=proxies).text
    
    ex = '<div class="img">.*?href="(.*?)"><img.*?src="(.*?)"'
    # ex1 = '<div id="big-pic">.*?alt="(.*?)".*?src="(.*?)"">'
    ex1 = '<div id="big-pic">.*?alt="(.*?)".*?src="(.*?)"'
    
    img_src_list = re.findall(ex, page_text, re.S)
    
    # print(type(img_src_list))
    # print(img_src_list)
    
    nei_url_list = []
    for src in img_src_list:
        imgname = src[1].split('/')[-1]
        imgpath = f'./xiaojiejie/{imgname}'
        img_src = src[1]        
        nei_url_list.append(src[0])
    
    nei_page_img = []
    nei_page_url = []
    for nei_url in nei_url_list:        
        nei_page_text =  requests.get(url=nei_url, headers=headers, proxies=proxies)
        nei_page_text.encoding = nei_page_text.apparent_encoding
        data = re.findall(ex1, nei_page_text.text, re.S)
        nei_page_url.append(data[0][1])
        print(data[0][1])
        
        
