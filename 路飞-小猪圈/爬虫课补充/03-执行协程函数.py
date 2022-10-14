# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/14 17:54:58

import asyncio

async def func():
    print('快来搞我吧')

result = func()

# 去生成或获取一个事件循环
# loop = asyncio.get_event_loop()

# 将任务放到 “任务列表”
# loop.run_until_complete(result)

asyncio.run(result)   # python3.7 可以用这一行代替上边的两行