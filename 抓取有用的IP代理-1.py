# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/12 17:28:43

import requests
from lxml import etree

'''
抓取：www.ip3366.net
创建两个列表用来存放代理ip
原型：https://www.jb51.net/article/252466.htm
'''

all_ip_list = []  #用于存放从网站上抓取到的ip
usable_ip_list = [] #用于存放通过检测ip后是否可以使用

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
}

# 检测ip是否可以使用
def test_ip(proxy):
    # 构造代理ip需要的字典
    proxies = {
        # 表示将一个代理ip拼接上它应该走的协议
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
        # "http": proxy,
        # "https": proxy,
    }
    try:
        response = requests.get(url='https://www.baidu.com/', headers=headers, proxies=proxies, timeout=1) #设置timeout，使响应等待1s
        response.close()
        if response.status_code == 200:
            usable_ip_list.append(proxy)
            print(proxy, '\033[31m可用\033[0m')   # 红字
        else:
            print(proxy, '\033[32m可用\033[0m')   # 黄字
    except:
        print(proxy,'请求异常')
        
        
# 发送请求，获得响应，抓取免费的代理
def send_request():
    #爬取9页，可自行修改
    for page in range(1,10):
        print(f'=====正在抓取第{page}页=====')
        response = requests.get(url=f'http://www.ip3366.net/free/?page={page}', headers=headers, timeout=20)
        response.encoding = response.apparent_encoding
        #使用xpath解析，提取出数据ip，端口
        tree = etree.HTML(response.text)
        tr_list = tree.xpath("//*[@id='list']//tbody/tr")
        for td in tr_list:
            ip_ = td.xpath('./td[1]/text()')[0] #ip
            port_ = td.xpath('./td[2]/text()')[0]  #端口
            proxy = f"{ip_}:{port_}"   #115.218.5.5:9000
            all_ip_list.append(proxy)
            test_ip(proxy)      #开始检测获取到的ip是否可以使用
            
    print('抓取完成！')
    print(f'抓取到的ip个数为：{len(all_ip_list)}')
    print(f'可以使用的ip个数为：{len(usable_ip_list)}')
    print('分别有：\n', usable_ip_list)
    
if __name__ == '__main__':
    send_request()


            
        
        
        
        

'''
print 显示颜色，知识点：

    # 格式：
    # 　　设置颜色开始 ：\033[显示方式;前景色;背景色m
    # 说明：
    # 前景色            背景色           颜色
    # ---------------------------------------
    # 30                40              黑色
    # 31                41              红色
    # 32                42              绿色
    # 33                43              黃色
    # 34                44              蓝色
    # 35                45              紫红色
    # 36                46              青蓝色
    # 37                47              白色
    # 显示方式           意义
    # -------------------------
    # 0                终端默认设置
    # 1                高亮显示
    # 4                使用下划线
    # 5                闪烁
    # 7                反白显示
    # 8                不可见
    
'''
