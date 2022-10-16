# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/15 16:21:06

#  环境安装  pip install aiohttp
# 使用该模块中的 ClientSession
import aiohttp
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
    # response = requests.get(url=url)
    
    # aiohttp: 基于异步网络请求的模块  请看 07-aiohttp实现多任务异步协程.py
    # 利用 aiohttp.ClientSession() 返回一个对象，取名为：session
    async with aiohttp.ClientSession() as session:
        # 进行 session 对象发送请求
        # 所有的 with 前边都需要 async 进行修饰，固定写法
        # 请求对象返回一个 response 响应数据对象
        
        # get(),post()：
        # 如果要进行UA伪装，需要 headers = {}, get里用parame = {}， post里用data = {},代理proxy = 'http://ip:port' 是字符串，不再是字典
        async with await session.get(url=url) as response:   # get发起请求有网络IO阻塞，耗时阻塞，需挂起，挂起方法：await 关键字
            # text()返回的字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            
            # 注意：获取响应数据操作之前一定要使用 await 进行手动挂机，不然会报下边RuntimeWarning
            # 在异步网页请求中，只要碰到阻塞或等待的代码，就需要手动挂机
            page_text = await response.text()   # RuntimeWarning: Enable tracemalloc to get the object allocation traceback
            print(page_text)
        
    
    print(f'下载完毕 {url}')
    
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

