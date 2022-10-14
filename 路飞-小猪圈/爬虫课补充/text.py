# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/14 11:30:52

# import asyncio

# @asyncio.coroutine
# def func1():
#     print(1)
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
#     print(2)

# @asyncio.coroutine
# def func2():
#     print(3)
#     yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
#     print(4)

# tasks = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))





# import asyncio

# async def func1():
#     print(1)
#     await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
#     print(2)

# async def func2():
#     print(3)
#     await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
#     print(4)

# tasks = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))






# import requests

# def download_image(url):
#     print('开始下载：', url)
#     # 发送网络请求，下载图片
#     response = requests.get(url)
#     print('下载完成')
#     # 图片保存到本地文件
#     file_name = url.rsplit('/')[-1]
#     with open(file_name, mode='wb') as fp:
#         fp.write(response.content)

# if __name__ == '__main__':
#     url_list = [
#         'http://image2.pearvideo.com/cont/20221012/13293812-170223-1.png',
#         'http://image2.pearvideo.com/cont/20200729/cont-1688740-12438860.png',
#         'http://image.pearvideo.com/cont/20210723/cont-1736170-12605892.png'
#     ]

#     for item in url_list:
#             download_image(item)




import asyncio

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'

async def main():
    print('main开始')
    
    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    task1 = asyncio.create_task(func())
    
    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    task2 = asyncio.create_task(func())
    
    print('main结束')
    
    # 当执行某协程遇到 IO 操作时，会自动化切换执行其他任务。
    # 此处的 await 是等待相对应的协程全都执行完毕并获取取结果
    
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)
    
asyncio.run(main())
    
