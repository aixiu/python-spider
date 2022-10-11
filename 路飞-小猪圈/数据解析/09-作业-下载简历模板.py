# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/11 21:10:09



import requests
from lxml import etree
import os

# 获取文本数据函数
def gethtmlText(url, headres):
    try:
        r = requests.get(url=url, headers=headres, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return 'Something Wrong!'

# 获取二进制数据函数   
def gethtmlContent(url, headres):
    try:
        r = requests.get(url=url, headers=headres, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except Exception as e:
        return 'Something Wrong!'
    
    
if __name__ == '__main__':
    # 主URL
    url = 'https://sc.chinaz.com/jianli/free.html'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    
    # 创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')

    # 获取文本数据
    page_text = gethtmlText(url=url, headres=headers)
    
    # 数据解析：href的属性值
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//div[@id='container']/div/a")
    all_urls = []
    
    # 查找每一个文件详情页    
    for li in li_list:        
        all_urls.append(f"https:{li.xpath('./@href')[0]}")
    
    # 找到每个详情页的下载地址：   
    for xq_url in all_urls:
        xq_page_text = gethtmlContent(url=xq_url, headres=headers)
        xq_tree = etree.HTML(xq_page_text)
        
        # 具体下载地址
        down_url = xq_tree.xpath("//div[@class='clearfix mt20 downlist']/ul/li/a/@href")[0]
        
        # 文件名
        file_name = f"{xq_tree.xpath('//h1/text()')[0]}.rar"
        # 定义文件路径
        file_path = f'./picLibs/{file_name}.'
        
        # 获取文件下载数据
        file_data = gethtmlContent(url=down_url, headres=headers)
        
        # 下载文件持久化保存
        with open(file_path, mode='wb') as fp:
            fp.write(file_data)
            print(f"{file_name}  ==>  下载成功！！")
        