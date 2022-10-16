# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/12 21:22:12

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
}

urls = [
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202210/zjianli557.rar',
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202210/zjianli563.rar',
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202210/zjianli561.rar',
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202210/zjianli568.rar',
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202210/zjianli552.rar',
    'https://downsc.chinaz.net/Files/DownLoad/jianli/202210/zjianli555.rar',
]

def get_content(url):
    print(f'正在爬取：{url}')
    # get方法是一个阻塞的方法
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content
    
def parse_content(content):
    print(f'响应数据的长度为：{len(content)}')
    
for url in urls:
    content = get_content(url)
    parse_content(content)