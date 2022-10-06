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
    
    img_src_list = re.findall(ex, page_text, re.S)
    
    for src in img_src_list:
        imgname = src[1].split('/')[-1]
        imgpath = f'./xiaojiejie/{imgname}'
        src = src[1]
        # fullsrc = src[0]
        img_data = requests.get(url=src, headers=headers, proxies=proxies).content
        with open(imgpath, mode='wb') as fp:
            fp.write(img_data)
            print(f'图片{imgname}下载完毕。')
            