# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/14 23:38:12

# import asyncio

# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回值'

# async def main():
#     print('main开始')

#     task_list = [
#         asyncio.create_task(func(), name="n1"),
#         asyncio.create_task(func(), name="n2")
#     ]
    
#     print('main结束')
    
#     done, pending = await asyncio.wait(task_list, timeout=None)
#     print(done)

    
# asyncio.run(main())




# import asyncio

# async def func():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return '返回值'

# task_list = [
#     func(),
#     func()
# ]
    
# done, pending = asyncio.run(asyncio.wait(task_list))
# print(done)




import asyncio

async def set_affter(fut):
    await asyncio.sleep(2)
    fut.set_result('666')
    
async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    
    # 创建一个任务(Future 对象)，没绑定任何行为，则这个任务永远不知道什么时候结束。
    fut = loop.create_future()
    
    # 创建一个任务（Task对象），绑定了 set_after函数，函数内部在2s之后，会给fut赋值
    # 即手动设置 future 作雾的最终结翰林，那么 fut就可以结束了。
    await loop.create_task(set_affter(fut))
    
    # 等待 Future 对象获取 最终结果，否则一直等下去
    data = await fut
    print(data)
    
asyncio.run(main())