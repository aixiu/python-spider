# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/14 18:03:58

import asyncio

async def func():
    print('来玩呀')
    response = await asyncio.sleep(2)   # 理解为网络IO请求
    print('结束', response)

asyncio.run(func())


import asyncio

async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def func():
    print('执行协程函数内部代码')
    
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行，当前协程挂机时，事件循环可以去执行其他协程（任务）。
    response = await others()
    print('IO请求结束，结果为：', response)
    
asyncio.run(func())
    
