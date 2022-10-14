# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/14 12:26:46

import requests

def download_image(url):
    print('开始下载：', url)
    # 发送网络请求，下载图片
    response = requests.get(url)
    print('下载完成')
    # 图片保存到本地文件
    file_name = url.rsplit('/')[-1]
    with open(file_name, mode='wb') as fp:
        fp.write(response.content)

if __name__ == '__main__':
    url_list = [
        'http://image2.pearvideo.com/cont/20221012/13293812-170223-1.png',
        'http://image2.pearvideo.com/cont/20200729/cont-1688740-12438860.png',
        'http://image.pearvideo.com/cont/20210723/cont-1736170-12605892.png'
    ]

    for item in url_list:
            download_image(item)