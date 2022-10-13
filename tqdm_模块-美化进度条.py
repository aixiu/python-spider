#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from tqdm import trange
from tqdm import tqdm
import time

"""
原文：https://blog.csdn.net/qq_43799400/article/details/123550855
    iterable: 可迭代的对象, 在手动更新时不需要进行设置
    desc: 字符串, 进度条左边的描述文字
    total: 总的项目数
    leave: bool值, 迭代完成后是否保留进度条
    file: 输出指向位置, 默认是终端, 一般不需要设置
    ncols: 调整进度条宽度, 默认是根据环境自动调节长度, 如果设置为0, 就没有进度条, 只有输出的信息
    unit: 描述处理项目的文字, 默认是'it', 例如: 100 it/s, 处理照片的话设置为'img' ,则为 100 img/s
    unit_scale: 自动根据国际标准进行项目处理速度单位的换算, 例如 100000 it/s >> 100k it/s
    
其它: https://blog.csdn.net/wxd1233/article/details/118371404

"""

# 使用trange
# trange(i) 是 tqdm(range(i)) 的简单写法

# for i in trange(100):
#     time.sleep(0.1)
    
for i in tqdm(range(50), '进度条'):
    time.sleep(0.1)
    
    
# tqdm模块是python进度条库，tqdm加载一个可迭代对象，并以进度条的形式实时显示该可迭代对象的加载进度。

# 一、tqdm的基本使用
from tqdm import tqdm
import time

# range(100)是加载的迭代器，desc是进度条的描述文字。
for i in tqdm(range(100), desc='Processing'):
    time.sleep(0.05)


# output：
# Processing: 100%|██████████| 100/100 [00:06<00:00, 15.81it/s]

        

# 二、进度条的迭代和进度条名字的设置
from tqdm import tqdm
import time

data=list(range(1000))
data_bar=tqdm(data)   # 将data设置为进度条
for i in data_bar:    # 进度条可以迭代
    data_bar.set_description("Processing "+str(i))   # 在不同时刻设置进度条的名字
    time.sleep(0.05)


# output：
# Processing 202:  20%|██        | 202/1000 [00:12<00:50, 15.93it/s]

# 上面的程序中，我们设置在0-1000内不断将进度条名字设置为正在加载的数字。可以看到进度条到20%的时候，加载到了202
        

# 三、tqdm() 的参数
# tqdm() 的源码为：

# def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None,
#                  ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
#                  ascii=None, disable=False, unit='it', unit_scale=False,
#                  dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
#                  position=None, postfix=None, unit_divisor=1000, write_bytes=None,
#                  lock_args=None, nrows=None, colour=None, delay=0, gui=False,
#                  **kwargs):

# 其中各个参数的含义为：

    # iterable: 可迭代的对象, 在手动更新时不需要进行设置
    # desc: 字符串, 进度条左边的描述文字
    # total: 总的项目数
    # leave: bool值, 迭代完成后是否保留进度条
    # file: 输出指向位置, 默认是终端, 一般不需要设置
    # ncols: 调整进度条宽度, 默认是根据环境自动调节长度, 如果设置为0, 就没有进度条, 只有输出的信息
    # unit: 描述处理项目的文字, 默认是'it', 例如: 100 it/s, 处理照片的话设置为'img' ,则为 100 img/s
    # unit_scale: 自动根据国际标准进行项目处理速度单位的换算, 例如 100000 it/s >> 100k it/s
        

# 四、深度学习网络训练中如何有效使用tqdm
# 比如数据集很大时，我们想实时知道已经训练了多少数据，就可以把data_loader设置为进度条对象，如下面的代码所示：

from tqdm import tqdm
from torch.utils.data import DataLoader

train_loader=DataLoader(dataset,shuffle=True,batch_size=16)   # 假设已知dataset
epochs=10
for epoch in range(epochs):
    # 此处省略若干步骤
    train_bar = tqdm(train_loader)   # 实时显示加载了多少数据
    for step, data in enumerate(train_bar):
        # 此处省略若干步骤
        train_bar.desc = f"train epoch [{epoch+1}/{epochs}]   loss= {loss:.3f}"


# output：
# train epoch [1/10]   loss= 1.462:  11%|█         | 23/207 [00:37<05:00,  1.63s/it]