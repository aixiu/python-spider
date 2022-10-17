# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/17 08:27:46

from selenium import webdriver
from selenium.webdriver.edge.service import Service
# 导入动作链对应的类
from selenium.webdriver import ActionChains

import time

bro = webdriver.Edge(service=Service('./msedgedriver.exe'))

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于 iframe 标签之中则必须如下操作进行定位
bro.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域
div = bro.find_element(by='id', value='draggable')

# 动作链
action =ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    # perform()立即执行动作链操作
    # move_by_offset(x, y): x水平方向  y垂直方赂
    action.move_by_offset(25, 0).perform()
    time.sleep(0.3)
    
# 释放动作链
action.release().perform()

print(div)

bro.quit()