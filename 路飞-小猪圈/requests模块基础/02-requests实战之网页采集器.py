#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time: 2022/10/01 22:21:03

import requests

'''
    UA： User-Agent  (请求载体的身份标识)
    
    UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，就说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标 识不是某一款浏览器的，则表示该请求为不正常的请求（爬虫），则服务器端就很有可能拒绝该次请求。
    
    UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器。
'''

if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    
    # UA伪装：将对应的 User-Agent 封装备到一个字典中
    heaaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    kw = input('enter a word: ')
    # 处理url携带的参数：封装到字典中
    param = {
        'query': kw
    }

    # 对指定的url发起的请求对应的url是携带参数的，并且请求垸程中处理了参数
    response = requests.get(url=url, params=param, headers=heaaders)    
    page_text = response.text
    fileName = f'{kw}.html'
    with open(fileName, mode='w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')
    