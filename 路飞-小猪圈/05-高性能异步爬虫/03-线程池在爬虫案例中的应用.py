# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/13 18:14:06

import requests
from lxml import etree
import random
import os
from multiprocessing.dummy import Pool

# 需求：爬取梨视频的视频数据
# 原则：线程池处理的是阻塞且 较为 耗时的操作
# 官网url = http://www.pearvideo.com/category_5
# 真实地址获取资料: https://www.cnblogs.com/qianhu/p/14027192.html

# 生成一个存视频的文件夹
if not os.path.exists('./video'):
    os.mkdir('./video')
    
file_path = './video'
        
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',    
}
# 对下述 url发起请求，解析出视频详情页的 url 和视频名称
url = 'http://www.pearvideo.com/category_5'

page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)

li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')

full_mp4_info_list = []

for li in li_list:
    detail_url = f'http://www.pearvideo.com/{li.xpath("./div/a/@href")[0]}'
    name = f'{li.xpath("./div/a/div[2]/text()")[0]}.mp4'
    
    # 对详情页的url发起请求
    detail_page = requests.get(url=detail_url, headers=headers).text
    
    # 从详情页中解析出视频的地址 url
    mv_id = detail_url.split('video_')[1]
    mrd = random.random()
    
    params = {
        'contId': mv_id,
        'mrd': mrd,
    }
    
    ajax_url = f'http://www.pearvideo.com/videoStatus.jsp'
    
    # 加了'Referer': 'https://www.pearvideo.com/video_1708144'后就不会显示该视频已下架了
    ajax_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
        'Referer': f'https://www.pearvideo.com/video_{mv_id}'
    }
    
    json_obj = requests.get(url=ajax_url, headers=ajax_headers, params=params).json()
    
    video_url = json_obj["videoInfo"]['videos']["srcUrl"]
    
    # 此处视频地址做了加密即ajax中得到的地址需要加上cont-,并且修改一段数字为id才是真地址
    # 真地址查找方法：F12--网络--媒体 就能看到真识地址，只需要将得到的json伪地址，换成真地址即可
    # 真地址："https://video.pearvideo.com/mp4/third/20201120/cont-1708144-10305425-222728-hd.mp4"
    # 伪地址："https://video.pearvideo.com/mp4/third/20201120/1606132035863-10305425-222728-hd.mp4"

    # 做字符串处理，得到真实url
    # 获取并替换最后一部分字符串
    end_url = video_url.split('/')[-1]
    new_end_url = end_url.replace(f'{end_url.split("-")[0]}', f'cont-{mv_id}')
    
    # 拼接url的开始部分
    start_url = ''
    start_url_list = video_url.split('/')
    for u_str in range(0, len(start_url_list)):
        if u_str < len(start_url_list) -1:
            start_url += f'{start_url_list[u_str]}/'
            
    # 完整的 url        
    new_url = f'{start_url}{new_end_url}'
    
    mp4_data = {
        'name': name,
        'url': new_url
    }
    
    full_mp4_info_list.append(mp4_data)
    
# 使用线程池对视频数据进行请求(较为耗时的阻塞操作)
def get_video_data(dic):
    url = dic['url']
    name = dic['name']
    print(f'{name}  ==> 正在下载！')
    data = requests.get(url=url, headers=headers, timeout=20).content
    # 持久化存储操作
    with open(f'{file_path}/{name}', mode='wb') as fp:
        fp.write(data)
        print(f'{name}  ==> 下载完毕！')
    
pool = Pool(4)  #  实例化四个，因为上边只有四个地址

# map() 第一个参数为函数,第二个参数为可迭代对象  作用机制,把可迭代对象的每一项内容,交给前边的函数处理
pool.map(get_video_data, full_mp4_info_list)

# 这里的pool.close()是说关闭pool，使其不在接受新的（主进程）任务
pool.close()

# 这里的pool.join()是说：主进程阻塞后，让子进程继续运行完成，子进程运行完后，再把主进程全部关掉。
pool.join()
    