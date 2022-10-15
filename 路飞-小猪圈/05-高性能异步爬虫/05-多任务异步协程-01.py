# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/15 11:58:27

import asyncio
import time

async def request(url):
    print(f'正在下载:{url}')
    
    # 在异步协程中，如果出现了同步模块相关的代码，那么就无法实现异步。
    # time.sleep 就是同步阻塞
    # time.sleep(2)
    
    # asyncio.sleep 就是异步阻塞
    # 在 asyncio中遇到阻塞操作，必须进行手动挂起，使用 await。
    await asyncio.sleep(2)
    
    print(f'下载完毕:{url}')
 
start = time.time()   
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.doubanjiang.com'
]

# 任务列表：存放多个任务对象
stasks = []

for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
    
loop = asyncio.get_event_loop()
# 固定语法格式，需要将任务列表封装在 wait()中
loop.run_until_complete(asyncio.wait(stasks))

print(f'{time.time() - start}')  