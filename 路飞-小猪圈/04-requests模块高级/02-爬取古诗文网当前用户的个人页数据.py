# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/11 23:08:14

import requests
from lxml import etree


'''
    网站设置了cookie反爬！那我们带上cookie来试试看
    
    # 定义一个session对象
    session = requests.Session()
'''
    
# 定义一个session对象  cookie 用服务器端记录客户端相关状态
session = requests.Session()     
    
if __name__ == '__main__':
    # 将验证码图片下载到本地
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
    }
    
    page_text = session.get(url=url, headers=headers, timeout=20)
    page_text.encoding = page_text.apparent_encoding
    # 解析验证码图片img中的src属性值
    tree = etree.HTML(page_text.text)
    # img_url = "https://so.gushiwen.cn{}".format(tree.xpath("//div[@class='mainreg2']/img/@src")[0])  # 第一种 
    img_url = "https://so.gushiwen.cn{}".format(tree.xpath("//*[@id='imgCode']/@src")[0]) # 第二种 
    img_data =  session.get(url=img_url, headers=headers, timeout=20)
    img_data.encoding = img_data.apparent_encoding    
    
    with open('./code_img/code.jpg', mode='wb') as fp:
        fp.write(img_data.content)

    # 调用 ddddocr 库进行验证码图片数据识别：
    import ddddocr

    def recognize():
        ocr = ddddocr.DdddOcr()
        with open('./code_img/code.jpg', 'rb') as fp:
            img_bytes = fp.read()
        res = ocr.classification(img_bytes)
        return res
    
    code_text = recognize().upper()  # 转换成大写

    data = {
        '__VIEWSTATE': 'zMZfRlutsU1x0/2uRYJCZuYEayFcGn3lD8P8cGXreVyW0SwleipeFCauejkU/oavmiv6sAKRRO9bEeTdW6qrOn1U7yl88F4r5Z+Ut/ImJzvD2qMRpCgNZtFrIw/6rsL3nj0Y8aP8g+8PCFEWM8Q4f5NUdRo=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '4815563@qq.com',
        'pwd': 'shendlax520',
        'code': code_text,  # 验证码动态变化
        'denglu': '登录'
    }
    print(f"当前验证码为：{data['code']}")
    
    logging_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    
    
    
    # 对点击登陆按钮发起请求:获取了登录成功后对应的页面源码数据
    page_text_login = session.post(url=logging_url, headers=headers, data=data, timeout=20)
    page_text_login.encoding = page_text_login.apparent_encoding
    print(f"状态码为：{page_text_login.status_code}")    

    with open('./gushiwen.html', mode='w', encoding='utf-8') as fp:
        fp.write(page_text_login.text)
    print("用户登录成功！")
    
    # 爬取当前用户的个人主页对应的页面数据
    detail_url = 'https://so.gushiwen.cn/user/collect.aspx?type=s&id=3516635&sort=t'
    
    detail_page_text = session.get(url=detail_url, headers=headers, timeout=20)
    detail_page_text.encoding = detail_page_text.apparent_encoding
    with open('./geren.html', mode='w', encoding='utf-8') as fp:
        fp.write(detail_page_text.text)
    print("个人页面爬取成功！")
