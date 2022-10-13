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

def gethtmlText(url, headers):
    try:
        r = requests.get(url=url, headers=headers, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return 'Something Wrong!'
    
def gethtmlContent(url, headers):
    try:
        r = requests.get(url=url, headers=headers, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except Exception as e:
        return 'Something Wrong!'
    
    
if __name__ == '__main__':
    # 将验证码图片下载到本地
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    page_text =  gethtmlText(url=url, headers=headers)
    # 解析验证码图片img中的src属性值
    tree = etree.HTML(page_text)
    # img_url = "https://so.gushiwen.cn{}".format(tree.xpath("//div[@class='mainreg2']/img/@src")[0])  # 第一种 
    img_url = "https://so.gushiwen.cn{}".format(tree.xpath("//*[@id='imgCode']/@src")[0]) # 第二种 
    img_data =  gethtmlContent(url=img_url, headers=headers)
    
    with open('./code_img/code.jpg', mode='wb') as fp:
        fp.write(img_data)

    # 调用 ddddocr 库进行验证码图片数据识别：
    import ddddocr

    def recognize():
        ocr = ddddocr.DdddOcr()
        with open('./code_img/code.jpg', 'rb') as fp:
            img_bytes = fp.read()
        res = ocr.classification(img_bytes)
        return res
    
    code_text = recognize()

    data = {
        '__VIEWSTATE': 'zMZfRlutsU1x0/2uRYJCZuYEayFcGn3lD8P8cGXreVyW0SwleipeFCauejkU/oavmiv6sAKRRO9bEeTdW6qrOn1U7yl88F4r5Z+Ut/ImJzvD2qMRpCgNZtFrIw/6rsL3nj0Y8aP8g+8PCFEWM8Q4f5NUdRo=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '4815563@qq.com',
        'pwd': 'shendlax520',
        'code': code_text,  # 验证码动态变化
        'denglu': '登录'
    }
    print(data['code'])
    
    logging_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    
    # 定义一个session对象
    session = requests.Session() 
    
    # 对点击登陆按钮发起请求:获取了登录成功后对应的页面源码数据
    response = session.post(url=logging_url, headers=headers, data=data, timeout=20) 
    print(response.status_code)
    
    page_text_login = response.text
    
    with open('./gushiwen.html', mode='w', encoding='utf-8') as fp:
        fp.write(page_text_login)
    print("登录成功")
    
    
    
    


    
    
