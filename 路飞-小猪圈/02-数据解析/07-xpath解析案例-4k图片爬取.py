# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/10 23:11:23

import requests
from lxml import etree
import os

def gethtmlText(url, headres):
    try:
        r = requests.get(url=url, headers=headres, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return 'Something Wrong!'
    
def gethtmlContent(url, headres):
    try:
        r = requests.get(url=url, headers=headres, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except Exception as e:
        return 'Something Wrong!'
    
    
if __name__ == '__main__':
    # 解析下载4k图片
    url = 'http://pic.netbian.com/4kmeinv/'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    page_text = gethtmlText(url=url, headres=headers)
    
    # 数据解析：src的属性值 alt属性
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//div[@class='slist']/ul/li")
    
    # 创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
        
    for li in li_list:
        img_src = f"http://pic.netbian.com{li.xpath('./a/img/@src')[0]}"
        img_name = f"{li.xpath('./a/img/@alt')[0]}.jpg"
        # print(img_src, img_name)
        
        # 图片进行持久化存储
        img_data = gethtmlContent(url=img_src, headres=headers)
        img_path = f"./picLibs/{img_name}"
        
        with open(img_path, mode='wb') as fp:
            fp.write(img_data)
            print(f"{img_name}  ==>  下载成功！！")
        
    
