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
    
    all_city_names = []
    
    # 解析到了热门城市名称
    hot_li_list = tree.xpath("//div[@class='bottom']/ul/li")
    for li in hot_li_list:
        hot_city_name = li.xpath("./a/text()")[0]
        all_city_names.append(hot_city_name)
    
    # 解析到了全部城市名称
    city_names_list = tree.xpath("//div[@class='bottom']/ul/div[2]/li")
    for li in city_names_list:
        city_name = li.xpath("./a/text()")[0]
        all_city_names.append(city_name)
        
    print(all_city_names, len(all_city_names))
