# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/11 23:08:14

import requests
from lxml import etree

def gethtmlText(url, headres):
    try:
        r = requests.get(url=url, headers=headres, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return 'Something Wrong!'
    
def gethtmlContent(url, headres):
    try:
        r = requests.get(url=url, headers=headres, timeout=20)
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
    
    page_text =  gethtmlText(url=url, headres=headers)
    # 解析验证码图片img中的src属性值
    tree = etree.HTML(page_text)
    # img_url = "https://so.gushiwen.cn{}".format(tree.xpath("//div[@class='mainreg2']/img/@src")[0])  # 第一种 
    img_url = "https://so.gushiwen.cn{}".format(tree.xpath("//*[@id='imgCode']/@src")[0]) # 第二种 
    img_data =  gethtmlContent(url=img_url, headres=headers)
    
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

    nb = recognize()
    print(f"识别结果为 ==> {nb}")

    
    
