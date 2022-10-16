# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/15 15:34:47

import requests
import asyncio
import time

start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom',
]

async def get_page(url):
    print(f'正在下载 {url}')
    
    # response.get是基于同步的，必须使用基于异步的网络请求模块进行指定 url的请求发送
    response = requests.get(url=url)
    
    # aiohttp: 基于异步网络请求的模块  请看 07-aiohttp实现多任务异步协程.py
    
    print(f'下载完毕 {response.text}')
    
tasks = []   # 多任务列表

for url in urls:
    c = get_page(url)   # 函数get_page返回一个 async协程对象
    task = asyncio.ensure_future(c)   # 将 async协程对象封装到任务对象 task 当中
    tasks.append(task)   #  将任务对象，添加到任务列表中
    
# 将任务列表注册到循环事件中
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print(f'总耗时：{end - start}')
