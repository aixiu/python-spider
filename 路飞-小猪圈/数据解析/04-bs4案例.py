# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/05 10:01:47

import requests
from bs4 import BeautifulSoup
# 需求：爬取三国演义小说所有的章节标题和章节内容

if __name__ == '__main__':
    # 对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    
    # UA伪装：将对应的 User-Agent 封装备到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    page_text = requests.get(url=url, headers=headers,).content
    
    # 在首页中解析出章节的标题和详情页的 url
    # 1.实例化 BeautifulSoup 对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu> ul > li')
    for li in li_list:
        title = li.a.string
        detail_url = f'https://www.shicimingju.com{li.a["href"]}'
        # 对详情面发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        
        
        
        