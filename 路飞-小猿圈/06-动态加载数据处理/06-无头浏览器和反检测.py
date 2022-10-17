# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/17 11:20:17

# 参考地址：https://blog.csdn.net/weixin_51368459/article/details/125462178

# 无头浏览器就是无可视化界面
from selenium import webdriver
from selenium.webdriver.edge.service import Service
# 无头Edge浏览器库及规避检测
from selenium.webdriver.edge.options import Options

import time

# 创建一个参数对象，用来控制 Edge以无界面模式打开
edge_options = Options()
# 使用无头模式
edge_options.add_argument('--headless')
# 禁用GPU，防止无头模式出现莫名的BUG
edge_options.add_argument('--disable-gpu')

# 反检测设置 #
# 规避被检测到的风险
# 开启开发者模式
# option = EdgeOptions()
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 禁用启用Blink运行时的功能
edge_options.add_argument('--disable-blink-features=AutomationControlled')


# 将参数传给浏览器 (options=edge_options)  即可实现无头浏览器  还有phantomJs 等。
bro = webdriver.Edge(service=Service('./msedgedriver.exe'), options=edge_options)
bro.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
# 代码中url所指网站可以检测浏览器是否通过selenium控制，如果未检测出selenium控制，则"WebDriver"一栏为绿色。

print(bro.page_source)
time.sleep(2)
bro.quit()
