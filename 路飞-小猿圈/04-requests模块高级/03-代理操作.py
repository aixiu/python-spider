# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/12 11:55:10

'''
代理ip的类型：
    - http: 应用到https协议对应的url中
    - https: 应用到https协议对应的url中
代理ip的匿名度：
    - 透明：服务器知道该此请求使用了代理，也知道请求对应的真实IP
    - 匿名：服务器知道使用了代理，但是不知道真实IP
    - 高匿：服务器不知道使用了代理，更不知道真实IP

'''

import requests

url = 'https://ynxiu.cn/ip/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
}
ip = '124.71.186.187:3128'
proxies = {
    # 表示将一个代理ip拼接上它应该走的协议
    'http': f'http://{ip}',
    'https': f'http://{ip}'
    # "http": proxy,
    # "https": proxy,
}

page_text = requests.get(url=url, headers=headers, proxies=proxies, timeout=10)
page_text.encoding = page_text.apparent_encoding

with open('./ip.html',mode='w', encoding='utf-8') as fp:
    fp.write(page_text.text)