# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/11 20:10:41

# 需求：解析出所有城市名称：http://www.aqistudy.cn/historydata/

import requests
from lxml import etree

def gethtmlText(url, headres):
    try:
        r = requests.get(url=url, headers=headres, timeout=20)
        r.raise_for_status()
        r.encoding =  r.apparent_encoding
        return r.text
    except Exception as e:
        return 'Something Wrong!'

if __name__ == '__main__':
    url = 'http://www.aqistudy.cn/historydata/'
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    page_text = gethtmlText(url=url, headres=headers)
    
    tree = etree.HTML(page_text)
    # 解析到执门城市和所有城市对应的a标签
    # 热门城市a标签层级关系：//div[@class='bottom']/ul/li/a
    # 全部城市a标签层级关系：//div[@class='bottom']/ul/div[2]/li/a
    
    # a_list = tree.xpath("//div[@class='bottom']/ul/li/a | //div[@class='bottom']/ul/div[2]/li/a") # 方法一： 用 | 或
    a_list = tree.xpath("//div[@class='bottom']/ul//li/a")  # 方法二
    all_ciity_names = []
    for a in a_list:
        city_name = a.xpath("./text()")[0]
        all_ciity_names.append(city_name)
        
    print(all_ciity_names, len(all_ciity_names))