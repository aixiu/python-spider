# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/16 16:12:20

# from selenium import webdriver
# from lxml import etree
# import time

# # 因为 msedgedriver.exe 下载放在 python/Scripts 目录下，可以不用写 executable_path= 参数
# # 实例化一个浏览器对象（传入浏览器的驱动程序）
# driver = webdriver.Edge()

# # 让浏览器发起一个指定rul对应的请求
# driver.get('http://scxk.nmpa.gov.cn:81/xk/')  # 已经无法练习，换下边淘宝

# #page_source获取浏览器当前页面的页面源码数据
# page_text=driver.page_source       # 这里获取的动态的页面代码

# print(page_text)

# # 解析企业名称
# tree=etree.HTML(page_text)

# li_list=tree.xpath('//ul[@id="gzlist"]/li')

# for li in li_list:
#     name=li.xpath('./dl/@title')[0]
#     post_url=li.xpath('./dl/a/@href')[0]
#     # print(name)
#     # print(post_url)
#     # driver.get(post_url)
#     # page=driver.page_source
#     # tr=etree.HTML(page)
#     # today_list=tr.xpath('/html/body/div[4]/table/tbody/tr')
#     # #print(today_list)
#     # for t in today_list:
#     #     name=t.xpath('./td[1]/text()')
#     #     #name1 = t.xpath('/td[@id="epsName"]/text()')
#     #     print(name)

# time.sleep(5)    # 代表停留5秒，再继续
# driver.quit()    # 结束模拟浏览器



from selenium import webdriver
from lxml import etree
import time

# 因为 msedgedriver.exe 下载放在 python/Scripts 目录下，可以不用写 executable_path= 参数
# 实例化一个浏览器对象（传入浏览器的驱动程序）
driver = webdriver.Edge()

# 让浏览器发起一个指定rul对应的请求
driver.get(f'https://www.taobao.com/')

# page_source获取浏览器当前页面的页面源码数据
page_text=driver.page_source       # 这里获取的动态的页面代码

# 解析首页商品名字和链接
tree=etree.HTML(page_text)

li_list=tree.xpath('//div[@class="tb-recommend-content-item"]/a')

for li in li_list:
    name = li.xpath('./div[2]/div/text()')[0]
    url = li.xpath('./@href')[0]
    print(f'{name}  ==>  {url}')    

time.sleep(5)    # 代表停留5秒，再继续
driver.quit()    # 结束模拟浏览器