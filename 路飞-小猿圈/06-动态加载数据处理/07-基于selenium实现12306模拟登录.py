# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/17 17:48:24

from selenium import webdriver
from selenium.webdriver.edge.service import Service
# 无头Edge浏览器库及规避检测
from selenium.webdriver.edge.options import Options
# 导入动作链对应的类
from selenium.webdriver import ActionChains
import time

# 参考：https://blog.csdn.net/m0_54490473/article/details/122751814

# 创建一个参数对象，用来控制 Edge以无界面模式打开
edge_options = Options()
# 反检测设置 #
# 规避被检测到的风险
# 开启开发者模式
# option = EdgeOptions()
edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 去掉：浏览器上方有“Chrome正受到自动测试软件的控制
edge_options.add_experimental_option("detach", True)
# 禁用启用Blink运行时的功能
edge_options.add_argument('--disable-blink-features=AutomationControlled')

# 将参数传给浏览器 (options=edge_options)
bro = webdriver.Edge(service=Service('./msedgedriver.exe'), options=edge_options)
bro.get('https://kyfw.12306.cn/otn/resources/login.html')

# 解决特征识别, 用来解决滑块出错，验证问题
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
bro.execute_script(script)

# 根据id获取用户账号输入框、密码输入框，并输入账号密码
time.sleep(2)
username_tag = bro.find_element(by='id', value='J-userName').send_keys('4815563@qq.com')
time.sleep(2)
password_tag = bro.find_element(by='id', value='J-password').send_keys('shendlax520')

# 根据id获取登录按钮并点击
login_btn = bro.find_element(by='id', value='J-login').click()

# 这里必须得休眠，不然运行速度太夸，代码难以定位到滑块
time.sleep(2)
span = bro.find_element(by='id', value='nc_1_n1z')

# 定义动作链，点击并拖拽
aco = ActionChains(bro)

# 点击并长按
aco.click_and_hold(span)

#perform()立即执行动作链操作
for i in range(10):
    aco.move_by_offset(36,0).perform()
    time.sleep(0.3)
    
# 释放动作链
aco.release()
time.sleep(2)

# 点击登录后的弹窗 确定 按钮
ok_btn = bro.find_element(by='class name', value='ok').click()

time.sleep(5)
bro.quit()
