# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/13 17:53:40

import time

# # 单线程串行方式执行
# def get_page(str):
#     print(f'正在下载：{str}')
#     time.sleep(2)
#     print(f'下载成功：{str}')
    
# name_list = ['xiaozi', 'aa', 'bb', 'cc']

# start_time = time.time()

# for i in range(len(name_list)):
#     get_page(name_list[i])
    
# end_time = time.time()

# print(f'{end_time - start_time} second')


from multiprocessing.dummy import Pool
# 导入线程池模块对应的类 （叫进程池？老师讲错了）
# 使用线程池方式执行

start_time = time.time()
def get_page(str):
    print(f'正在下载：{str}')
    time.sleep(2)
    print(f'下载成功：{str}')
    
name_list = ['xiaozi', 'aa', 'bb', 'cc']

# 实例化一个线程池对象
pool = Pool(4)
# 将列表中每一个元素传递给 get_page 进行处理
pool.map(get_page, name_list)
    
end_time = time.time()

print(f'{end_time - start_time} second')

