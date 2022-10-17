# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/17 11:04:59

from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

bro = webdriver.Edge(service=Service('./msedgedriver.exe'))

bro.get('https://i.qq.com/')

bro.switch_to.frame('login_frame')
a_tag = bro.find_element(by='id', value='switcher_plogin').click()


userName_tag = bro.find_element(by='id', value='u').send_keys('4815563')
time.sleep(1)
password_tag = bro.find_element(by='id', value='p').send_keys('shendlax520xy3')
time.sleep(1)
btn = bro.find_element(by='id', value='login_button').click()

time.sleep(3)

bro.quit()