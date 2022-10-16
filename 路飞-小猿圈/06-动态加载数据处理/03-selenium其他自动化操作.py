# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/16 17:28:30

from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.common.by import By

bro = webdriver.Edge(executable_path='./msedgedriver')

bro.get('https://www.taobao.com/')

# 标签定位
# search_input = bro.find_element('id', 'q')
search_input = bro.find_element(by='id', value='q')   # 查找ID叫 Q的输入框

# 标签的交互
search_input.send_keys('Ipthone')  # 往输入框里写入内容

# 执行一组js程序
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 滚动条向下滚动一屏
time.sleep(2)

# btn = bro.find_element(by='css selector', value='btn-search')  # 查找class 叫 .btn-search的按钮
btn = bro.find_element(by='class name', value='btn-search')  # 查找class 叫 .btn-search的按钮
# btn = bro.find_element(By.CLASS_NAME, 'btn-search')  # 此方法要用到 BY模块
btn.click()  # 点击按钮动作 

bro.get('http://www.baidu.com')
time.sleep(2)
# 回退
bro.back()
time.sleep(2)
# 前进
bro.forward()

time.sleep(5)
bro.close()


'''
1.只查找一个元素的时候:可以使用find_element(),find_elements()
  find_element()会返回一个WebElement节点对象,但是没找到会报错,而find_elements()不会,之后返回一个空列表
2.查找多个元素的时候:只能用find_elements(),返回一个列表,列表里的元素全是WebElement节点对象
3.找到都是节点(标签)
4.如果想要获取相关内容(只对find_element()有效,列表对象没有这个属性)  使用  .text;
5.如果想要获取相关属性的值(如href对应的链接等,只对find_element()有效,列表对象没有这个属性):使用  .get_attribute("href")                                        
'''

'''
find_element属于定位元素中的另一种方法，包含了常用的定位方法，使用的时候可能和其他的使用方法不一样
源码中包含了我们的使用方法，但是我们正常去使用的时候会报错，因为找不到By模块，所以我们首先要导入By模块。


# 导入By模块
from selenium.webdriver.common.by import By


# 使用方法：
# driver.find_element(By.定位方法，‘元素信息’)
driver.find_element(By.ID, 'foo')


# 使用中的定位方法和普通的定位方法是一致的。

from selenium import webdriver
from selenium.webdriver.common.by import By

# 选择浏览器
driver = webdriver.Chrome()

# 进入百度网站
driver.get('https://www.baidu.com')

# 通过find_element定位输入框
driver.find_element(By.ID,'kw').send_keys('python')
'''