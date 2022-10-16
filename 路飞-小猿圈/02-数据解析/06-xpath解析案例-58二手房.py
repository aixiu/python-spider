# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/10 21:32:20

# 需求： 爬取58二手房中的房源信息   https://bj.58.com/ershoufang

import requests
from lxml import etree

def getHtmlText(url, headers):
    try:
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return 'Something Wrong!'
    
    
if __name__ == '__main__':
    # 爬取到页面源码数据
    url = 'https://gz.zu.ke.com/zufang'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    page_text = getHtmlText(url, headers)
    
    # 数据解析
    tree = etree.HTML(page_text)
    title_list = tree.xpath("//div[@class='content__list']//a[1]/@title")
    jiage = tree.xpath("//div[@class='content__list']//span[@class='content__list--item-price']/em/text()")
    fangyuan = zip(title_list, jiage)
    
    with open('./贝壳二手房.txt', mode='w', encoding='utf-8') as fp:        
        for title, jiage in fangyuan:
            fp.write(f'{title}\t==>\t{jiage}元\n')
        print("爬取完毕")
    
    
        
    
    
    

    
