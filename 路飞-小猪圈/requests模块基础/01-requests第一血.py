#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import requests

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=20)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Something Wrong!'
    
    
def gethtml(url):
    try:
        
    except:

if __name__ == '__main__':
    # setp1: 指定url
    url = "https://sogou.com/"
    
    # setp2: 发起请求
    # get方法会返回一个响应对象
    response = requests.get(url=url)
    
    # setp3: 获取响应数据 .text 返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    
    # setp4: 持久化存储
    with open("./sogou.html", mode="w", encoding="utf-8") as fp:
        fp.write(page_text)
        
    print("爬取数据结束！！！")
    
    
