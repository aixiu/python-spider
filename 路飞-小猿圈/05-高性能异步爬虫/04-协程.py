# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/14 10:09:12

'''
单线程+异步协和（推荐）
    event_loop: 事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。
    
    coroutine: 协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。    
    我们可以使用， async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。
    
    task: 任务，它是对协程对象的进一步封装，包含了任务的各个状态。
    
    futrue: 代表将来执行或还没有执行的任务，实际上和 task 没有本质区别。
    
    async: 定义一个协程。
    
    await 用来挂机阻塞方法的执行。
'''

import asyncio

async def request(url):
    print(f'正在请求的url是{url}')
    print(f'请求成功{url}')
    return url
    
# async 修饰的函数，调用之后返回的是一个协程对    
c = request('www.baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()

# # 将协程对象注册到loop中，然后启动loop  即可以实现注册，同时也启动循环
# loop.run_until_complete(c)


# task的使用

# loop = asyncio.get_event_loop()
# # 基于 loop创建了一个 task对象
# task = loop.create_task(c)
# print(task)

# # 执行
# loop.run_until_complete(task)
# print(task)


# future的使中用

# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)

# loop.run_until_complete(task)
# print(task)


# 绑定回调
def callback_func(task):
    # result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())
    
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)